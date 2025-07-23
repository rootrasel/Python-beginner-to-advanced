## Problem 5: Combine marks from two subjects

math = {"Rasel": 85, "Nila": 90, "Rumi": 78}
english = {"Rasel": 88, "Nila": 85, "Rumi": 82}

result = {}

for name in math:
    result[name] = {
        "Math": math[name],
        "English": english.get(name, 0),
        "Total": math[name] + english.get(name, 0)
    }

print(result)