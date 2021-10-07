# -*- coding: utf-8 -*-
#拆解问题：读取csv文件；如何把对应的信息发送到微信（通过看文档学习一个从没来没有用过的库）
#学习新的东西，要测试其API
import csv,time
from wxpy import *
def read_info():
    with open('./Script_Day10/sample.csv','r',newline='') as f_obj:
        reader=csv.DictReader(f_obj)
        #不是代码逻辑复杂而是对视觉不优化
        return [info for info in reader]  #[{},{},{}] 列表表达式

def make_msg(row_info):
    t='{n}-同学请于{t}时间参照{s}课程，课程地址是{a}。收到请回复，谢谢！'
    #把row_info字典提炼组成新的模板放入列表中
    return [t.format(
        n=info['姓名'],
        t=info['上课时间'],
        s = info['课程'],
        a = info['上课地址']
    ) for info in row_info]

#发送微信消息
def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        frend_name=msg.split('-')[0]
        f=bot.friends().search(frend_name)
        if len(f)==1:
            f[0].send()
        else:
            print(frend_name)
            print('重复的名称')
    time.sleep(3)

row_info=read_info()
msg_list=make_msg(row_info)
send(msg_list)
