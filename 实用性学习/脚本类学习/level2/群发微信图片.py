# -*- coding: utf-8 -*-
from wxpy import *
# 指定图片文件的路径
image_path = "./images/owl.jpg"  #这里替换成你的图片路径
# 初始化微信机器人
bot = Bot()
# 将要发送的好友的名字存到list中
friends = ['王总','麻瓜编程君','麻瓜编程OK姐']
# 定义用于群发操作的函数
def send_to_friends(friends):
    for friend in friends:
        # 搜素好友
        friend_search = bot.friends().search(friend)
        # 如果搜索结果仅有一个，则发送图片，否则返回错误信息
        if (len(friend_search) == 1):
            friend_search[0].send_image(image_path)
        else:
            print("发送失败！请检查用户名:"+friend)
# 调用函数
send_to_friends(friends)