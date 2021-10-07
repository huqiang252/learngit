# -*- coding: utf-8 -*-
import requests
r=requests.get(url='http://www.c0ks.com')
#Response.history 是一个 Response 对象的列表，
# 为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序
print(r.history)
print(r.url)
print(r.status_code)