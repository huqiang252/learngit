# -*- coding: utf-8 -*-
import requests,time
#导入requests和time
start = time.time()
# 记录程序开始时间
url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']
#把8个网站封装成列表

for url in url_list:

#遍历url_list
    r = requests.get(url)
    print(url,r.status_code,time.time()-start)
