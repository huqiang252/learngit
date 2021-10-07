# -*- coding: utf-8 -*-
import random
player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
enemy_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】']
players = random.sample(player_list, 3)
enemies = random.sample(enemy_list, 3)
player_info = {}
enemy_info = {}

order_dict = {}
# 新建字典，存储顺序
def order_role():
    for i in range(3):
        global players
        order = int(input('你想将 %s 放在第几个上场？(输入数字1~3)' % players[i]))
        order_dict[order] = players[i]

    players = []
    for i in range(1, 4):
        players.append(order_dict[i])

    print('\n我方角色的出场顺序是：%s、%s、%s' % (players[0], players[1], players[2]))
