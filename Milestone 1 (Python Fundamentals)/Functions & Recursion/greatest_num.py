def greatest_num(a, b, c):
    """Return the greatest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
result = greatest_num(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {result}")

