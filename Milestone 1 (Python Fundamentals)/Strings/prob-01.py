# problem: 01
name = input("Enter your name: ")
print("name:", len(name))


# problem: 02
name = "$, Rasel, $500"
print("name:", name.count("$"))  


# Problem: 03 - Check if the name is a palindrome
name = input("Enter your name: ")

if name == name[::-1]:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


# Problem: 04 - convert a string to uppercase and lowercase
name = input("Enter your name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())


# Problem: 05 - count how many vowels('aeiouAEIOU') are present in a string.
name = input("Enter your name: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in name if char in vowels)
print("Number of vowels:", count)


# alternative way to count vowels
# Ask the user to enter their name
name = input("Enter your name: ")
vowels = 'aeiouAEIOU'
print("Vowels in your name:", vowels.count(name))


# alternative way to count vowels
name = input("Enter your name: ")
a_count = name.count('a') + name.count('A')
e_count = name.count('e') + name.count('E')
i_count = name.count('i') + name.count('I')
o_count = name.count('o') + name.count('O')
u_count = name.count('u') + name.count('U')

total = a_count + e_count + i_count + o_count + u_count
print("Number of vowels:", total)


# Set a counter to 0
# count = 0

# for char in name:
#     if char in vowels:
#         count += 1  # Increase count if it's a vowel

# print("Number of vowels:", count)

