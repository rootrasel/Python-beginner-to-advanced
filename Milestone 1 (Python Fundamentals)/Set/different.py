# Problem 6: Find common and different subjects

student1 = {"python", "java", "C"}
student2 = {"python", "C++", "java", "html"}

common = student1.intersection(student2)
different = student1.symmetric_difference(student2)

print("Common Subjects:", common)
print("Different Subjects:", different)
