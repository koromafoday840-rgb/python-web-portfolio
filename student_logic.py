"""
Project: Student Performance Tracker
Author: Foday C. Koroma
Date: 6 March, 2026.
Description: "I built this script because I was tired of dealing with messy, unorganized academic data. It takes a raw list of student records and moves them into nested dictionaries, which makes searching for a specific student much faster and cuts out all the repeat information. I also added logic to automatically handle the math for subject averages and final grades so I can actually track how everyone is doing over the term without doing it by hand."
"""
# my tuple list of students records.
records = [
    ("Foday", "Maths", 96),
    ("Sarah", "Physics", 83),
    ("Ali", "Maths", 67),
    ("John", "Physics", 34),
    ("Mary", "Maths", 75),
    ("Foday", "Physics", 98),
    ("Sarah", "Maths", 64),
    ("Ali", "Physics", 81),
    ("John", "Maths", 69),
    ("Mary", "Physics", 65)
]

students = {}

for name, subject, score in records:
    students.setdefault(name, {})
    students[name].setdefault(subject, [])
    students[name][subject].append(score)


for name, subjects in students.items():
    print(f"\nstudent: {name}")
    
    total_sum = 0
    total_count = 0
    
    for subject, scores in subjects.items():
       
        try:
            subject_average = sum(scores) / len(scores)
        except ZeroDivisionError:
            subject_average = 0.0
        
        print(f"{subject} average: {subject_average:.2f}")
        
        total_sum += sum(scores)
        total_count += len(scores)
    
    
    print(f"Overall average: {total_sum / total_count if total_count > 0 else 0.0:.2f}")