def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    sum = a + b
    return sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = calculate_sum(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")