# -*- coding: utf-8 -*-
import os
list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']
with open ('poem2.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

print(lines)
with open('poem_new.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

os.replace('poem_new.txt', 'poem2.txt')
