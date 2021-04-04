M = int(input())
lessons = []
for i in range(M):
    present_number = int(input())
    students_present = []
    for j in range(present_number):
        students_present.append(input())
    lessons.append(students_present)

for student in lessons[0]:
    is_always_present = True
    for i in range(1, len(lessons)):
        is_always_present *= lessons[i].__contains__(student)
    if is_always_present:
        print(student)
