# -*- coding: utf-8 -*-
#比大小

def than_the_size(i,j):
    '''输入两个数字，返回大的数字'''
    if i>j:
        return i
    elif i<j:
        return j
    else:
        return '一样大'

print(than_the_size(99**2,8080))