# -*- coding: utf-8 -*-
import requests
import webbrowser
import time

api = 'https://api.github.com/repos/channelcat/sanic'
web_page = "https://github.com/channelcat/sanic"
last_update = None

while True:
    all_info = requests.get(api).json()
    cur_update = all_info['updated_at']

    if not last_update:
        last_update = cur_update
        print(cur_update)

    if last_update < cur_update:
        webbrowser.open(web_page)
        last_update = cur_update
        time.sleep(600)