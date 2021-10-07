# -*- coding: utf-8 -*-
from gevent import  monkey
monkey.patch_all()

import gevent,requests,time
from gevent.queue import Queue

work=Queue()

url_list= ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

for url in url_list:
    work.put_nowait(url)

def out_nowait():
    while not work.empty():
        url=work.get_nowait()
        r=requests.get(url)
        print(url,r.status_code,work.qsize())

tasklist=[]

for i in range(2):
    task=gevent.spawn(out_nowait)
    tasklist.append(task)

gevent.joinall(tasklist)