def fibonacci_series(n):
    """Generate Fibonacci series up to n."""
    fib_series = []
    a = 0
    b = 1
    while a < n:
        fib_series.append(a)
        temp = a + b
        a = b
        b = temp 
    return fib_series

n = int(input("Enter a number: "))
result = fibonacci_series(n)
print(f"The Fibonacci series up to {n} is: {result}")