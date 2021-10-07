# -*- coding: utf-8 -*-
#扫描存在zip数据-----对这些数据进行解压-----删除压缩文件
#按照 面向过程的思路进行编程
import os,shutil,time
path='C:/Users/huqiang252/Desktop'

def scan_file():
    files=os.listdir(path)
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    file_name=f.split('.')[0]
    file_path='C:/Users/huqiang252/Desktop/'+file_name
    print(file_path)
    os.makedirs(file_path)
    f_path='C:/Users/huqiang252/Desktop/'+f
    shutil.unpack_archive(f_path,file_path)

def delete(f):
    f_path='C:/Users/huqiang252/Desktop/'+f
    os.remove(f_path)
    time.sleep(2)

while True:
    zip_file=scan_file()
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)
        time.sleep(2.5)











