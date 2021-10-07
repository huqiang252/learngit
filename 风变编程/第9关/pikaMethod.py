# -*- coding: utf-8 -*-

# 一个简单的return。函数内部一旦遇到return语句，就会停止执行并返回结果。没有return语句的函数，
# Python也会在末尾隐性地加上return None，即返回None值（return None可以简写为return。）
# 所以你也会看到，我们接下来的很多例子是省略了return语句的


def pika1():
    print('我最喜欢的神奇宝贝是皮卡丘')
    return

pika1()