# -*- coding: utf-8 -*-

class 出租车():
    def __init__(self,price,max_gl,max_p):
        self.price=price
        self.max_gl=max_gl
        self.max_p=max_p

    def 计费(self):
        self.记录行程()
        self.统计费用()
        self.结算信息()

    def 记录行程(self):
        self.公里数 = float(input('请输入行程公里数：'))

    def 统计费用(self):
        if self.公里数 <= self.max_gl:
            self.费用 = self.max_p
        else:
            self.费用 = self.max_p + (self.公里数 - self.max_gl) * (self.price)


    def 结算信息(self):
         print('费用一共是：' + str(self.费用) + '元')

class 电动车(出租车):
    def 统计费用(self):
        if self.公里数 <= self.max_gl:
            self.费用 = self.max_p
        else:
            self.费用 = (self.max_p + (self.公里数 - self.max_gl) * (self.price))*0.8

小王的出租车 = 出租车(2.5,3,15)
小王的出租车.计费()

小李的电动车 = 电动车(2.5,3,15)
小李的电动车.计费()