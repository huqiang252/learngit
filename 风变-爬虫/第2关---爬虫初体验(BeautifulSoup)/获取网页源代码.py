# -*- coding: utf-8 -*-
import requests #调用requests库
from bs4 import BeautifulSoup
url1='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
# url2='https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get(url1)
#获取网页源代码，得到的res是response对象
print(res.status_code) #检查请求是否正确响应
html = res.text #把res的内容以字符串的形式返回
soup=BeautifulSoup(html,'html.parser') #bs对象=BeautifulSoup(要解析的文本，'解析器')
# item=soup.find('div')
# print(type(item))
# print(item)
items=soup.find_all(class_='books')
for item in items:
    kind=item.find('h2')  #类型
    title=item.find(class_="title")  #书名
    brief=item.find(class_="info")  #简介
    print(kind.text,title.text,title['href'],brief.text)
    print('------------------------------------------')