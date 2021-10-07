# -*- coding: utf-8 -*-
import os,shutil
image_list=['jpg','png','gif']
document_list=['doc','docx','md','ppt']
path='./'
files=os.listdir(path)
image_path='./image'
document_path='./document'
if not os.path.exists(image_path):
    os.makedirs(image_path)
if not os.path.exists(document_path):
    os.makedirs(document_path)
for f in files:
    if not ('.' in  f):
        f_path = './' + f
        f_files = os.listdir(f_path)
        if (f in image_list):
            for f1 in f_files:
                shutil.move(f_path+'/'+f1,image_path)
        if (f in document_list):
            for f2 in f_files:
                shutil.move(f_path+'/'+f2,document_path)

# 循环移动文件后，删除文件夹
for i in ['doc', 'docx', 'gif', 'jpg', 'md', 'png', 'ppt']:
    f_path = './' + i
    os.removedirs(f_path)



