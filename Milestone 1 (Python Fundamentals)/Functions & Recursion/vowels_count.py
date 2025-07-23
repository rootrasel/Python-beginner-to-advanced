def vowels_count(s):
    """Count the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    found_vowels = []
    
    for char in s:
        if char in vowels:
            count += 1
            found_vowels.append(char)
    print(f"Vowels found: {', '.join(found_vowels)}")
    return count, char

s = input("Enter a string: ")
result = vowels_count(s)
print(f"The number of vowels in the string is: {result}")