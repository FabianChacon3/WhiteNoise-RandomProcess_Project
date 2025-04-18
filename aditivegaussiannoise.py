import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, correlate, welch


codigos = [2204277, 2214192, 2210413]
digfinal = [c % 10 for c in codigos]

G = sum(digfinal) % 10     # Dígito final de la suma de los últimos dígitos de los código
a = np.median(codigos)     # La mediana de los dígitos del código
A = 10 + G                 # Número de muestras

# Se define un vector de tiempo
t = np.arange(0, 10, 0.01)

# Se genera una señal de ruido blanco gaussiano (media 0, varianza 1)
x = np.random.normal(0, 1, len(t))
ventana = np.ones(A) / A
x_gauss = lfilter(ventana, [1], x)                           # Convolución recursiva

print("Media:", np.mean(x_gauss))
print("Varianza:", np.var(x_gauss))

# Gráfica del ruido
plt.figure()
plt.plot(t, x_gauss)
plt.title("Adittive Gaussian Noise")
plt.grid(True)

plt.figure()
plt.hist(ventana, bins=50, density=True, alpha=0.6, color='c')  # histograma normalizado
plt.title("Función de densidad de probabilidad (PDF)")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.grid(True)

plt.show()