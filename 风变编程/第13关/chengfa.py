# -*- coding: utf-8 -*-
class 乘法表():
    def __init__(self,n):
        self.n=n


    def 打印(self):
        for i in range(1,self.n+1):
            for x in range(1,i+1):
                print( '%d X %d = %d' % (i ,x ,i*x) ,end = '  ' )
            print('  ')

九九乘方表=乘法表(4)
九九乘方表.打印()