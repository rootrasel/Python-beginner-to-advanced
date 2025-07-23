def calculate_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  
num3 = int(input("Enter the third number: "))
result = calculate_avg(num1, num2, num3)
print(f"The average of {num1}, {num2}, and {num3} is: {result}")