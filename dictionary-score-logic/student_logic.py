"""
Project: Student Database Logic
Author: Foday C. Koroma
Date: 4 March, 2026.
Description: I use this code to  show manual iteration over a dictionary to find  maximum value without using built-in functions like max()
"""

# My assumed students 
student_db = {
    "Foday": 98,
    "John": 83,
    "Mary": 71,
    "Ali": 97,
    "Sarah": 45
}

highest_name = ""
highest_score = -1

# I use this  logic to find the highest score manually
for name in student_db:
    current_score = student_db[name]
    if current_score > highest_score:
        highest_score = current_score
        highest_name = name

print(f"Highest scorer: {highest_name} with a score of {highest_score}")

# I Update and delete the students in my dictionary
student_db["Sarah"] = 88
del student_db["Mary"]
print("Final database:", student_db)