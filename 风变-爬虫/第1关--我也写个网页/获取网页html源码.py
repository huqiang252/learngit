# -*- coding: utf-8 -*-
import requests
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res=requests.get(url)

connect=res.text

with open('这个书苑不太冷.txt','a+',encoding='utf-8') as f_obj:
    f_obj.write(connect)