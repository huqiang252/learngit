# -*- coding: utf-8 -*-
import random,time
computer_choice=['剪刀','石头','布']
#亮拳,并显示胜负
def show_quan():
    print('电脑随机出拳了')
    computers = random.choice(computer_choice)
    time.sleep(1.5)
    my_choices = input('请输入我们的出拳类型(石头，剪刀，布)')
    while my_choices not in computer_choice:
        print('输入错误，请重新出拳')
        my_choices = input('请输入我们的出拳类型(石头，剪刀，布)')

    print('双方亮拳-------->')
    print('电脑的出拳：{}'.format(computers))
    print('我的出拳：{}'.format(my_choices))
    show_result(computers,my_choices)



#显示胜负
def show_result(computers,my_choices):
    if computers==my_choices:
        print('打平了')
    #当电脑猜拳的位置 如果是我猜拳的位置-1 都是胜利
    elif computers==computer_choice[computer_choice.index(my_choices)-1]:
        print('你赢了')
    else:
        print('你输了')




show_quan()