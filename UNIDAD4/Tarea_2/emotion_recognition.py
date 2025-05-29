import cv2
import os
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

class EmotionRecognizer:
    def __init__(self):
        self.emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
        self.IMG_SIZE = 48

        self.model = self.build_model()

    def build_model(self):
        """Construye el modelo CNN"""
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(self.IMG_SIZE, self.IMG_SIZE, 1)))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(self.emotions), activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, augmented, epochs=15, batch_size=32):
        """Entrena el modelo con los datos organizados por carpetas"""
        print("Cargando datos de entrenamiento...")

        X_train = []
        y_train = []

        for emotion_idx, emotion in enumerate(self.emotions):
            emotion_path = os.path.join(augmented, emotion)
            if not os.path.exists(emotion_path):
                print(f"Carpeta no encontrada: {emotion_path}")
                continue

            for file in os.listdir(emotion_path):
                try:
                    img_path = os.path.join(emotion_path, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is None:
                        continue

                    img_resized = cv2.resize(img, (self.IMG_SIZE, self.IMG_SIZE))
                    img_normalized = img_resized.astype('float32') / 255.0
                    X_train.append(img_normalized)
                    y_train.append(emotion_idx)
                except Exception as e:
                    print(f"Error procesando {file}: {e}")

        X_train = np.array(X_train)
        y_train = keras.utils.to_categorical(y_train, num_classes=len(self.emotions))
        X_train = np.expand_dims(X_train, -1)

        print("Entrenando modelo...")
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1)

        # Guardar modelo entrenado
        model_name = f"modelo_emociones_entrenado_{int(time.time())}.h5"
        self.model.save(model_name)
        print(f"Modelo guardado como: {model_name}")

# --- Ejecución del entrenamiento ---
if __name__ == "__main__":
    recognizer = EmotionRecognizer()
    recognizer.train_model("augmented")  