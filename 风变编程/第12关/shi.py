# -*- coding: utf-8 -*-

class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']

    @classmethod
    def 念诗函数(cls,name):
        print('念给'+name+'的诗：')
        for i in cls.一首诗:
            print(i)

name='张三'
念诗类.念诗函数(name)