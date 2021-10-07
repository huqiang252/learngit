# coding:utf-8
# build space -> choose space -> switch space
# How we start OOP ? -> space

'''
folder

choose = input()
if choose == workspace.name:
    workspace.switch()

'''
import os
from sconfig import CONFIGS
import win32gui
import win32api
import win32con
# 如果win32包引入有问题，可以忽略，不影响程序运行
# 如果运行报错，可以尝试下载对应的库
# https://sourceforge.net/projects/pywin32/postdownload?source=dlp

class WorkSpace:

    def __init__(self, c):
        self.folders = c['folders']
        self.name    = c['name']
        self.target  = c['target']
        # 添加两个新的字段
        self.wallpaper = c['wallpaper']
        self.softwares = c['softwares']

    def switch(self):
        for f in os.listdir(self.target):
            # xxx.wspc
            if f.endswith('.wspc'):
                path = self.target + f
                os.remove(path)
        # mklink
        # 以下部分是 Windows 系统的写法，其他代码一致。
        # 另外由于 windows 系统运行 MKLINK 需要管理员权限，
        # 推荐使用 cmder 运行 http://www.jeffjade.com/2016/01/13/2016-01-13-windows-software-cmder/，
        # 或者用管理员身份打开cmd，然后运行python script_lesson_7.py.
        # Step1：根据CONFIG中的内容，创建系统软链接
        for source in self.folders:
            real_target = self.target + source.split('/')[-1] + '.wspc'
            command = ['MKLINK','/D', '"'+real_target+'"', '"'+source+'"']
            print(' '.join(command))
            # WINDOWS下使用os.system
            os.system(' '.join(command))

        # Step2：根据CONFIG中的内容，配置壁纸
        self.change_wallpaper(self.wallpaper)

        # Step3：根据CONFIG中的内容，打开指定软件
        for software in self.softwares:
            self.open_software(software)

    # Windows下自动打开软件
    def open_software(self, software):
        os.startfile(software)

    # Windows下自动切换壁纸
    def change_wallpaper(self, wallpaper):
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
            "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        # 拉伸适应桌面
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        # 桌面居中
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, wallpaper, 1+2)



workspaces = [WorkSpace(c) for c in CONFIGS]
choice = input('Choose your workspace:')
for w in workspaces:
    if w.name == choice:
        w.switch()
