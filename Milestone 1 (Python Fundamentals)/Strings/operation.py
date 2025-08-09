### Basic String Operations:


# Concatenation:
"hello" + "world" # → "helloworld"

# Length of string:
len("hello") #  → 5

# Accessing characters (Indexing):
text = "hello"
print(text[0])  # 'h'
print(text[-1]) # 'o'

# Slicing:
text = "hello world"
print(text[0:5])   # 'hello'
print(text[6:])    # 'world'

# String Methods (Useful Built-in Functions):
# Uppercase / Lowercase:
"hello".upper()   # 'HELLO'
"WORLD".lower()   # 'world'

# Replace:
"hello world".replace("world", "Python")  # 'hello Python'

# Split and Join:
"a,b,c".split(",")           # ['a', 'b', 'c']
"-".join(["a", "b", "c"])    # 'a-b-c'

# Strip (Remove whitespace):
"  hello  ".strip()  # 'hello'

# Startswith / Endswith:
"Python".startswith("Py")  # True
"Python".endswith("on")    # True

# Find and Count:
"banana".find("na")   # return 1st idx of 1st occurr: 2
"banana".count("a")   # 3

#======================#
# Formatting Strings:  #
#======================#

# f-strings:
name = "Rasel"
age = 25
f"Hello, my name is {name} and I am {age} years old."


#String Check Methods (Return True/False):
"abc".isalpha()     # True
"123".isdigit()     # True
"abc123".isalnum()  # True
"   ".isspace()     # True
"Hello".istitle()   # True


