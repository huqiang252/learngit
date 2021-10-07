# -*- coding: utf-8 -*-
import csv


with open(r'C:\Users\huqiang252\Desktop\test.csv','a+',newline='',encoding='utf-8') as csv_obj:
    writer=csv.writer(csv_obj) #csv对象生成一个writer对象
    print(type(writer))
    headers=['电影','豆瓣评分']
    writer.writerow(headers)
    writer.writerow(['银河护卫队','8.0'])
    writer.writerow(['复仇者联盟','8.1'])


with open(r'C:\Users\huqiang252\Desktop\test.csv','r',newline='',encoding='utf-8') as csv_obj2:
    reader=csv.reader(csv_obj2) #生成一个reader对象
    for row in reader:
        print(row)