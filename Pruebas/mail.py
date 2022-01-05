import smtplib

def sendMessage():

    message = "Hola, un mensaje desde Python!\n ya valio papu, mi IA envia correos"
    subject = "Prueba de correo"

    message = 'Subject: {}\n\n{}'.format(subject,message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('leo.andrade.la1@gmail.com','10191999')

    server.sendmail('leo.andrade.la1@gmail.com','veronica99quesada@gmail.com', message)
    server.quit()

    print("Correo enviado exito")