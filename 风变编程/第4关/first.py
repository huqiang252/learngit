# -*- coding: utf-8 -*-
list1 = [{'嫉妒':'envy'},{'恨':'hatred'},{'爱':'love'}]

print(list1[2]['爱'])


# 第一步：取出列表中的第三个元素（list1[2]），字典{'爱':'love'}；

# 第二步：取出list1[2]中键'爱'所对应的值，即'love’（list1[2]['爱']）。

dict1 = {1:['cake','scone','puff'],2:['London','Bristol','Bath'],3:['love','hatred','envy']}

print(dict1[3][0])


# 第一步：取出字典中键为3对应的值（dict1[3]），即['love','hatred','envy']。

# 第二步：再取出列表['love','hatred','envy']中的第一个元素（dict1[3][0]）。


tuple1 = ('A','B')

list2 = [('A','B'),('C','D'),('E','F')]

print(tuple1[0])

print(list2[1][1])


# 从代码里，也可看出：1.元组内数据的提取也是用偏移量；2.元组也支持互相嵌套。
