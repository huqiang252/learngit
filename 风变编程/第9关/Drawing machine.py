# -*- coding: utf-8 -*-
#抽奖器

import random,time

def hellokitty_machine(*name):
    print(name)
    a=random.choice(name) #中奖名单中随意选择
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
        /\_)o<
        |      \\
        | O . O|
        \_____/
        '''
    print(image)
    print('恭喜'+a+'中奖了！')


hellokitty_machine('郭靖','黄蓉','杨过','欧阳锋')