# -*- coding: utf-8 -*-
import test111
print(test111.a)  # 打印变量“a”

test111.hi()  # 调用函数“hi”

print(test111.Go1.a)  # 打印类属性“a”
test111.Go1.do1()  # 调用类方法“Go1”

A = test111.Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”