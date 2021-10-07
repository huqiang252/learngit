# -*- coding: utf-8 -*-
# 什么是异常
# 如何预测异常  ----针对不可抗力（如网路环境差）
import csv
from wxpy import *
import time


def read_info():
    f = open('./sample.csv','r',encoding='utf-8')
    reader = csv.DictReader(f)
    return [info for info in reader]#[{},{},{}]

    #'xx-同学请于 xx 时间参加 xx 课程，课程地址是 xxx。收到请回复，谢谢'
def make_msg(raw_info):
    t = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢!'
    return [t.format(n=info['姓名'],
                     t=info['上课时间'],
                     s=info['课程'],
                     a=info['上课地址']
                     ) for info in raw_info]
    # -> list ['xxx','xxx']

def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('-')[0]
        f = bot.friends().search(fren_name) # list
        if len(f) == 1:
            try:
                f[0].send(msg)
            except :
                print('Stop at:')  #告诉在什么号码的时候出现异常！
                print(msg)
        else:
            print(fren_name)
            print('Please check this name')
    time.sleep(3)

# bot -> bot.find_fren() -> bot.send()
# f = bot.friend().search('name')
# f.send('msg')

raw_info = read_info()
msg_list = make_msg(raw_info)
send(msg_list)