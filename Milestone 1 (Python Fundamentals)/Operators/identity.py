a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True 
print(a is c)       # False 
print(a == c)       # True 
print(a is not c)   # True
