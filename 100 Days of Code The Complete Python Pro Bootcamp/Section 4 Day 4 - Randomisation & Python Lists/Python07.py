# Nested Lists
student1_grades = ["A-", "B+", "A+", "A-", "A"]
student2_grades = ["B+", "B+", "A", "A-", "B-"]
student3_grades = ["A+", "A+", "A-", "A", "B"]
grades_of_students = [student1_grades, student2_grades, student3_grades]
print(grades_of_students)
print(grades_of_students[0][1], end=" ")
print(grades_of_students[2][3], end=" ")
print(grades_of_students[1][3], end=" ")
