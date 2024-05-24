import numpy as np
import matplotlib.pyplot as plt

# amplitud de la onda sinusoidal
amp = 5
# frecuencia de la onda sinusoidal
freq = 0.1
# ruido aleatorio que agregaremos
noise = 0.5

# generamos datos
np.random.seed(42)
t = np.linspace(0, 10, 1000) # tiempo
y = amp * np.sin(2 ** np.pi * freq * t) + np.random.normal(0, noise, len(t))

# creación de etiquetas
lags = 5
X = np.zeros(len(y) - lags, lags)
y_labels = np.zeros(len(y) - lags)
for i in range(len(y) - lags):
    X[i] = y[i:i+lags]
    y_labels[i] = y[y+lags]

# division conjuntos entrenamiento y prueba
train_size = int(0.8 * len(y))
X_train, X_test = X[:train_size], X[train_size]
y_train, y_test = y_labels[:train_size], y_labels[train_size:]

# entrenamiento del modelo
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# evaluación del modelo
score = model.score(X_test, y_test)
print(f'Puntuación del modelo: {score:.2f}')

# predicción futura
future_steps = 50
future_X = X[-1:] # ultimos valores conocidos
future_predictions = []

for _ in range(future_steps):
    future_pred = model.predict(future_X)
    future_predictions.append(future_pred)
    future_X = np.roll(future_X, -1)
    future_X[-1] = future_pred

def graph():
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label="Serie temporal sintética")
    plt.plot(t[-1] + np.arange(1, future_steps + 1), future_predictions, label="Predicciones Futuras", linestyles="--")
    plt.xlabel("Tiempo")
    plt.ylabel("Valor")
    plt.title("Serie temporal Sintética y Predicciones Futuras")
    plt.legend()
    plt.show()

# graph()