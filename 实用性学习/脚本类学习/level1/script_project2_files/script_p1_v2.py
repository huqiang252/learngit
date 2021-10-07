import shutil
import os

path = './'   #由于这里是相对路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
files = os.listdir(path)

for f in files:
    # f.png
    #./png
    folder_name = './' + f.split('.')[-1]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)


