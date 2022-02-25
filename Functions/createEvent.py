from datetime import datetime
from Functions.calendarSetup import get_calendar_service
from Functions.listener import listen
from Functions.talker import talk
import time

def take_event_title(nameAV, engine):
    talk("¿Cuál es el título del evento?", engine)
    listened_title = listen(nameAV, engine, 1)

    return listened_title

def take_event_desc(nameAV, engine):
    talk("¿Cuál es la descripción del evento?", engine)
    listen_desc = listen(nameAV, engine, 1)

    return listen_desc

def take_start_date(nameAV, engine):
    talk("¿En qué fecha y hora será el evento?", engine)
    listened_date = listen(nameAV, engine, 1)

    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 21', '2021')

    print(listened_date)

    date = datetime.strptime(listened_date, '%d del %m del %Y a las %H:%M') #Mensaje confirmacion
    date_isoformat = datetime.isoformat(date)

    return date_isoformat

def take_end_date(nameAV, engine):
    talk("¿En qué fecha y hora terminará el evento?", engine)
    listened_date = listen(nameAV, engine, 1)

    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 21', '2021')

    print(listened_date)

    date = datetime.strptime(listened_date, '%d del %m del %Y a las %H:%M')
    date_isoformat = datetime.isoformat(date)

    return date_isoformat



def create_event(nameAV, engine):
    event_title = take_event_title(nameAV, engine)
    time.sleep(0.9)
    event_desc = take_event_desc(nameAV, engine)
    time.sleep(0.9)
    start_date = take_start_date(nameAV, engine)
    time.sleep(0.9)
    end_date = take_end_date(nameAV, engine)
    time.sleep(0.9)

    calendar_service = get_calendar_service()  # Servicio de Google Calendar para identificarse

    #Insertar nuevo evento en el calendario
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title.upper(),
            "description": event_desc.upper(),
            "start": {"dateTime": start_date, "timeZone": 'America/Guayaquil'},
            "end": {"dateTime": end_date, "timeZone": 'America/Guayaquil'},
        }
    ).execute()

    print("Evento creado con éxito!")
    print("Título: ", event_result['summary'])
    print("Descripción: ", event_result["description"])
    print("Empieza en: ", event_result["start"])
    print("Termina en: ", event_result["end"])