# -*- coding: utf-8 -*-
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
    com_index=computer_choice.index(computers)
    my_index=computer_choice.index(my_choices)
    len_index=my_index-com_index

    print('双方亮拳-------->')
    print('电脑的出拳：{}'.format(computers))
    print('我的出拳：{}'.format(my_choices))
    show_result(len_index)



#显示胜负
def show_result(len_index):
    if len_index==0:
        print('打平了')
    elif len_index==1 or len_index== -2:
        print('你赢了')
    else:
        print('你输了')




show_quan()