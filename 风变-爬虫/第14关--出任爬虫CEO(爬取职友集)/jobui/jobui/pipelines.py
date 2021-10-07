# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt

class JobuiPipeline(object):
    def __init__(self):
        # 初始化函数 当类实例化时这个方法会自启动
        self.book=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.book.add_sheet('Sheet')
        self.valuelist=[['公司', '职位', '地址', '招聘信息']]


    def process_item(self, item, spider):
        # process_item是默认的处理item的方法，就像parse是默认处理response的方法
        self.valuelist.append([item['company'], item['position'], item['address'], item['detail']])
        return item
        # 将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度

    def close_spider(self, spider):
        # close_spider是当爬虫结束运行时，这个方法就会执行
        # 写入表格
        for i in range(len(self.valuelist)):
            for j in range(len(self.valuelist[i])):
                self.sheet.write(i, j, self.valuelist[i][j])
        self.book.save(r'C:\Users\huqiang252\Desktop\招聘信息.xlsx')


