import unidecode
import smtplib
import time
from Functions.talker import talk
from Functions.listener import listen
import subprocess


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
    cmd = ['hostname']
    shell_cmd = subprocess.run((cmd), capture_output=True, text=True)
    hostname = (shell_cmd.stdout).rstrip()

    if hostname == "ALEXANDER":  # Computadora Alexander
        archivo = "Files/emailsAlex.txt"
    else: #Computadora Leo
        archivo = "Files/emailsLeo.txt"

    email_sender = 'leo.andrade.la1@gmail.com'
    password = '10191999'

    # Viendo destinario en el diccionario
    nameDictionary = takeEmailReciver(nameAV, engine).lower()
    print(nameDictionary)
    
    with open(archivo) as emails:
        for linea in emails:
            linea = linea.split(': ')
            if linea[0] in nameDictionary:
                email_reciver = linea[1]
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
    server.login(email_sender,password)

    server.sendmail(email_sender, email_reciver, message)
    server.quit()

    talk(f'Correo enviado con exito', engine)
    print("Correo enviado exito")
