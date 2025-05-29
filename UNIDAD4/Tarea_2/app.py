import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Cargar el modelo entrenado
modelo = load_model("modelo_emociones_entrenado.h5") 
# Lista de emociones
emociones = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
IMG_SIZE = 48

# Cargar clasificador Haar para detección de rostros
detector_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Iniciar cámara
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = detector_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in rostros:
        rostro = gris[y:y+h, x:x+w]
        rostro_redimensionado = cv2.resize(rostro, (IMG_SIZE, IMG_SIZE))
        rostro_normalizado = rostro_redimensionado.astype('float32') / 255.0
        rostro_reshapeado = np.expand_dims(rostro_normalizado, axis=0)
        rostro_reshapeado = np.expand_dims(rostro_reshapeado, axis=-1)

        prediccion = modelo.predict(rostro_reshapeado)
        emocion_predicha = emociones[np.argmax(prediccion)]

        # Dibujar el recuadro y la emoción
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emocion_predicha, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Reconocimiento de Emociones", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
