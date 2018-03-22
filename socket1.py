# import socket

# #AF_INET指定使用IPv4协议 SOCK_STREAM指定使用面向流的TCP协议
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# # 建立连接:
# s.connect(('www.sina.com.cn',80))

# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


# #接收数据
# buffer=[]
# while True:
# 	d=s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break

# data=b''.join(buffer)

# #关闭链接
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# from email.mime.text import MIMEText

# msg=MIMEText('hello,send by python...','plain','utf-8')

# from_addr='m13008366818@126.com'
# password=''

# to_addr='273494899@qq.com'
# smtp_server='smtp.126.com'

# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'm13008366818@126.com'
receivers = ['273494899@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP('smtp.126.com',25)
    smtpObj.login(sender,'')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功") 
except smtplib.SMTPException:
    print("Error: 无法发送邮件")