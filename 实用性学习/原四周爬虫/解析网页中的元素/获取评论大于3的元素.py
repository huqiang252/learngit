# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(1)
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
body > div.main-content > ul > li:nth-child(1) > div.rate > span
'''
info=[]
with open('./web/new_index.html','r',encoding='utf-8') as wb_data:
    Soup=BeautifulSoup(wb_data,'lxml')
    images=Soup.select('body > div.main-content > ul > li > img')
    titles=Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs=Soup.select('body > div.main-content > ul > li> div.article-info > p.description')
    rates=Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates=Soup.select('body > div.main-content > ul > li> div.article-info > p.meta-info ')  #分类，多对一的结构只需要获取到父类
    # print(images,titles,descs,rates,cates,sep='\n--------\n')

for image,title,desc,rate,cate in zip(images,titles,descs,rates,cates):
    data={
        'title':title.get_text(),
        'desc':desc.get_text(),
        'rate':rate.get_text(),
        'cate':list(cate.stripped_strings),
        'img':image.get('src')
    }
    info.append(data)

for i in info:
    # if float(i['rate'])>3:
    #     print(i['title']+'---->',i['desc'])
    print(i)
