import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

strFrom = 'gexar47@gmail.com'
strTo = 'gexar47@mail.ru'

# Create the root message 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Тут заголовок письма'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo

msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>Тут <i>может</i> быть</b> любой текст.<br><img src="cid:image1"><br>И тут может быть текст', 'html')
msgAlternative.attach(msgText)

#Attach Image 
fp = open('MMA-&-Box-new.jpg', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login('gexar47@gmail.com', 'nameless47ok')
server.sendmail(strFrom, strTo, msgRoot.as_string())
server.quit()