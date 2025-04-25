import numpy as np
from scipy.signal import lfilter

def generar_AR1(alpha, sigma, n):
    w = np.random.normal(0, sigma, n)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = alpha * x[i-1] + w[i]
    return x

def sistema_no_lineal(x):
    return x**2

def filtro_fir_custom(x, a):
    b = [1, -1/a, 1/(2*a)]
    return lfilter(b, [1], x)

def filtro_impulso(x):
    h = np.zeros(3)
    h[2] = 3
    return np.convolve(x, h, mode='same')

def filtro_senoidal(x, frecuencia=0.1, fs=1):
    n = np.arange(len(x))
    h = np.sin(2 * np.pi * frecuencia * n / fs)
    return np.convolve(x, h, mode='same')

def filtro_sinc(x, ancho=0.1, fs=1):
    n = np.arange(-50, 51)
    h = np.sinc(2 * ancho * (n / fs))
    return np.convolve(x, h, mode='same')

def calcular_autocorrelacion(x):
    n = len(x)
    x_mean = np.mean(x)
    autocorr = np.correlate(x - x_mean, x - x_mean, mode='full') / n
    return autocorr
