Modelo de Series Temporales con Python
Este proyecto tiene como objetivo crear un modelo de series temporales desde cero utilizando Python. Aprenderemos a generar datos sintéticos, entrenar un modelo y predecir valores futuros.
Librerías utilizadas

NumPy: Para operaciones matemáticas y generación de datos.
Matplotlib: Para graficar la serie temporal y las predicciones.

Proceso paso a paso


Generación de datos sintéticos:

Utilizaremos una función sinusoidal para la tendencia y agregaremos ruido aleatorio.
La fórmula general será: y(t)=Asin(2πft)+ϵ(t)


(A): Amplitud de la onda sinusoidal.
(f): Frecuencia (puedes elegir un valor, por ejemplo, 0.1 para una frecuencia baja).
(\epsilon(t)): Ruido aleatorio.





Creación de etiquetas (lags):

Definiremos una ventana temporal para predecir el siguiente valor de la serie.
Por ejemplo, si utilizamos los últimos 5 valores como entrada, predeciremos el siguiente valor.



Entrenamiento del modelo:

Utilizaremos un modelo de regresión (como regresión lineal o árboles de decisión) para predecir el siguiente valor.
Dividiremos los datos en conjuntos de entrenamiento y prueba.
Entrenaremos el modelo en los datos de entrenamiento y evaluaremos su rendimiento en los datos de prueba.



Predicción futura:

Utilizaremos el modelo entrenado para predecir valores futuros de la serie temporal.



Ejecución del código

Asegúrate de tener Python instalado.
Instala las librerías necesarias: pip install numpy matplotlib.
Copia el código proporcionado en un archivo .py.
Ejecuta el archivo para generar la serie temporal y ver las predicciones.