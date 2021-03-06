# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem
# 需要引用DoubanItem，它在items里面。因为是items在top250.py的上一级目录，所以要用..items，这是一个固定用法。


class DoubanSpider(scrapy.Spider):
    name = 'douban' #爬虫的名字
    allowed_domains = ['https://book.douban.com']  #域名
    start_urls = []  #存放所有需要爬取的url
    for x in range(3):
        url='https://book.douban.com/top250?start='+str(x*25)
        start_urls.append(url)

    def parse(self, response):
        '''parse是Scrapy里默认处理response的一个方法，中文是解析'''
        bs=BeautifulSoup(response.text,'html.parser')
        datas=bs.findall('tr',class_='item')
        # 用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        for data in datas:
            # 遍历data。
            item = DoubanItem()
            # 实例化DoubanItem这个类。
            item['title'] = data.find_all('a')[1]['title']
            # 提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['publish'] = data.find('p', class_='pl').text
            # 提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['score'] = data.find('span', class_='rating_nums').text
            # 提取出评分，并把这个数据放回DoubanItem类的score属性里。
            print(item['title'])
            # 打印书名。
            yield item
            # yield item是把获得的item传递给引擎。