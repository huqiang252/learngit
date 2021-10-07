# -*- coding: utf-8 -*-


order_dict = {}
players=['A','B','C']
enemies=['A','B','C']
orderlist=[]

def pandshuzhi():
    while True:
        try:
            order = int(
                input('你想将 %s 放在第几个上场？(输入数字1~3)' % players[i]))

            if order not in [1,2,3]:
                print('请输入123中的数字')
            elif order in orderlist:
                # 判断在列表
                print('你输入的数据有重复')
            else:
                orderlist.append(order)
                break
        except ValueError:
            print('请输入数字')
            continue
    return order


for i in range(3):
    order = pandshuzhi()
    order_dict[order] = players[i]


players = []
for i in range(1, 4):
    players.append(order_dict[i])
print('\n你的队伍出场顺序是：%s、%s、%s'
      % (
     players[0], players[1], players[2]))
print('敌人队伍出场顺序是：%s、%s、%s'
      % (
      enemies[0], enemies[1], enemies[2]))
