# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all() #开始线程运行
import requests
from bs4 import BeautifulSoup
import gevent
from gevent.queue import Queue
import xlwt

#构造网址
url_index='http://www.boohee.com/food/'
url_list=[]

#生成前10个类型的网址
for i in range(1,11):
    for j in range(1,4):
        #拼接出URL
        group_url=url_index+'group/'+str(i)+"?"+'page='+str(j)
        url_list.append(group_url)
#生成第11个类型的网址
for x in range(1,4):
    menu_url=url_index+'view_menu?page='+str(x)
    url_list.append(menu_url)

print(url_list)

work=Queue() #队列对象
for url in url_list:
    work.put_nowait(url)  #放入队列中



headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

valuelist=[['食物名称','食物详情链接','食物相关热量']]

def get_food():
    '''定义函数来获取food中部分值'''
    while not work.empty():
        url=work.get_nowait() #从队列中获取对应url
        r=requests.get(url,headers=headers)
        bs=BeautifulSoup(r.text,'html.parser')
        foods=bs.find_all(class_='item clearfix')
        for food in foods:
            foodv=food.find(class_='text-box pull-left')
            food_info=foodv.find('h4').text #食物介绍
            v_href=foodv.find('h4').find('a')['href']
            food_href='http://www.boohee.com'+v_href
            food_hot=foodv.find('p').text
            valuelist.append([food_info,food_href,food_hot])
            print(url,work.qsize())  #观察线程爬取的URL
            # print(valuelist)
            print('\n\n\n')


task_list=[] #要执行的任务队列
for x in range(5):
    task=gevent.spawn(get_food) #将函数当作任务执行
    task_list.append(task)

gevent.joinall(task_list)  #执行任务

book=xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('Sheet1')

for i in range(len(valuelist)):
    for j in range(len(valuelist[i])):
        sheet.write(i,j,valuelist[i][j])

book.save(r'C:\Users\huqiang252\Desktop\食物热量数据分析.xlsx')



