import random
# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建3个子类，可实例化为3个不同的职业

class Knight(Role):
    def __init__(self, name='【圣光骑士】'):  # 把子类角色名作为默认参数
        Role.__init__(self, name)  # 利用了父类的初始化函数
        self.life = self.life * 5  # 骑士有5份血量
        self.attack = self.attack * 3  # 骑士有3份攻击力

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【暗影刺客】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【圣光骑士】对 『%s』【暗影刺客】说：“让无尽光芒制裁你的堕落！”' % (str1, str2))


class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【精灵弩手】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【暗影刺客】对 『%s』【精灵弩手】说：“主动找死，就别怪我心狠手辣。”' % (str1, str2))


class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【圣光骑士】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【精灵弩手】对 『%s』【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”' % (str1, str2))



class Game():
    def __init__(self):
        self.players=[]
        self.enemies=[]
        self.born_role()
        self.cooperat_role(self.players)
        self.cooperat_role(self.enemies)


    def born_role(self):
        self.players.append(Knight())
        self.players.append(Assassin())
        self.players.append(Bowman())

        self.enemies.append(Knight())
        self.enemies.append(Knight())
        self.enemies.append(Knight())

    def cooperat_role(self,man):
        self.man=man
        flag = (isinstance(self.man[0], type(self.man[1]))) and (
            isinstance(self.man[0], type(self.man[2])))
        flag2 = (isinstance(self.man[0], type(self.man[1]))) or (
            isinstance(self.man[0], type(self.man[2]))) or (
                    isinstance(self.man[1], type(self.man[2])))
        if flag:
            for i in self.man:
                i.life = i.life * 1.25
        if flag2==False:
            for i in self.man:
                i.attack = i.attack * 1.25


game=Game()
for i in game.players:
    print(i,i.life,i.attack)
print('----------------------')
for j in game.enemies:
    print(j,j.life,j.attack)


#都是真的(都一样为True)
# flag=(isinstance(game.players[0],type(game.players[1]))) and (isinstance(game.players[0],type(game.players[2])))
# print(flag)
# #当生成角色都属于某个角色类型，会抱团起来，血量增加25%；
# for i in game.players:
#     i.life=i.life*1.25
#

#
# #都是假的(都不一样为Flase)
# flag2=(isinstance(game.players[0],type(game.players[1]))) or (isinstance(game.players[0],type(game.players[2]))) or (isinstance(game.players[1],type(game.players[2])))
# print(flag2)
# #我们都不一样：当角色的角色类型都不一样，则会互相配合，攻击增加25%
# for i in game.players:
#     i.attack=i.attack*1.25


