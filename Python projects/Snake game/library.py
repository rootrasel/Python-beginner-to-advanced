# app.py — Minimal Library Management System (Flask 3 + SQLite)
from datetime import datetime, timedelta
from typing import Optional
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# ---------------------- App & DB setup ----------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# --------------------------- Models -------------------------
class Book(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(200), nullable=False, index=True)
    author  = db.Column(db.String(120), nullable=False, index=True)
    copies  = db.Column(db.Integer, nullable=False, default=1)  # available copies
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

class Member(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)

class Loan(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    book_id    = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id  = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_at      = db.Column(db.DateTime, nullable=False)
    returned_at = db.Column(db.DateTime)

    book   = db.relationship("Book")
    member = db.relationship("Member")

# Create tables once at startup (Flask 3 compatible)
with app.app_context():
    db.create_all()

# ---------------------- Helpers -----------------------------
def bad_request(msg: str, code: int = 400):
    return jsonify({"ok": False, "error": msg}), code

@app.errorhandler(404)
def not_found(_):
    return bad_request("Not found", 404)

# ------------------------- Books ----------------------------
@app.post("/books")
def add_book():
    data = request.get_json(silent=True) or {}
    title  = (data.get("title") or "").strip()
    author = (data.get("author") or "").strip()
    copies = data.get("copies", 1)

    if not title or not author:
        return bad_request("title and author are required")
    try:
        copies = int(copies)
        if copies < 0:
            raise ValueError
    except Exception:
        return bad_request("copies must be a non-negative integer")

    b = Book(title=title, author=author, copies=copies)
    db.session.add(b); db.session.commit()
    return jsonify({"ok": True, "book_id": b.id})

@app.get("/books")
def list_books():
    q = Book.query
    if t := request.args.get("title"):
        q = q.filter(Book.title.ilike(f"%{t}%"))
    if a := request.args.get("author"):
        q = q.filter(Book.author.ilike(f"%{a}%"))

    # optional pagination: ?limit=20&offset=0
    try:
        limit  = int(request.args.get("limit", 100))
        offset = int(request.args.get("offset", 0))
    except ValueError:
        return bad_request("limit/offset must be integers")

    rows = q.order_by(Book.title).offset(offset).limit(limit).all()
    return jsonify([{
        "id": b.id, "title": b.title, "author": b.author,
        "copies": b.copies, "added_on": b.added_on.isoformat()
    } for b in rows])

# ------------------------ Members ---------------------------
@app.post("/members")
def add_member():
    data = request.get_json(silent=True) or {}
    name  = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    if not name or not email:
        return bad_request("name and email are required")

    if Member.query.filter_by(email=email).first():
        return bad_request("email already exists", 409)

    m = Member(name=name, email=email)
    db.session.add(m); db.session.commit()
    return jsonify({"ok": True, "member_id": m.id})

@app.get("/members")
def list_members():
    rows = Member.query.order_by(Member.name).all()
    return jsonify([{"id": m.id, "name": m.name, "email": m.email} for m in rows])

# -------------------- Borrow / Return -----------------------
@app.post("/loans/borrow")
def borrow_book():
    data = request.get_json(silent=True) or {}
    try:
        book_id   = int(data["book_id"])
        member_id = int(data["member_id"])
        due_days  = int(data.get("due_days", 14))
    except Exception:
        return bad_request("book_id, member_id must be integers")

    book   = Book.query.get(book_id)   or abort(404)
    member = Member.query.get(member_id) or abort(404)

    if book.copies <= 0:
        return bad_request("No copies available")

    loan = Loan(book=book, member=member,
                due_at=datetime.utcnow() + timedelta(days=due_days))
    book.copies -= 1
    db.session.add(loan); db.session.commit()

    return jsonify({"ok": True, "loan_id": loan.id,
                    "due_at": loan.due_at.isoformat()})

@app.post("/loans/return")
def return_book():
    data = request.get_json(silent=True) or {}
    try:
        loan_id = int(data["loan_id"])
    except Exception:
        return bad_request("loan_id is required and must be integer")

    loan = Loan.query.get(loan_id) or abort(404)
    if loan.returned_at:
        return bad_request("Already returned")

    loan.returned_at = datetime.utcnow()
    loan.book.copies += 1
    db.session.commit()
    return jsonify({"ok": True})

@app.get("/loans")
def list_loans():
    active = request.args.get("active")
    q = Loan.query
    if active == "1":
        q = q.filter(Loan.returned_at.is_(None))
    rows = q.order_by(Loan.borrowed_at.desc()).all()

    def row(l: Loan):
        status = ("returned" if l.returned_at else
                 ("overdue" if l.due_at < datetime.utcnow() else "borrowed"))
        return {
            "id": l.id, "book": l.book.title, "member": l.member.name,
            "borrowed_at": l.borrowed_at.isoformat(),
            "due_at": l.due_at.isoformat(),
            "returned_at": l.returned_at.isoformat() if l.returned_at else None,
            "status": status
        }

    return jsonify([row(l) for l in rows])

# ------------------------- Run ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
