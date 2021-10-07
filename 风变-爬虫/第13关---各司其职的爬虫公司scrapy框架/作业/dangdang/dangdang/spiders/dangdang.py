# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import DangdangItem

class DangdangSpiders(scrapy.Spider):
    name = 'dangdang'
    allowed_domains=['http://bang.dangdang.com']
    start_urls=[]
    for i in range(1,3):
        url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(i)
        start_urls.append(url)

    def parse(self, response):
        bs=BeautifulSoup(response.text,'html.parser')
        datas = bs.find('ul',
                        class_='bang_list clearfix bang_list_mode').find_all(
            'li')
        item=DangdangItem()

        for data in datas:
            item['book_name'] = data.find('div', class_='name').find('a')['title']

            item['book_publisher'] = \
            data.find('div', class_='publisher_info').find('a')['title']

            item['book_price'] = data.find('div', class_='price').find('span',
                                                               class_='price_n').text

            print(item['book_name'])
            yield item


