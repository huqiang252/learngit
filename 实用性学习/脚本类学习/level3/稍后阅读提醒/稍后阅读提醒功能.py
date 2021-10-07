# -*- coding: utf-8 -*-
'''
    实现逻辑:
    找到Url---find url----复杂的问题，url需要分类  chrome的插件=save as shortcut 采用windows *ulr类型保存格式
    核对时间---check time
    发送到浏览器----send to browser

    实例化对象：
    配置文件：c_config.py

    code如何实现：下一步思考：tool and context (如何在情景中设计工具）
    ---希望manager.run()-----通过使用的方式反推需要变量和数据（关键步骤）
'''
from c_config import CONFIGS
from time import ctime
import os,webbrowser
import threading

class ReadManager:
    def __init__(self,c):
        self.read_time=c['time']
        self.folder_path=c['folder_path']
        self.urls=self.urls_parse(self.folder_path)

    def urls_parse(self,path):
        '''解析文件夹里面的url'''
        urls = []
        for f in os.listdir(path):
            full_path=path+f
            with open(full_path,'r',encoding='utf-8') as raw_url:
                url = raw_url.read().split('URL=')[-1]
                print(url)
                urls.append(url)
        return urls

    def run(self):
        #使用多线程，怕卡死
        def _run():
            while True:
                if self.time_to_read():
                    self.send_to_browser()
        t=threading.Thread(target=_run())
        t.daemon = True
        t.start()

    def time_to_read(self):
        #返回一个 是否到达当前时间
        return self.read_time == ctime().split()[-2]

    def send_to_browser(self,urls):
        for url in urls:
            webbrowser.open_new_tab(url)

managers=[ReadManager(c) for c in CONFIGS]
for m in managers:
    m.send_to_browser(m.urls)
# for m in managers:
#     m.run()






