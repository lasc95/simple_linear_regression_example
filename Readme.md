# Modelo de Series Temporales con Python

Este proyecto tiene como objetivo crear un modelo de series temporales desde cero utilizando Python. Aprenderemos a generar datos sintéticos, entrenar un modelo y predecir valores futuros.

## Librerías utilizadas

1. **NumPy**: Para operaciones matemáticas y generación de datos.
2. **Matplotlib**: Para graficar la serie temporal y las predicciones.

## Proceso paso a paso

1. **Generación de datos sintéticos**:
   - Utilizaremos una función sinusoidal para la tendencia y agregaremos ruido aleatorio.
   - La fórmula general será: $$y(t) = A \sin(2\pi ft) + \epsilon(t)$$
     - \(A\): Amplitud de la onda sinusoidal.
     - \(f\): Frecuencia (puedes elegir un valor, por ejemplo, 0.1 para una frecuencia baja).
     - \(\epsilon(t)\): Ruido aleatorio.

2. **Creación de etiquetas (lags)**:
   - Definiremos una ventana temporal para predecir el siguiente valor de la serie.
   - Por ejemplo, si utilizamos los últimos 5 valores como entrada, predeciremos el siguiente valor.

3. **Entrenamiento del modelo**:
   - Utilizaremos un modelo de regresión (como regresión lineal o árboles de decisión) para predecir el siguiente valor.
   - Dividiremos los datos en conjuntos de entrenamiento y prueba.
   - Entrenaremos el modelo en los datos de entrenamiento y evaluaremos su rendimiento en los datos de prueba.

4. **Predicción futura**:
   - Utilizaremos el modelo entrenado para predecir valores futuros de la serie temporal.

## Ejecución del código

1. Asegúrate de tener Python instalado.
2. Instala las librerías necesarias: `pip install numpy matplotlib`.
3. Copia el código proporcionado en un archivo `.py`.
4. Ejecuta el archivo para generar la serie temporal y ver las predicciones.
