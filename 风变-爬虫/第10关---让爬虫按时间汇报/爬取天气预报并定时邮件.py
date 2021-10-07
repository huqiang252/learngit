# -*- coding: utf-8 -*-
import requests
from bs4 import  BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule,time
def weather_spider():
    '''获取今天的天气状况'''
    url='http://www.weather.com.cn/weather/101280601.shtml'

    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    res=requests.get(url=url,headers=headers)
    res.encoding='utf-8'
    bs=BeautifulSoup(res.text,'html.parser')
    tem1 = bs.find(class_='tem')
    weather1=bs.find(class_='wea')
    tem=tem1.text
    weather=weather1.text
    return tem,weather


def send_mail(tem,wather):
    '''发送邮件'''
    # 定义变量
    from_addr = '275442825@qq.com'  # 发件人
    password = 'bdkeczjibpxobjda'  # 授权码
    to_addr = '656498993@qq.com'  # 收件人
    # 2649230013
    # 656498993

    smtp_server = 'smtp.qq.com'  # 发信服务器
    text =tem+wather
    msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header('胡强哥哥')
    msg['To'] = Header('小可爱')
    msg['Subject'] = Header('今日天气预报')

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
    tem,weather=weather_spider()
    send_mail(tem,weather)
    print('任务完成')

schedule.every(30).seconds.do(job)  #每10秒执行一次Job函数
# schedule.every().day.at("07:30").do(job) #每天执行

while True:
    schedule.run_pending()
    time.sleep(1)