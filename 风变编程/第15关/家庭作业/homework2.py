# -*- coding: utf-8 -*-
list_test = ['一弦一柱思华年。\n','只是当时已惘然。']  # 将要默写的诗句放在列表里。
with open ('poem2.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)


with open('poem2.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)

# def shuru(*a):
#     return a
#
#
# tupa=shuru(2,'h',12.3,'bb')
# print(tupa)
# list=list(tupa)
# print(list)