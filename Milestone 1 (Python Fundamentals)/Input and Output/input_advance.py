# ##1. Formatted Output (advanced use of print()):
# name = "Rasel"
# age = 22
# print("Name: {}, Age: {}".format(name, age))  # old style
# print(f"Name: {name}, Age: {age}")  # f-string (modern & best)


# ##2. Escape Characters in Output:
# print("He said, \"Python is fun!\"")
# print("Line1\nLine2\tTabbed")


# ##3. Output Formatting (width, precision):
# pi = 3.1415926535
# print(f"Pi to 2 decimal places: {pi:.2f}")   # Pi to 2 decimal
# print(f"Number padded: {42:05d}")            # 00042


# ##4. Input validation (basic):
# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Invalid input! Please enter an integer.")
    
    
# 5. File I/O (very basic idea):
# Writing to file
with open("output.txt", "w") as f:
    f.write("Hello, How are you?")

# Reading from file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
    
    
## Using sep and end parameter
print("Roots", end="@")
print("of Intelligence")

# for formatting a date
print('09', '12', '2025', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')