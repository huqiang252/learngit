# -*- coding: utf-8 -*-
import requests
import webbrowser as web
import time


chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
web.register('chrome',None,web.BackgroundBrowser(chromepath))

api='https://api.github.com/users/kennethreitz/starred'
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
new_id=[]
last_id_list=[45634074, 107100872, 11404587, 43336679, 208441172, 120538304, 40684033, 32555448, 110339095, 162761045, 95903923, 149144377, 47099511, 36897953, 30933195, 132507058, 43768227, 57192704, 185315628, 35955666, 23983011, 30325550, 90320494, 4344025, 51591133, 176576395, 62367558, 51270739]

while True:
    all_starred = requests.get(api, headers=headers).json()
    for starred in all_starred:
        if starred['id'] not in last_id_list:
            new_id.append(starred['id'])
            fullname = starred['full_name']
            print('https://github.com/'+fullname)
            web.get('chrome').open('https://github.com/'+fullname)
    last_id_list=last_id_list+new_id
    print(last_id_list)
    time.sleep(60)














