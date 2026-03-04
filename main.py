"""
Project: Student Database Logic
Author: Foday C. Koroma 
Description: This script shows manual iteration over a dictionary to find maximum value without using built-in functions like max().
"""
student_db = {
  "Foday": 98,
  "John": 83,
  "Mary": 71,
  "Ali": 97,
  "Sarah":45
}
highest_name = ""
highest_score = -1
for name in student_db:
  current_score = student_db[name]
  if current_score > highest_score:
    highest_score = current_score
    highest_name = name
print(f"Highest scorer: {highest_name} {highest_score}") 
student_db["Sarah"] = 88
del student_db["Mary"]
print("Final database:", student_db)