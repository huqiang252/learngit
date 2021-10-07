# -*- coding: utf-8 -*-
import xlwt

book=xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('new title')
valuelist=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
for i in range(len(valuelist)):
    for j in range(len(valuelist[i])):
        sheet.write(i,j,valuelist[i][j])
book.save('text.xls')