# -*- coding: utf-8 -*-
import requests

url='https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md'

res=requests.get(url)

print(type(res))
print(res.status_code)
