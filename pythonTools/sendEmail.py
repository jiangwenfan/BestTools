#主要功能是发送邮件。 目的：开机就发送邮件。 py3
#C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 
#自己把自己添加到启动文件夹中，只针对于win7
#发送gmail邮箱有2分钟延迟
import smtplib
from email.header import Header
from email.mime.text import MIMEText
 

mail_host = "smtp.126.com"      
mail_user = "zhan2103208467@126.com"                  # 用户名
mail_pass = "beida660xiaofan"               # 授权密码
 
sender = 'zhan2103208467@126.com'    # 发件人邮箱(最好写全, 不然会失败)
receivers = ['technology198964@gmail.com'] 
 
content = '机房电脑已经正常启动。。。'
title = 'test2程序自动发送。。'  
 
def sendEmail():
 
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
 
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
 
    email_client.quit()
 
if __name__ == '__main__':
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
