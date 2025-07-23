n = int(input("Enter a number: "))

factorial = 1
for el in range(1, n + 1):
    factorial *= el
print("The factorial of", n, "is:", factorial)