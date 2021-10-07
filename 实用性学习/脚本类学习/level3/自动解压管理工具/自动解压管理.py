# -*- coding: utf-8 -*-
import os,shutil,time
from zip_config import CONFIGS

class ZipManager:
    def __init__(self,c):
        self.folder_path=c['folder_path']
        self.name=c['name']

    def run(self):
        zip_file=self.scan_file()
        if zip_file:
            self.unzip_it(zip_file)
            if self.name=='DESKTOP':
                self.delete(zip_file)
            elif self.name=='DOWNLOAD':
                self.move(zip_file)



    def scan_file(self):
        '''扫描是否存在zip数据,返回压缩文件f'''
        files = os.listdir(self.folder_path)
        for f in files:
            if f.endswith('.zip'):
                return f

    def unzip_it(self,f):
        '''解压'''
        file_name = f.split('.')[0]
        file_path = self.folder_path + file_name
        print(file_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        f_path = self.folder_path + f
        shutil.unpack_archive(f_path, file_path)

    def delete(self,f):
        '''删除压缩文件'''
        f_path = self.folder_path + f
        os.remove(f_path)
        time.sleep(2)

    def move(self,f):
        '''移动压缩的文件夹到子文件夹package中'''
        f_path = self.folder_path + f
        new_file=self.folder_path+'package'  #存储压缩文件夹位置
        if not os.path.exists(new_file):
            os.makedirs(new_file)
        shutil.move(f_path,new_file)
        time.sleep(2)

zipmanagers=[ZipManager(c) for c in CONFIGS]
# downer=zipmanagers[1]
# f=downer.scan_file()
# downer.unzip_it(f)
# downer.move(f)

for zip in zipmanagers:
        zip.run()
