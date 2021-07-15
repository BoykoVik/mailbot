import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from settings import SENDERS, TITLES, ONE_MAIL_MATCH, FILES_IMG, TIME_RAGE
from time import sleep

f = open('list.txt')
list_emails = []
quant_mails = 0
for line in f:
    if '@' in line:
        list_emails.append(line)
        quant_mails += 1

quant_senders = len(SENDERS)

print('Максимальное число писем = ' + str(quant_senders * ONE_MAIL_MATCH) + ' из ' + str(quant_mails))
ans = input('продолжаем? да/нет: \n')
if ans == 'да':

    current_sender = 0 # счетчик отправителей
    current_title = 0 # счетчик заголовков
    current_img = 0 # счетчик изображений

    err_much = 0 # счетчик ошибок
    good_much = 0 # счетчик отправленных

    for mail_to in list_emails:
        try:
            strFrom = SENDERS[current_sender][0] #отправитель
            pwd = SENDERS[current_sender][1]# пароль отправителя

            # Создание письма
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = TITLES[current_title] # задание заголовка
            msgRoot['From'] = strFrom # задание отправителя
            msgRoot['To'] = mail_to # задание получателя

            msgRoot.preamble = 'Multi-part message in MIME format.'
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
            msgText = MIMEText('Alternative plain text message.')
            msgAlternative.attach(msgText)

            msgText = MIMEText('<img src="cid:image1">', 'html') #<b>Тут <i>может</i> быть любой текст.</b><br>
            msgAlternative.attach(msgText)

            #загрузка изображения
            fp = open(FILES_IMG[current_img], 'rb') #открыл изображение
            msgImage = MIMEImage(fp.read())#считал
            fp.close()#закрыл

            # Создание ID соответствия
            msgImage.add_header('Content-ID', '<image1>')
            msgRoot.attach(msgImage)# добавление в месседж

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(strFrom, pwd)
            server.sendmail(strFrom, mail_to, msgRoot.as_string())
            server.quit()
            good_much += 1
            print(str(good_much) + ' отправлено на адрес ' + mail_to + ' с адреса ' + strFrom)
        except:
            err_much += 1
            print('НЕ отправлено на адрес ' + mail_to)
            print('НЕ отправлено ВСЕГО ' + str(err_much))

        # Смена отправителя
        current_sender += 1
        if current_sender >= len(SENDERS):
            current_sender = 0
        # Смена заголовка
        current_title += 1
        if current_title >= len(TITLES):
            current_title = 0
        # Смена изображения
        current_img += 1
        if current_img >= len(FILES_IMG):
            current_img = 0

        sleep(TIME_RAGE)


else:
    print('отменено')

print('ОТПРАВЛЕНО ' + str(good_much) + ' писем')
print('ОШИБОК ' + str(err_much) + ' писем')
print('...................................')
