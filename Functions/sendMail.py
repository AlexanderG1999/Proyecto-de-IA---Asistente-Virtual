import smtplib

email_sender = 'leo.andrade.la1@gmail.com'
email_reciver = ''
message = "Hola, un mensaje desde Python!\n ya valio papu, mi IA envia correos"
subject = "Prueba de correo"
message = 'Subject: {}\n\n{}'.format(subject,message)

def sendMail(email_reciver):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_sender,'10191999')

    server.sendmail(email_sender,email_reciver, message)
    server.quit()

    print("Correo enviado exito")

sendMail()