# -*- coding: utf-8 -*-
import requests
url='https://www.baidu.com/'
res=requests.get(url)

#返回cookiejar对象
cookiejar_obj=res.cookies
print(cookiejar_obj)
print(type(cookiejar_obj))

print('----------------------------------')

#将cookiejar对象转换位字典
cookiejar_dic=requests.utils.dict_from_cookiejar(cookiejar_obj)
print(cookiejar_dic)
print(type(cookiejar_dic))


