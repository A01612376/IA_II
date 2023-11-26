# IA_II
##Repositorio para el segundo bloque de Inteligencia artificial avanzada para la ciencia de datos

###Flowers_CNN_Josemaría_A01612376
Contiene un **código** para generar un **modelo CNN** el cual clasifica flores por medio de imágenes. 

###.py
**main.py** es un archivo que llama al modelo guardado y al que se le da un archivo o **imagen con formato _.jpg_** para generar una **predicción**. Al correrlo te devolverá un texto diciendo el tipo de flor de la imagen dada.

###.model y .keras
**flowers.model.h5** y **flowers.keras** son **archivos donde están guardados el modelo**, son independientes entre ellos y se debe usar **únicamente uno dentro del archivo main.py** para la ejecución y pruebas del modelo.

###.jpg
Los archivos .jpg son para uso experimental del modelo, con éstas se realizan las predicciones dentro de main.py

###.pdf
**"Reporte de Implementación Deep Learning"** es la documentación correspondiente al desarrollo del modelo. **_Análisis de seguridad y logs de acceso_ archivo correspondiente a la documentación del manejo de seguridad del reto del bloque correspondiente, _no está relacionado con el modelo CNN_ y es _evidencia_ de la subcompetencia _SEG0403B_**

###Librerías necesarias para el código
- warnings
- numpy
- pandas
- matplotlib.pyplot
- seaborn
- sklearn
- keras
- random
- cv2
- tqdm
- PIL
