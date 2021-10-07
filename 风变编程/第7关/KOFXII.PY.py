# -*- coding: utf-8 -*-
#双人攻击类游戏
import time
import random

activity=True
while activity:
    print('欢迎来到moby游戏')
    n = 3
    # 玩家和敌人的胜利次数
    play_vectory = 0
    enemy_vectory = 0
    for i in range(n):
        # 随机玩家和敌人属性
        time.sleep(2)
        play_life = random.randint(100, 150)
        play_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)
        print('--------现在是第{}局-----------'.format(i+1))

        # print('【玩家】\n血量：%s\n攻击：%s' % (play_life, play_attack))
        print('【玩家】\n血量：{}\n攻击：{}'.format(play_life, play_attack))

        print('------------------------')  # 辅助功能，起到视觉分割的作用，让代码的运行结果更清晰
        time.sleep(1.5)
        # print('【敌人】\n 血量:%s\n攻击:%s' % (enemy_life, enemy_attack))
        print('【敌人】\n 血量:{}\n攻击:{}'.format (enemy_life, enemy_attack))
        print('------------------------')
        time.sleep(1.5)
        while enemy_life > 0 and play_life > 0:
            enemy_life = enemy_life - play_attack
            play_life = play_life - enemy_attack
            # print('你发起了攻击，【敌人】剩余血量:%s' % enemy_life)  # 人工计算敌人血量：100-50=50
            print('你发起了攻击，【敌人】剩余血量:{}'.format(enemy_life) )
            print('敌人向你发起了攻击，【玩家】剩余血量:{}'.format(play_life) )  # 人工计算玩家血量：100-30=70
            print('------------------------')
            time.sleep(1.5)
        else:
            if play_life > 0 and enemy_life <= 0:
                play_vectory += 1
                print('敌人死翘翘了，你赢了！')  # 打印结果
                continue
            elif enemy_life > 0 and play_life <= 0:
                enemy_vectory += 1
                print('悲催,敌人把你干掉了')
                continue
            else:
                print('打个平手')

    if play_vectory > enemy_vectory:
        print('最后最终结果：你赢了')
    elif play_vectory < enemy_vectory:
        print('你输了')
    else:
        print('平局')

    answer=input('3局已过是否重来一盘，选择重来一盘继续游戏，选择退出游戏退出:')
    if answer=='退出':
        print('游戏退出')
        activity=False





















