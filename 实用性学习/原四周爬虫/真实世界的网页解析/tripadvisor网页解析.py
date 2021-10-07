# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url='https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

web_data=requests.get(url)
soup=BeautifulSoup(web_data.text,'lxml')
# print(soup)

titles=soup.select('#taplc_attraction_coverpage_attraction_0 > div > div> div > div > div.shelf_item_container.shelfItemsWithGrayBgWrapper > div> div.poi > div > div.item.name > a')
print(titles)