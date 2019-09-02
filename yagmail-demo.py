PASS = ''





import smtplib
from email.mime.text import MIMEText
from email.header import Header

unpaid_list = ['soongon@gmail.com', 'soongon@hucloud.co.kr']

smtp = smtplib.SMTP(host='smtp.naver.com', port=587)
smtp.ehlo()
smtp.starttls()
smtp.login(user='ssgoni', password=PASS)

for customer in unpaid_list:
    msg = MIMEText('본문입니다.')
    msg['Subject'] = Header('제목입니다.', charset='utf-8')
    msg['From'] = 'ssgoni@naver.com'
    msg['To'] = customer

    smtp.send_message(msg)

smtp.quit()
print('mail sended..')










