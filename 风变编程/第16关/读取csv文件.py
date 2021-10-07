# -*- coding: utf-8 -*-
import csv
with open('test.csv','r',newline='',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
print('读取结束了。。。')