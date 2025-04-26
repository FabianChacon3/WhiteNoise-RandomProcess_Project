import matplotlib.pyplot as plt
import numpy as np

# --- Gráficas para señales y filtros ---
def graficar_senal_y_espectro(x, fs, titulo):
    """Grafica señal en tiempo y su espectro"""
    n = len(x)
    t = np.arange(n) / fs
    f = np.fft.fftfreq(n, 1/fs)[:n//2]
    X_fft = np.abs(np.fft.fft(x)[:n//2]) / n

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, x, 'b-')
    plt.title(f'Señal en Tiempo: {titulo}')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(f, 20 * np.log10(X_fft), 'g-')
    plt.title(f'Espectro de {titulo}')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.grid(True)
    plt.tight_layout()

# --- Gráficas de autocorrelación ---
def graficar_autocorrelacion(r, titulo, media=None, varianza=None):
    """Grafica autocorrelación centrada en τ=0 con ejes en 0 y líneas de media/varianza"""
    L = len(r)
    lags = np.arange(-(L-1)//2, (L+1)//2)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(lags, r, 'm-', linewidth=1, label='Autocorrelación')
    ax.axhline(0, color='k', linewidth=1)
    ax.axvline(0, color='k', linewidth=1)
    if media is not None:
        ax.axhline(media, color='b', linestyle='--', label=f'Media: {media:.2f}')
    if varianza is not None:
        ax.axhline(varianza, color='r', linestyle='--', label=f'Varianza: {varianza:.2f}')
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_visible(True)

    ax.set_title(f'Autocorrelación de {titulo}')
    ax.set_xlabel('Retardo $\\tau$ [muestras]')
    ax.set_ylabel('$R(\\tau)$')
    ax.legend()
    ax.grid(True)

# --- Gráficas para sistema no lineal ---
def graficar_resultados_no_lineales(t, y, r_y, f, Pxx_y, *args):
    """Grafica resultados para y(t) = x²(t) - E[x²] con autocorrelación y líneas de tendencia simuladas"""
    # Figura 1: Tiempo y Espectro
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t[:500], y[:500], 'b-')
    plt.title('Señal no lineal $y(t)$')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(f, Pxx_y, 'r-')
    plt.title('PSD de $y(t)$')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Potencia [dB]')
    plt.grid(True)
    plt.tight_layout()

    # Figura 2: Autocorrelación centrada en τ=0
    L = len(r_y)
    lags = np.arange(-(L-1)//2, (L+1)//2)
    center = (L-1)//2
    taus = lags[center:center+200]
    values = r_y[center:center+200]

    # Cálculo de media y varianza simuladas usando numpy
    media_sim = np.mean(y)
    varianza_sim = np.var(y)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(taus, values, 'm-', linewidth=1, label='Simulado')
    ax.axhline(0, color='k', linewidth=1)
    ax.axvline(0, color='k', linewidth=1)
    # Líneas de media y varianza simuladas
    ax.axhline(media_sim, color='b', linestyle='--', label=f'Media simulada: {media_sim:.2f}')
    ax.axhline(varianza_sim, color='r', linestyle='--', label=f'Varianza simulada: {varianza_sim:.2f}')
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_visible(True)

    ax.set_title('Autocorrelación de $y(t)$')
    ax.set_xlabel('Retardo $\\tau$ [muestras]')
    ax.set_ylabel('$R(\\tau)$')
    ax.legend()
    ax.grid(True)
