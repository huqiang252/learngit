# -*- coding: utf-8 -*-
#创建以后缀命名的文件夹
#复合这个后缀的文件移动到该命名的文件夹中
import os,shutil
path='./'
files=os.listdir(path) #获取所有文件列表
for f in files:
    # 获取文件的后缀名
    filename=f.split('.')[-1]
    if  not (filename=='py'):
        filepath='./'+filename
        if not os.path.exists(filepath):
            os.makedirs(filepath)
            shutil.move(f,filepath)
        else:
            shutil.move(f,filepath)
