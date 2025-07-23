# set1 = {1, 2, 3, 4, 5, 2, 1, 3, 4, 5}

# print("Initial Set:", set1) # duplicates are ignored

# set2 = {}
# print(set2)  # empty set: dict
# print(type(set2))  # <class 'dict'>


set2 = set()
print(set2)  # empty set: now set
print(type(set2))  # <class 'set'>


a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b))              # {1, 2, 3, 4}
print(a.intersection(b))       # {2, 3}
print(a.difference(b))         # {1}
print(a.symmetric_difference(b))  # {1, 4}
