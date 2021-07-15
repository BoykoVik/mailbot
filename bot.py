import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import email
import email.mime.application

from_email = 'gexar47@gmail.com'
password = 'nameless47ok'

msg = MIMEMultipart()
msg['Subject'] = 'Тут заголовок'
msg['From'] = from_email

to_email = 'gexar47@mail.ru'
message = 'Тут может быть сообщение'

msg.attach(MIMEText(message, 'plain'))

filename='list.jpeg'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="jpeg")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()

