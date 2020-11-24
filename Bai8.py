import smtplib
import config
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.email_address, config.password)
        message = 'subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.email_address, config.email_address, message)
        server.quit()
        print("Đã gửi thành công: ")
    except:
        print('Gửi thất bại. ')
subject = 'Test code'
msg ='DEEP WEB-BIG DATA'
send_email(subject, msg)
