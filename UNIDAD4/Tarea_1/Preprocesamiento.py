import cv2
import os
import numpy as np
from tqdm import tqdm

# Parámetros
IMG_SIZE = 48
input_folder = 'train'
output_folder = 'augmented'

# Aumentar o disminuir brillo
def adjust_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    final_hsv = cv2.merge((h, s, v))
    img_bright = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return cv2.cvtColor(img_bright, cv2.COLOR_BGR2GRAY)

# Rotar imagen
def rotate_image(img, angle):
    center = (IMG_SIZE // 2, IMG_SIZE // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, M, (IMG_SIZE, IMG_SIZE))

# Escalar imagen (zoom)
def scale_image(img, scale):
    h, w = img.shape[:2]
    new_h, new_w = int(h * scale), int(w * scale)
    resized = cv2.resize(img, (new_w, new_h))

    if scale > 1.0:
        # Recortar centro si imagen es más grande
        start_h = (new_h - h) // 2
        start_w = (new_w - w) // 2
        return resized[start_h:start_h+h, start_w:start_w+w]
    else:
        # Poner imagen pequeña al centro
        output = np.zeros((h, w), dtype=np.uint8)
        start_h = (h - new_h) // 2
        start_w = (w - new_w) // 2
        output[start_h:start_h+new_h, start_w:start_w+new_w] = resized
        return output

# Aumentación
def augment_and_save(img, label, filename):
    base_path = os.path.join(output_folder, label)
    os.makedirs(base_path, exist_ok=True)
    name = os.path.splitext(filename)[0]

    # Brillo
    brightness_levels = [-80, -50, -20, 0, 20, 50, 80]
    for i, b in enumerate(brightness_levels):
        bright_img = adjust_brightness(img, b) if b != 0 else img
        cv2.imwrite(os.path.join(base_path, f'{name}_bright_{b}.jpg'), bright_img)

    # Rotaciones
    angles = [-45, -30, -15, 0, 15, 30, 45]
    for a in angles:
        rot_img = rotate_image(img, a) if a != 0 else img
        cv2.imwrite(os.path.join(base_path, f'{name}_rot_{a}.jpg'), rot_img)

    # Escalado
    scales = [0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5]
    for s in scales:
        scaled_img = scale_image(img, s) if s != 1.0 else img
        cv2.imwrite(os.path.join(base_path, f'{name}_scale_{s:.1f}.jpg'), scaled_img)

# ----- RECORRER TODAS LAS EMOCIONES -----

for emotion in os.listdir(input_folder):
    emotion_path = os.path.join(input_folder, emotion)
    if not os.path.isdir(emotion_path):
        continue

    for file in tqdm(os.listdir(emotion_path), desc=f'Procesando {emotion}'):
        file_path = os.path.join(emotion_path, file)
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        if img.shape[:2] != (IMG_SIZE, IMG_SIZE):
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        augment_and_save(img, emotion, file)