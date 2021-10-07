# -*- coding: utf-8 -*-
import csv
print(dir(csv))
new_list=[]

#前面带__ 都是系统方法（不用理会）
for i in dir(csv):
    if i[:2] == '__':
        continue
    else:
        new_list.append(i)

print(new_list)