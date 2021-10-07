# -*- coding: utf-8 -*-
import os,filecmp
path='./problem3_files/'
dir_files=os.listdir(path)
# answer=filecmp.cmp(file1_path,file2_path,shallow=True)
all_files=[] #存储所有文件路径
resf_files=[]#存储有重复的文件路径
#获取所有文件名称到all_files列表中
def allfile():
    for dir_f in dir_files:
        dir_f_path='./problem3_files/'+dir_f
        files=os.listdir(dir_f_path)
        for f in files:
            f_path=dir_f_path + '/' + f
            all_files.append(f_path)
    return all_files


def cmp_value(lists):
    i = 0
    for f in lists[:-1]:
        for j in lists[i + 1:]:
            if filecmp.cmp(f, j, shallow=True):
                if not (j in resf_files):
                    #如果j不在删除列表中就加入，防止重复
                    resf_files.append(j)
        i = i + 1
    return resf_files

all_files=allfile()
print(all_files)
resf_files=cmp_value(all_files)
print(resf_files)
#删除对应路径的重复文件
for rf_path in resf_files:
    os.remove(rf_path)
