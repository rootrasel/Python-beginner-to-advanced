a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True (both refer to same object)
print(a is c)       # False (same value, different object)
print(a == c)       # True (values are equal)
print(a is not c)   # True
