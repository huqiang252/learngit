# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers={"Cache-Control":"must-revalidate, no-cache, private",
"Connection":"keep-alive",
"Content-Encoding":"br",
"Content-Type":"text/html; charset=utf-8",
"Date":"Wed, 11 Dec 2019 08:55:57 GMT",
"Expires":"Sun, 1 Jan 2006 01:00:00 GMT",
"Keep-Alive":"timeout=30",
"Pragma":"no-cache",
"Server":"dae",
"Transfer-Encoding":"chunked",
"Vary":"Accept-Encoding",
"Vary":"Accept-Encoding",
"X-Content-Type-Options":"nosniff",
"X-DAE-App":"movie",
"X-DAE-Instance":"default",
"X-Douban-Mobileapp":"0",
"X-Xss-Protection":"1; mode=bloc"}
for x in range(1):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    url='https://movie.douban.com/top250?start=25&filter='
    res = requests.get(url,headers=headers)
    print(res.status_code) #报418 反爬虫了
    bs = BeautifulSoup(res.text, 'html.parser')
    bsf = bs.find('ol', class_="grid_view")
    print(bsf.find_all('li'))
    for titles in bsf.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)