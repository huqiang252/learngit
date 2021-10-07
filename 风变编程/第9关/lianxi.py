# -*- coding: utf-8 -*-
num2 = list(range(1,6))
num2.extend('ABCDE')
print(num2)
list2 = [m+n for m in ['天字', '地字'] for n in '一二']
list3 = [n*n for n in range(1,11) if n % 3 == 0]
print(list2)
print(list3)