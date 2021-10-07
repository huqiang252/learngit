# -*- coding: utf-8 -*-
'''被动入坑需要普获异常'''

try:
    age = int(input('请输入你的年龄：'))
except ValueError:
    print('请输入整数')



