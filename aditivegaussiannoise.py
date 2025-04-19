import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, correlate, welch


codigos  = [2,2,0,4,2,7,7,  2,2,1,4,1,9,2,  2,2,1,0,4,1,3]
digfinal = [codigos[i] for i in range(6, len(codigos), 7)]

G = sum(digfinal) % 10     # Dígito final de la suma de los últimos dígitos de los código
a = np.median(codigos)     # La mediana de los dígitos del código
A = 10 + G                 # Número de muestras

# Se genera una señal de ruido blanco gaussiano (media 0, varianza 1)
def gaussian_noise(t):
    x = np.random.normal(0, 1, len(t))
    ventana = np.ones(A) / A
    x_gauss = lfilter(ventana, [1], x)      # Convolución recursiva
    return x_gauss

# Modulador QAM modo AM
def qam_modulator(message, Tbit=0.001, A=1, ka=0.5, fc=1e5, fs=1e6):
    Ns = int(fs * Tbit)                    # Muestras por bit
    total_samples = Ns * len(message)      # Total de muestras
    t = np.arange(0, total_samples) / fs   # Vector de tiempo

    # Expande el mensaje: cada valor se repite Ns veces
    message_expanded = np.repeat(message, Ns)

    # Modulación AM
    s_t = A * (1 + ka * message_expanded) * np.cos(2 * np.pi * fc * t)

    return t, s_t


message = np.random.randint(1,6,50)     # Mensage digital aleatorio (valor_minimo, valor_maximo, #bits)

t, s_t = qam_modulator(message)         # Mensaje modulado

noise_signal = s_t + gaussian_noise(t)


# Gráficas
plt.figure(figsize=(12, 6))

plt.subplot(2,1,1)
plt.plot(t, s_t, label='Señal modulada (limpia)')
plt.title("Señal modulada sin ruido")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, noise_signal, label='Señal con ruido', color='orange')
plt.title("Señal modulada con ruido")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()