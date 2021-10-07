# -*- coding: utf-8 -*-
import os
path=r'C:\Users\huqiang252\Downloads\练习\files'
files=os.listdir(path)
for f in files:
    if (not f.endswith('.gif')) and ('project30' in f or 'commercial' in f):
        print('符合条件的：'+f)