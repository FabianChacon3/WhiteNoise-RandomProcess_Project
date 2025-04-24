import matplotlib.pyplot as plt
import numpy as np

def graficar_senal_y_espectro(x, fs, titulo):
    n = len(x)
    t = np.arange(n)
    f = np.fft.fftfreq(n, 1/fs)
    X_f = 20 * np.log10(np.abs(np.fft.fft(x)))

    # Tiempo
    plt.figure()
    plt.plot(t, x, linewidth=1.5)
    plt.title(f'Señal en Tiempo - {titulo}')
    plt.xlabel('n')
    plt.ylabel('Amplitud')
    plt.grid(True, which='both')
    plt.tight_layout()

    # Espectro
    plt.figure()
    plt.plot(f[:n//2], X_f[:n//2], color='green', linewidth=1.5)
    plt.title(f'Espectro de {titulo}')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.grid(True, which='both')
    plt.tight_layout()

def graficar_autocorrelacion(r, titulo, media, varianza):
    n = len(r) // 2
    t = np.arange(-n, n+1)
    plt.figure()
    plt.plot(t, r, linewidth=1.5)
    plt.title(f'Autocorrelación de {titulo}')
    plt.xlabel('τ')
    plt.ylabel('R(τ)')
    plt.grid(True, which='both')
    plt.axhline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
    plt.axhline(varianza, color='blue', linestyle='--', label=f'Var: {varianza:.2f}')
    plt.legend()
    plt.tight_layout()

