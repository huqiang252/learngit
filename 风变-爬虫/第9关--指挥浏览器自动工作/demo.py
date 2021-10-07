# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver_obj=webdriver.Chrome()

url='https://localprod.pandateacher.com/python-manuscript/hello-spiderman/'
driver_obj.get(url)
time.sleep(2) #等待2秒
pageSourse=driver_obj.page_source  #获取网页源代码（渲染完整的）
print(type(pageSourse)) #类型为str
print(pageSourse)

print('--------------------------------------------------------')
labels = driver_obj.find_elements_by_tag_name('label') # 根据类名找到元素

print(labels)
print(type(labels)) # 打印label的数据类型

for label in labels:
    print(label.text) #获取每一个label标签的文本




driver_obj.close() # 关闭浏览器


