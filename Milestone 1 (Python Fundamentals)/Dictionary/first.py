# =============================================== #
#               Instructor Information            #
# ------------------------------------------------#
# Name     : Md. Rasel Sarker                     #
# Email    : rasel.sarker6933@gmail.com           #
# WhatsApp : +880 1581-528651                     #
# =============================================== #


# student = {                           # "key": "value" pairs
#     "name": "Rasel sarker",
#     "age": 25,
#     "dept": "CSE",
#     "cgpa": 3.75,
#     "skills": ["Python", "ML", "C++"],
# }

#======================#
# Basic info           #
#======================#
# print(student)  
# student["name"]      # Output: 'Rasel sarker'
# student["cgpa"]      # Output: 3.75
# student["dept"]      # Output: 'CSE'
# student["skills"]    # Output: ['Python', 'ML', 'C++']

# student["key"] = "value"   # assign new value


#======================#
# Value reassignment   #
#======================#
# student["name"] = "Rasel Ahmed"  # Reassigning the value of "name"
# student["age"] = 26              # Reassigning the value of "age"
# print(student)

#===========================#
# Value in null dictionary  #
#===========================#
# info = {}
# info["name"] = "Roots of intelligence" 
# info["age"] = 5
# info["dept"] = "Cognitive Science"
# print(info) 


#=============================#
# Nested dictionary in python #
#=============================#
student = {
    "name": "Rasel sarker",
    "age": 25,
    "score": {
        "Machine Learning": 90,
        "Deep Learning": 85,
        "Generative AI": 88,
        "NLP": 92,
        "Computer Vision": 87,
    },
}

print(student)
print(len(student))

# 1. Get value by key
print(student.get("name"))  # Output: 'Rasel sarker'
print(student.get("name1"))  # error: None

# 2. Get all keys
print(student.keys())  # Output: dict_keys(['name', 'age', 'score'])

# 3. Get all values
print(student.values())  # Output: dict_values([...])
print(list[student.values()])

# 4. Get all key-value pairs as tuples
print(student.items())  
# Output: dict_items([('name', 'Rasel sarker'), ('age', 25), ('score': {...})])
print(list[student.items()])

# 5. Update dictionary
student.update({"email": "rasel@example.com"})
print(student)

# 6. Remove a key-value pair
student.pop("age")
print(student)

# 7. Set default value if key doesn’t exist
student.setdefault("phone", "Not provided")
print(student)

# 8. Delete all items
# student.clear()
# print(student)

# 9. Copy the dictionary
student_copy = student.copy()
print(student_copy)

# 10. Create dictionary from keys
keys = ["name", "age", "email"]
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

# 11. Convert dictionary to list of key-value pairs
pairs = list(student.items())
print(pairs)