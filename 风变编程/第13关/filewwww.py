# -*- coding: utf-8 -*-
class 幸运():
    def 好运翻倍(self):
        print('好的，我把它存了起来，然后翻了888倍还给你：' + str(self.幸运数*888))

def 新好运翻倍(self):
    print('我是重写后的新函数')
    print('好的，我把它存了起来，然后翻了666倍还给你：'+str(self.幸运数*666))

幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))
实例 = 幸运()  # 实例化
幸运.好运翻倍=新好运翻倍
实例.好运翻倍()