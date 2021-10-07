# -*- coding: utf-8 -*-
students=['小明','小红','小刚']

# for i in range(3):
#     print(students)
#     student=students.pop(0)
#     students.append(student)

for i in range(3):
    print(students)
    no1=students[0]
    del students[0]
    students.append(no1)


