# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart

#定义变量
from_addr = '275442825@qq.com' #发件人
password='bdkeczjibpxobjda'  #授权码
to_addr = '2649230013@qq.com'  #收件人

smtp_server='smtp.qq.com'  #发信服务器
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg=MIMEText(text,'plain','utf-8')


# 邮件头信息
msg['From'] = Header('胡强哥哥')
msg['To'] = Header('小可爱')
msg['Subject'] = Header('来自胡强nisha 的问候')


#使用的方法
server=smtplib.SMTP()
server.connect(smtp_server,25)
server.login(from_addr,password)
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('恭喜发送成功')
except:
    print('发送失败,请重试')
#关闭服务器
server.quit()


