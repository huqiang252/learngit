# -*- coding: utf-8 -*-
'''九九乘法表'''
for row in range(1,10):
    for columns in range(1,row+1):
        result=columns*row
        print('{}*{}={}'.format(columns,row,result),end='\t')
    print()