# -*- coding: utf-8 -*-
file=open('1.txt','w',encoding='utf-8')
file.write('难念的金')
file.close()

file2=open('1.txt','r',encoding='utf-8')
print(file2.read())
file2.close()