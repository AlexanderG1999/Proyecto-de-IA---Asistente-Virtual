import requests


bandera = True

while (bandera):
    send = input("Digite el mensaje a enviar: ")
    id = "-789572855" #Grupo a enviar
    token = "5048292664:AAFGCADK6IuFccuu5USne6vgZ8YGJpvtMsk" # Token BOT
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    params = {
        'chat_id': id,
        'text': send
    }

    requests.post(url, params = params)
    con = input("Presione x SALIR y c CONTINUAR: ")

    if con == 'x':
        bandera = False

