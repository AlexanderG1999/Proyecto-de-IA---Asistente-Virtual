import smtplib
from Functions.Talker import talk

email_sender = 'leo.andrade.la1@gmail.com'
message = "Hola, un mensaje desde Python!\n ya valio papu, mi IA envia correos"
subject = "Prueba de correo"
message = 'Subject: {}\n\n{}'.format(subject,message)

def sendMail(email_reciver, engine):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_sender,'10191999')

    server.sendmail(email_sender,email_reciver, message)
    server.quit()

    talk(f'Correo enviado con exito', engine)
    print("Correo enviado exito")
