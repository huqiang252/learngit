# -*- coding: utf-8 -*-
#猜数字游戏
import random

number=random.randint(1,100)

flagNum=3
while flagNum:
    guessNumber=int(input('请猜一个1~100之间的整数:'))
    str='猜大了' if guessNumber>number else ('猜小了' if guessNumber<number else '猜对了')
    print(str)
    if str=='猜对了':
        break
    flagNum-=1
else:
    print('3次都没有猜测对哦')
