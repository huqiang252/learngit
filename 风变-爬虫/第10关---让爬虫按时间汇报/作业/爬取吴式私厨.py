# -*- coding: utf-8 -*-
import requests
from bs4 import  BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule,time
def cookbook():
    '''本周最受欢迎菜谱'''
    url = 'http://www.xiachufang.com/explore/'
    res = requests.get(url)
    connect = res.text
    bs_obj = BeautifulSoup(connect, 'html.parser')
    foodlists = []
    items_all = bs_obj.find_all(class_="info pure-u")
    for item_all in items_all:
        foodname = item_all.find(
            class_='name').text.strip()  # 上层标签可以获取到下层标签所有的内容Text
        foodurl = 'http://www.xiachufang.com' + \
                  item_all.find(class_='name').find('a')['href']
        materials = item_all.find(class_='ing ellipsis').text.strip()
        foodlists.append([foodname, foodurl, materials])
    return foodlists

def send_mail(foodlists):
    '''发送邮件'''
    # 定义变量
    from_addr = '275442825@qq.com'  # 发件人
    password = 'bdkeczjibpxobjda'  # 授权码
    to_addr = '656498993@qq.com'  # 收件人
    # 2649230013
    # 656498993

    smtp_server = 'smtp.qq.com'  # 发信服务器
    text=''
    for foodlist in foodlists:
        foodname=foodlist[0]
        foodurl=foodlist[1]
        materials=foodlist[2]
        text = text+foodname +'\n'+ foodurl +"\n"+ materials+'\n\n'

    msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header('胡强哥哥')
    msg['To'] = Header('小可爱')
    msg['Subject'] = Header('本周最受欢迎菜谱')

    # 使用的方法
    server = smtplib.SMTP()
    server.connect(smtp_server, 25)
    server.login(from_addr, password)
    try:
        server.sendmail(from_addr, to_addr, msg.as_string())
        print('恭喜发送成功')
    except:
        print('发送失败,请重试')
    # 关闭服务器
    server.quit()

def job():
    print('开始一次任务')
    foodlists=cookbook()
    print(foodlists)
    send_mail(foodlists)
    print('任务完成')

schedule.every(5).seconds.do(job)  #每10秒执行一次Job函数
# schedule.every().day.at("07:30").do(job) #每天执行

while True:
    schedule.run_pending()
    time.sleep(1)
