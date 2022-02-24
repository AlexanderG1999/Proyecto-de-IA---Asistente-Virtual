import cv2
import os
import threading as tr
import subprocess as sub
import imutils

from Functions.sendMssTelegram import Telegram_Alert

data_path = 'Data_face'
image_paths = os.listdir(data_path)
#print('image_paths=', image_paths)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()  # inicializamos el modelo
# leyendo el modelo
face_recognizer.read('Files/LBPHFaceModel.xml')

face_classif = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')


def face_rec(state):
    capture = cv2.VideoCapture(0)
    while True:
        comp, frame = capture.read()
        if comp == False: break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux_frame = gray.copy()

        faces = face_classif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = aux_frame[y:y+h, x:x+w]
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(face)

            cv2.putText(frame, f'{result}', (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            # LBPHFace
            if result[1] < 76:
                cv2.putText(frame, f'{image_paths[result[0]]}', (x, y-25), 2, 0.8, (0, 255, 0),1 ,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                Telegram_Alert(image_paths[result[0]])
            else:
                #thread_alarma_song(0)
                cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                Telegram_Alert('Desconocido')
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & state == 1 or cv2.waitKey(1) == ord('s'):
            break
            cap.release()
            cv2.destroyAllWindows()
            sub.call(f'taskkill /IM python.exe /F', shell = True)

"""def alarm(state, name):
    if state ==0:
        Telegram_Alert(Desconocido)
    else:
        Telegram_Alert(name)"""

"""def thread_alarm(state, name):
    ta = tr.Thread(target=alarma_song, args=(state,))
    ta.start()
"""
face_rec(0)