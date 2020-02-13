import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# smtpserver = 'smtp.qq.com'
# # 发送邮箱用户/密码
# from_addr = '154759124@qq.com'
# password = 'wqmhgyxjwzfabhid'
# to_addr = 'jack_czm@vip.sina.com'
#
# msg = MIMEText('你好,我是xxx', 'plain', 'utf-8')
# msg['From'] = formataddr(['TSB Failure Module', from_addr])
# # msg['To'] = formataddr(['收件人昵称', to_addr])
# msg['Subject'] = '来自SMTP的问候'
#
# print(msg)
#
# server = smtplib.SMTP_SSL(smtpserver, 465)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()


class SendEmail:
    def __init__(self):
        # 发送邮箱服务器
        self.smtpserver = 'smtp.qq.com'
        # 发送邮箱用户/密码
        self.from_addr = '154759124@qq.com'
        self.password = 'wqmhgyxjwzfabhid'
        self.to_addr = 'jack_czm@vip.sina.com'

    def send_email(self,  text):
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(['TSB Failure Module', self.from_addr])
        # msg['To'] = formataddr(['收件人昵称', to_addr])
        msg['Subject'] = '来自SMTP的问候'
        server = smtplib.SMTP_SSL(self.smtpserver, 465)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        server.quit()

e_mail = SendEmail()
# e.send_email('jack_czm@vip.sina.com', '23424',)


import schedule
import time
#引入schedule和time模块
def job():
    e_mail.send_email('324324')
#定义一个叫job的函数，函数的功能是打印'I'm working...'
schedule.every(10).seconds.do(job)        #每2s执行一次job()函数

while True:
    schedule.run_pending()
    time.sleep(1)