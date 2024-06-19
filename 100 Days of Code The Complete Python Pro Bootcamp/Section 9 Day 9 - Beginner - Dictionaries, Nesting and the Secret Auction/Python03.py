# Exercise - Lesson  21 - Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for student in student_scores:
    if student_scores[student] >= 91:
        student_scores[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_scores[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_scores[student] = "Acceptable"
    else:
        student_scores[student] = "Fail"

print(student_scores)
