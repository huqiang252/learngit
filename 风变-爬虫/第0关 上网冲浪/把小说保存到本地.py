# -*- coding: utf-8 -*-
import requests

url='https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md'

res=requests.get(url)

novel=res.text

with open('《三国演义》.txt','a+',encoding='utf-8') as f_obj:
    f_obj.write(novel)
