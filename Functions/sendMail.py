import unidecode
import smtplib, time
from Functions.talker import talk
from Functions.listener import listen

emails = { # Archivos
    'alexander': 'alexanderguillin1999@gmail.com',
    'ricardo': 'ricardoerazoliga@gmail.com',
    'leonardo':'anais.leo.la@gmail.com',
    'cristian': 'cristianfantasma6666@gmail.com'
}

def takeEmailReciver(nameAV, engine):
    talk("¿Cuál es el nombre y apellido del destinario?", engine)
    listened_sender = listen(nameAV, engine)
    
    return listened_sender

def takeMessage(nameAV, engine):
    talk("¿Cuál es el mensaje a enviar?", engine)
    listened_message = listen(nameAV, engine)
    
    return listened_message

def takeSubject(nameAV, engine):
    talk("¿Cuál es el asunto del correo?", engine)
    listened_subject = listen(nameAV, engine)
    
    return listened_subject



def sendMail(nameAV, engine):
    email_sender = 'leo.andrade.la1@gmail.com'
    # Viendo destinario en el diccionario
    nameDictionary = takeEmailReciver(nameAV, engine).lower()
    print(nameDictionary)
    
    for mail in emails:
        if mail in nameDictionary:
            email_reciver = emails[mail]
    time.sleep(0.9)
    print(email_reciver)

    message = unidecode.unidecode(takeMessage(nameAV, engine)) # Quitando tildes
    time.sleep(0.9)
    subject = unidecode.unidecode(takeSubject(nameAV, engine)) # Quitando tildes
    time.sleep(0.9)

    message = 'Subject: {}\n\n{}'.format(subject, message)
    print(message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_sender,'10191999')

    server.sendmail(email_sender, email_reciver, message)
    server.quit()

    talk(f'Correo enviado con exito', engine)
    print("Correo enviado exito")
