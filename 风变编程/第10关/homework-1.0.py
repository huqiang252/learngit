# -*- coding: utf-8 -*-
#箭刀石头布
import random,time
computer_choice=['剪刀','石头','布']
user_choice=['剪刀','石头','布']
print('电脑随机出拳了')
computers = random.choice(computer_choice)
time.sleep(1.5)
my_choices = input('请输入我们的出拳类型(石头，剪刀，布)')
while my_choices not in user_choice:
    print('输入错误，请重新出拳')
    my_choices = input('请输入我们的出拳类型(石头，剪刀，布)')

print('双方亮拳-------->')
print('电脑的出拳：{}'.format(computers))
print('我的出拳：{}'.format(my_choices))

#判断胜负
if my_choices=='剪刀':
    if computers==my_choices:
        print('打平了')
    elif computers=='石头':
        print('你输了')
    else:
        print('你赢了')
elif my_choices=='石头':
    if computers==my_choices:
        print('打平了')
    elif computers=='布':
        print('你输了')
    else:
        print('你赢了')
else:
    if computers==my_choices:
        print('打平了')
    elif computers=='剪刀':
        print('你输了')
    else:
        print('你赢了')