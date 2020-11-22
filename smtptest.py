# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
 
 
def send_mail():
    # 第三方 SMTP 服务
    mail_host="smtp.139.com"  #设置服务器
    mail_user="13145872950@139.com"    #用户名
    mail_pass="hejinshou123"   #口令 
    sender = '13145872950@139.com'
    receiver = '13145872950@139.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mail_body='message'
    message = MIMEText(mail_body, 'html', 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    me="xxxx"+'<'+sender+'>'
    message['From'] = me 
    he='yyy'+'<'+receiver+'>'
    message['To']=he
    
    smtpObj = smtplib.SMTP_SSL('smtp.139.com',465) 
    #smtpObj.connect()  
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receiver, message.as_string())
    print ("邮件发送成功")
	
send_mail()
	