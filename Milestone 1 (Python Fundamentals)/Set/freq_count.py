## Problem 3: Count frequency of each subject

from collections import Counter

subject_list = ["python", "java", "C++", "python", "javascript",
                "java", "python", "java", "C++", "C"]

subject_count = Counter(subject_list)
print(subject_count)