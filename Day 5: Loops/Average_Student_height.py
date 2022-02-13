student_heights = input("Input a list of student heights \n").split()
print(student_heights)
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print(student_heights[n])

print(student_heights)

total = 0
number = 0
for height in student_heights:
    total += height
    number += 1
print(total)
print(number)
average_height = round(total / number)
print(average_height)
