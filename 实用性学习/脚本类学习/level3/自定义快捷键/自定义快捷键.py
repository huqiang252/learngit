# -*- coding: utf-8 -*-
#- 按快捷键“gh”跳转到 https://github.com/
# - 按快捷键“wk”跳转到 https://www.wikipedia.org/


from pynput.keyboard import Listener
import time
import threading
import webbrowser

class ComboListener:
    def __init__(self):
        self.cur_keys = []
        self._run() #做一些必须要运行的函数
        self.keymap={
            'gh' :'https://github.com/',
            'wk' :'https://www.wikipedia.org/'

        }

    def _on_press(self,key):
        try:
            self.cur_keys.append(key.char)
        except AttributeError:
            self.cur_keys.append(key.name)

    def _cleaner(self):
        '''实现对cur_keys 的 1秒清理一次'''
        while True:
            time.sleep(0.7)
            self.cur_keys.clear()  #清空


    def _run(self):
        '''监听的线程'''
        l = Listener(on_press=self._on_press)
        l.daemon = True  #为了不卡主线程
        l.start()
        #两个线程
        t = threading.Thread(target=self._cleaner)
        t.daemon=True
        t.start()

    # aaa bbb
    def get_combo(self):
        if len(self.cur_keys)>=2:
            combo=self.cur_keys[-2:]
            return combo

    def get_parsed_combo(self):
        '''解析combo'''
        combo=self.get_combo()
        #[a,b,c]]
        if combo:
            key = ''.join(combo)
            if key in self.keymap.keys():
                webbrowser.open_new_tab(self.keymap[key])
                print("URL has been opened. {}".format(self.keymap[key]))
                self.cur_keys.clear()  #当URL成功开启后，清空cur_keys，防止因程序运行过快而打开多个同样的页面


cl = ComboListener()
while True:
    print('开始了')
    cl.get_parsed_combo()




