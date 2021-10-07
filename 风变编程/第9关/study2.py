# -*- coding: utf-8 -*-
#位置参数、默认参数、不定长参数的使用
def chide(xiaocai,zhushi,tianpin='黑森林可乐',*shaokao):

    print('一盘小菜：'+xiaocai)

    print('主食来啦：'+zhushi)

    print('一份甜品：'+tianpin)

    for i in shaokao:
        print('烧烤之一：'+i)

chide('炒豆苗','馒头','樱桃布丁','羊肉串','肉筋','板筋','烤韭菜')

