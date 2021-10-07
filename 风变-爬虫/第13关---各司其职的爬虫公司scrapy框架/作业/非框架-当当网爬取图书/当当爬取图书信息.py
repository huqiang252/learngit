# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-1'
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
r=requests.get(url,headers=headers)
bs=BeautifulSoup(r.text,'html.parser')

datas=bs.find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
# print(datas)

for data in datas:
    book_name=data.find('div',class_='name').find('a')['title']
    book_publisher=data.find('div',class_='publisher_info').find('a')['title']
    book_price=data.find('div',class_='price').find('span',class_='price_n').text
    print(book_name)
    print(book_publisher)
    print(book_price)
    print('\n\n')





