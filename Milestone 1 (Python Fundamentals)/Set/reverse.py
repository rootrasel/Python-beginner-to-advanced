## Problem 4: Reverse word-meaning dictionary

original = {
    "sun": "a star",
    "moon": "a natural satellite",
    "earth": "a planet"
}

reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)