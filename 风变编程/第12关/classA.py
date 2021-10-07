# -*- coding: utf-8 -*-
class 类A():
    变量1 = 100
    变量2 = 200

    def 函数2():
        print('我们需要变量')

    @classmethod
    def 函数1(cls):
        print(cls.变量1)
        print(cls.变量2)



类A.函数1()
类A.函数2()