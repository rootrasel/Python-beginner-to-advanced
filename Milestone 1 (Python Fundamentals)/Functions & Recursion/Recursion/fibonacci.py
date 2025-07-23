def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example: Print first n terms
terms = int(input("How many terms? "))
for i in range(terms):
    print(fibonacci(i), end=' ')
