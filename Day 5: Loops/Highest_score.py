student_scores = input("Input score of the students: \n").split()

# Tranforms each of the objects in the list from a string to an integer
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max = 0

for score in student_scores:
    if score > max:
        max = score

print(f"the  highest score is : {max}")
