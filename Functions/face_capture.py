import cv2 # Tratamiento de imagenes
import os
import imutils # Manipular imagen
import numpy as np

from Functions.face_trainer import faceTrainer


def faceCapture(path):
    dimData =  np.size((os.listdir('Data_Face')))
    person = 'NuevoIndividuo' + str(dimData+1)
    data_path = 'Data_Face'
    person_path = data_path + '/' + person # Crear carpeta donde se almacenarán las imagenes generadas (data)

    # Verificar en el caso que no existe los directorios previos
    if not os.path.exists(person_path):
        os.makedirs(person_path)

    capture = cv2.VideoCapture(path)  # 0 tu propia camara, #1 camara remota, path.mp4


    face_classif = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')
    count = 0

    while True:
        comp, frame = capture.read()
        if comp == False:
            break
        frame = imutils.resize(frame, width=640) # Tamaño de imagenes
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux_frame = frame.copy()

        faces = face_classif.detectMultiScale(gray, 1.5, 2)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # dibuja rectangulo en el rostro
            face = aux_frame[y:y+h, x:x+w] #recoleccion de data
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(person_path+f'/face_{count}.jpg', face)
            count += 1

        cv2.imshow('frame', frame) # Mostramos ventana
        key = cv2.waitKey(1)

        if key == ord('s') or key == 27 or count >= 600:
            break

    capture.release()
    cv2.destroyAllWindows()

    faceTrainer()