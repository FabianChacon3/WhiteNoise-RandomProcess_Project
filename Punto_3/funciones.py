import numpy as np
from scipy.signal import lfilter, welch

# --- Generación de señales ---
def generar_AR1(alpha, sigma_w, n, media=0):
    """Genera señal AR(1) con media y varianza personalizables"""
    w = np.random.normal(0, sigma_w, n)
    x = np.zeros(n) + media
    for i in range(1, n):
        x[i] = alpha * (x[i-1] - media) + w[i] + media
    return x

# --- Filtros ---
def filtro_fir_custom(x, a):
    """Filtro FIR: h[k] = [1, -1/a, 1/(2a)]"""
    b = [1, -1/a, 1/(2*a)]
    return lfilter(b, [1], x)

def filtro_impulso(x):
    """Filtro h[k] = 3δ[k-2] (retardo de 2 muestras, ganancia 3)"""
    h = np.array([0, 0, 3])
    return np.convolve(x, h, mode='same')

def filtro_senoidal(x, frecuencia=0.01, fs=1000):
    """Filtro senoidal: h[k] = sin(2πfk/fs)"""
    n = np.arange(len(x))
    h = np.sin(2 * np.pi * frecuencia * n / fs)
    h = h / np.max(np.abs(h))  # Normalización por máximo
    return np.convolve(x, h, mode='same')

def filtro_sinc(x, ancho=0.05, fs=1000):
    """Filtro sinc: h[k] = sinc(2*ancho*k/fs)"""
    n = np.arange(-100, 101)
    h = np.sinc(2 * ancho * (n / fs))
    h = h / np.max(np.abs(h))  # Normalización por máximo
    return np.convolve(x, h, mode='same')

def sistema_no_lineal(x):
    """Sistema no lineal: y(t) = x²(t) (versión corregida)"""
    return x**2 - np.mean(x**2)  # Quita el componente DC

def calcular_autocorrelacion(x):
    """Calcula autocorrelación normalizada CENTRADA en τ=0"""
    n = len(x)
    x_centrada = x - np.mean(x)
    autocorr = np.correlate(x_centrada, x_centrada, mode='full') / n
    return autocorr  # Devuelve la autocorrelación completa (no recortada)

def calcular_PSD(x, fs):
    """Calcula PSD en dB usando Welch"""
    f, Pxx = welch(x, fs, nperseg=1024)
    return f, 10 * np.log10(Pxx)

def calcular_estadisticas(x):
    """Retorna media y varianza"""
    return np.mean(x), np.var(x)