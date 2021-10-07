# -*- coding: utf-8 -*-
#列表合并并排序
A=[91, 95, 97, 99]
B=[92, 93, 96, 98]
new_C=A+B
new_C.sort()
print(new_C)

sum_C=0
for i in new_C:
    sum_C+=i
avg_C=sum_C/len(new_C)
print('A的平均价'+str(avg_C))

for i in new_C:
    if i<=avg_C:
        print(i)

