# -*- coding: utf-8 -*-
import requests
session = requests.session()

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url_1 = 'https://ipassport.ele.me/newlogin/sms/send.do?appName=eleme&fromSite=-2'
tel = input('请输入手机号码：')
data_1 = {'captcha_hash':'',
        'captcha_value':'',
        'mobile':tel,
        'scf':''}

token = session.post(url_1, headers=headers, data=data_1).json()['validate_token']

url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
code = input('请输入手机验证码：')
data_2 = {'mobile':tel,
        'scf':'ms',
        'validate_code':code,
        'validate_token':token}

session.post(url_2,headers=headers,data=data_2)


address_url = 'https://www.ele.me/restapi/v2/pois?'
place = input('请输入你的收货地址：')
params = {'extras[]':'count','geohash':'ws105rz9smwm','keyword':place,'limit':'20','type':'nearby'}
# 这里使用了深圳的geohash

address_res = requests.get(address_url,params=params)
address_json = address_res.json()

print('以下，是与'+place+'相关的位置信息：\n')
n=0
for address in address_json:
    print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    n = n+1
address_num = int(input('请输入您选择位置的序号：'))
final_address = address_json[address_num]

restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants?'
# 使用带有餐馆列表的那个XHR地址。
params = {'extras[]':'activities',
'geohash':final_address['geohash'],
'latitude':final_address['latitude'],
'limit':'24',
'longitude':final_address['longitude'],
'offset':'0',
'terminal':'web'
}
# 将参数封装，其中geohash和经纬度，来自前面获取到的数据。
restaurants_res = session.get(restaurants_url,params=params)
# 发起请求，将响应的结果，赋值给restaurants_res
restaurants = restaurants_res.json()
# 把response对象，转为json。
for restaurant in restaurants:
# restsurants最外层是一个列表，它可被遍历。restaurant则是字典，里面包含了单个餐厅的所有信息。
    print(restaurant['name'])
