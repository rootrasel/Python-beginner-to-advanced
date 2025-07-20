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