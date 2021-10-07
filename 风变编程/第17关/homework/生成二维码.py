# -*- coding: utf-8 -*-
from MyQR import myqr
word='http://www.dgxt.com/'
img='谢育花.jpg'

myqr.run(
    words=word,
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture=img,  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='谢育花二维码.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )