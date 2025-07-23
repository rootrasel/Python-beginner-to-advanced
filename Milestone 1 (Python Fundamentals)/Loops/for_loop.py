# Basic for loop examples in Python

#1. range() – For looping over numbers
for i in range(5):
    print(i)
    
#Output: 0 1 2 3 4

# 2. len() 
name = "Rasel sarker"
for i in range(len(name)):  # loop through in index and returns the num of items in a sequence
    print(name[i])
    
# 3. enumerate() – gives index and item same time.
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
    
# 4. zip() – Loop through two or more lists at once
names = ["A", "B", "C"]
scores = [90, 85, 75]

for name, score in zip(names, scores):
    print(name, score)
    
# 5. split() – splits a string into words (or parts)
text = "I love Python"
for word in text.split():
    print(word)
    
# 6. sorted() – returns a sorted version of a sequence
nums = [3, 1, 4, 2]
for n in sorted(nums):
    print(n)
    
#7. reversed() – Loops through a sequence in reverse order
for ch in reversed("hello"):
    print(ch)













# movie = ["Inception", "The Matrix", "Interstellar", "The Godfather"]

# for mv in movie:
#     print(mv)


# tuple_list = ("Superman", "Batman", "Spiderman", "Ironman", "Hulk", "MachineMan")
# for hero in tuple_list:
#     print(hero)

# chr = "RootsofInelligence"
# for char in chr:
#     print(char)


# num_list = "RootsofInelligence"
# for num in num_list:
#     if(num == 'e'):
#         print("Found 'e', breaking the loop.")
#         break
#     print(num)
    
# else:
#     print("Loop completed successfully.")

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for idx in numbers:
#     if(idx % 2 != 0):
#         print(idx)
#         continue
    
# print("Loop completed successfully.")

# numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 36, 100)
# x = 36

# idx = 0
# for el in numbers:
#     if(el == x):
#         print("Number found at idx", idx)
#     idx += 1
 

    
