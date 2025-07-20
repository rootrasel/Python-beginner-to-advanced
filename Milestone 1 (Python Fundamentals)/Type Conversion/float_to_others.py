x = 11.75

print("Original float number is: ", x)
print("Integer number is: ", int(x))
print('String is: "' + str(x) + '"')
print("Boolean is: ", bool(x))
print("Complex number is: ", complex(x))
print("List is: ", [x])         # Correct way to make a list with x inside
print("Tuple is: ", (x,))       # Tuple with one element needs a comma  
print("Set is: ", {x})          # Set with one element
print("Dictionary is: ", {x: str(x)})  # Dictionary with x as