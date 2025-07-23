# str input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# int input
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

# list input
numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]
print(f"You entered the numbers: {numbers_list}")

# boolean input
is_student = input("Are you a student? (yes/no): ").strip().lower()
is_student = is_student == 'yes'
print(f"Student status: {is_student}")

# Multiple str inputs in one line
name, age = input("Enter your name and age separated by a space: ").split()
print(f"Hello, {name}! You are {age} years old.")

# Multiple int inputs in one line
a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
print(f"You entered: a={a}, b={b}, c={c}")

# Multiple float inputs in one line
x, y, z = map(float, input("Enter three float numbers separated by spaces: ").split())
print(f"You entered: x={x}, y={y}, z={z}")

# Tuple input
tuple_input = input("Enter a tuple of numbers separated by commas: ")
tuple_numbers = tuple(int(num) for num in tuple_input.split(','))
print(f"You entered the tuple: {tuple_numbers}")

# Dictionary input
dict_input = input("Enter a dictionary in the format key1:value1,key2:value2: ")
dict_numbers = dict(item.split(':') for item in dict_input.split(','))  
print(f"You entered the dictionary: {dict_numbers}")

# Set input
set_input = input("Enter a set of numbers separated by spaces: ")
set_numbers = set(int(num) for num in set_input.split())
print(f"You entered the set: {set_numbers}")