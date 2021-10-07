# -*- coding: utf-8 -*-
import random,time
def poker():
    '''每张扑克牌的展现形式是一个元组：(花色，大小)。'''
    color=['红心','方块','梅花','黑桃']
    type(range(2,11))
    num=list(range(2,11))
    num.extend(['J','Q','K','A'])
    return [(x,y) for x in color for y in num]





def than_the_size(name1,name2):
    print('开始发牌')
    poker_name1 = random.choice(poker())
    time.sleep(1)
    print(name1, poker_name1)
    poker_name2 = random.choice(poker())
    time.sleep(2)
    print(name2, poker_name2)
    poker1=poker_name1[1]
    poker2=poker_name2[1]
    if poker1>poker2:
        return poker_name1
    elif poker1<poker2:
        return poker_name2
    else:
        '一样大'


print('比大小结果:',than_the_size('王五','李四'))

