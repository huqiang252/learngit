# -*- coding: utf-8 -*-
import requests
url='https://res.pandateacher.com/2018-12-18-10-43-07.png'
res=requests.get(url)

pic=res.content  #把返回对象以二进制形式返回
#二进制文件使用 wb 写入
with open('ppt.jpg','wb') as f_obj:
    f_obj.write(pic)