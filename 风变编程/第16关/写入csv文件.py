# -*- coding: utf-8 -*-
import csv
with open('test.csv','a',newline='',encoding='utf-8') as f:
    f_csv=csv.writer(f)
    f_csv.writerow([1,2,3,4,5])