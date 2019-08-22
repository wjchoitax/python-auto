PASS = 'tnsrhsl30'





import smtplib
from email.mime.text import MIMEText

msg = MIMEText('본문입니다.')
msg['Subject'] = '제목입니다.'

smtp = smtplib.SMTP(host='smtp.naver.com', port=587)
smtp.ehlo()
smtp.starttls()
smtp.login(user='ssgoni', password=PASS)
smtp.sendmail('ssgoni@naver.com', ['soongon@gmail.com'], msg.as_string())
smtp.close()
print('mail sended..')










