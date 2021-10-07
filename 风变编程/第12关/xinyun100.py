# -*- coding: utf-8 -*-
class xinyun():

    @classmethod
    def show_bei(cls):
        number=cls.a
        str='好的，我把它存了起来，然后翻了888倍还给你:{}'.format(number*888)
        print(str)


xinyun.a=int(input('你的幸运数是多少？请输入一个整数。'))
xinyun.show_bei()