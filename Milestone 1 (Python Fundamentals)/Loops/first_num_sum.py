n = int(input("Enter a number: "))

# sum = 0
# for el in range(1, n + 1):
#     sum += el
# print("The sum of the first", n, "numbers is:", sum)

# while n > 0:
#     sum = 0
#     for el in range(1, n + 1):
#         sum += el
#     print("The sum of the first", n, "numbers is:", sum)
#     n = int(input("Enter a number (0 to exit): "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of the first", n, "numbers is:", sum)