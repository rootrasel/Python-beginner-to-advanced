# =============================================== #
#               Instructor Information            #
# ------------------------------------------------#
# Name     : Md. Rasel Sarker                     #
# Email    : rasel.sarker6933@gmail.com           #
# WhatsApp : +880 1581-528651                     #
# =============================================== #

# Set Operations in Python
set1 = {1, 2, 3, 4, 5}


#1. Add an Element
set1.add(6)


#2. Update with Multiple Elements
set1.update([7, 8])

#3. Remove an Element (Error if not found)
set1.remove(3)

# 4. Discard an Element (No Error if not found)
set1.discard(10)


#5. Pop Random Element
removed = set1.pop()


#6. Clear All Elements
set1.clear()


#7. Union (A ∪ B)
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))     # {1, 2, 3, 4, 5}


#8. Intersection (A ∩ B)
print(A.intersection(B))  # {3}


#9. Difference (A - B)
print(A.difference(B))    # {1, 2}


#10. Symmetric Difference (A △ B)
print(A.symmetric_difference(B))  # {1, 2, 4, 5}


#Set Relationship Checks
#11. Subset Check
A.issubset(B)


#12. Superset Check
A.issuperset(B)


#13. Disjoint Check
A.isdisjoint(B)


#14. Copy a Set
new_set = set1.copy()


#Example Summary:
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Symmetric Difference:", A ^ B)






