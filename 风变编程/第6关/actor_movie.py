# -*- coding: utf-8 -*-
movies = {'妖猫传':['黄轩','染谷将太'],
         '后会无期':['冯绍峰','陈柏霖','钟汉良','王珞丹'],
         '大上海':['周润发','黄晓明','洪金宝'],
         '我想和你好好的':['冯绍峰','倪妮']
         }

while True:
    print('需要输入一个演员名称来获取其演过的电影，输入q后退出')
    actorName=input('请输入演员名称：')
    if  actorName=='q':
        break
    for movie in movies:
        #获取这个电影的主演人员
        actorNames=movies[movie]
        if actorName in actorNames:
            print(actorName+'出演了电影'+movie)
