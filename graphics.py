import matplotlib.pyplot as plt


# Gráfica de cambios temporales en la señal
def graftimechange(t, s_t, noise_signal, finalsignal):
    
    plt.figure(figsize=(12, 10))

    # 1. Señal original
    plt.subplot(3, 1, 1)
    plt.plot(t, s_t)
    plt.title("1. Señal modulada AM (sin ruido)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # 2. Señal con ruido
    plt.subplot(3, 1, 2)
    plt.plot(t, noise_signal)
    plt.title("2. Señal con ruido blanco")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # 3. Señal final (después de la fibra)
    plt.subplot(3, 1, 3)
    plt.plot(t, finalsignal)
    plt.title("3. Señal después del canal de fibra óptica")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()



# Gráfica de Correlación
def grafcorrelation(lags, correlation):
    plt.figure(figsize=(10, 4))
    plt.plot(lags, correlation)
    plt.title("Correlación cruzada entre señal transmitida y recibida")
    plt.xlabel("Retardo [muestras]")
    plt.ylabel("Correlación")
    plt.grid(True)
    plt.tight_layout()



# Grafica de la PSD
def grafpsd(f, Pxx_original, Pxx_final):
    plt.figure(figsize=(12, 5))
    plt.semilogy(f, Pxx_original, label='Original')
    plt.semilogy(f, Pxx_final, label='Después de la fibra')
    plt.title("4. Densidad espectral de potencia (Welch)")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Potencia [dB]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


# Grafica de la señal filtrada
def graffilter(t, signal):
    plt.figure(figsize=(12, 3))
    plt.plot(t, signal, color='dodgerblue')
    plt.title("Señal en el dominio del tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()

import numpy as np
import matplotlib.pyplot as plt

def grafespectro(senal_modulada, fc, fs):
    N = len(senal_modulada)
    f = np.fft.fftfreq(N, 1/fs)
    S = np.fft.fft(senal_modulada)
    S_shifted = np.fft.fftshift(np.abs(S)/N)
    f_shifted = np.fft.fftshift(f)

    plt.figure(figsize=(10, 4))
    plt.plot(f_shifted, S_shifted)
    plt.title("Espectro de la señal AM")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.xlim(fc - 3*fc, fc + 3*fc)
    plt.tight_layout()