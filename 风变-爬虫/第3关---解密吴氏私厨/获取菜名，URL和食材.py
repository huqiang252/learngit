# -*- coding: utf-8 -*-
import requests
from bs4 import  BeautifulSoup

url='http://www.xiachufang.com/explore/'
res=requests.get(url)
connect=res.text
bs_obj=BeautifulSoup(connect,'html.parser')
foodlists=[]
items_all=bs_obj.find_all(class_="info pure-u")
for item_all in items_all:
    foodname=item_all.find(class_='name').text.strip() #上层标签可以获取到下层标签所有的内容Text
    foodurl='http://www.xiachufang.com'+item_all.find(class_='name').find('a')['href']
    materials=item_all.find(class_='ing ellipsis').text.strip()
    foodlists.append([foodname,foodurl,materials])
print(foodlists)

text = ''
for foodlist in foodlists:
    foodname = foodlist[0]
    foodurl = foodlist[1]
    materials = foodlist[2]
    text =text+ foodname + '\n' + foodurl + "\n" + materials + '\n\n'
print(text)

