# -*- coding: utf-8 -*-
# 本地Chrome浏览器的静默默模式设置：让浏览器在后台运行
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行
url='https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html'

driver.get(url)
time.sleep(3)

#查看更多评论循环3次（看3页的数据）
for i in range(3):

    #定位查看更多
    show_all_comment=driver.find_element_by_class_name('comment__show_all').find_element_by_tag_name('a').find_element_by_tag_name('i')
    show_all_comment.click()


time.sleep(1)

#定位评论



comments=driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
print(len(comments))
for comment in comments:
    sweet=comment.find_element_by_tag_name('p')
    print('评论:'+sweet.text+'\n\n')



driver.close()