import cv2
from keras.models import load_model
import numpy as np

# Cargar el modelo entrenado
model = load_model("flowers.keras")  # Asegúrate de tener el nombre correcto del archivo

# Función para procesar la imagen y hacer la predicción
def predict_flower(image_path):
    IMG_SIZE = 150
    # Cargar la imagen y redimensionarla al tamaño esperado por el modelo (150x150)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = np.reshape(img, [1, IMG_SIZE, IMG_SIZE, 3])

    # Normalizar los valores de píxeles
    img = img / 255.0

    # Realizar la predicción
    prediction = model.predict(img)
    
    # Obtener el tipo de flor predicha
    flower_types = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']
    predicted_flower = flower_types[np.argmax(prediction)]

    return predicted_flower

# Ruta de la imagen que deseas predecir
image_path_to_predict = "dandelion_test.jpg"  # Cambia esto por la ruta de tu imagen

# Hacer la predicción
predicted = predict_flower(image_path_to_predict)
print('La flor mostrada es de tipo:', predicted)
