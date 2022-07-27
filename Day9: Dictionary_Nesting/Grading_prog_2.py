student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    # print(key)
    # print(student_scores[key])
    if student_scores[key] > 90:
         student_grades[key]= "Outstanding"
    elif student_scores[key] >= 81:
         student_grades[key]= "Exceeds Expectation"
    elif student_scores[key] >= 71:
         student_grades[key]= "Acceptable"
    elif student_scores[key]  <= 70:
        student_grades[key]= "Fail"

print(student_grades)
