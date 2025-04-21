import numpy as np
from scipy.signal import lfilter, correlate, welch
from scipy.fft import fft, ifft, fftfreq, fftshift
from graphics import *


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

    return t, s_t, fc


def fibra_optica(signal, t, D=17e-6, L=1, atenuation=0.2, fc=1e5):
    # Constantes
    c = 3e8  # velocidad de la luz (m/s)
    lambda_m = c / fc  # longitud de onda en metros a partir de fc

    # Convertir parámetros
    alpha_np = atenuation / 4.343  # Np/km
    beta2 = (D * 1e-6) * (lambda_m**2) / (2 * np.pi * c)  # s^2/m
    beta2 = beta2 * 1e3  # s^2/km

    # Tiempo y frecuencia
    dt = t[1] - t[0]
    N = len(t)
    f = fftshift(fftfreq(N, dt))

    # FFT de la señal
    S = fft(signal)

    # Respuesta del canal
    phi = beta2 * (2 * np.pi * (f - fc))**2 * L
    H = np.exp(-alpha_np * L) * np.exp(1j * phi)

    # Aplicar canal
    S_out = S * H
    signal_out = np.real(ifft(S_out))
    
    return signal_out

minlevel = 1; maxlevel = 6; bits = 50
message = np.random.randint(minlevel, maxlevel, bits)     # Mensage digital aleatorio 

t, s_t, fc = qam_modulator(message)                       # Mensaje modulado

noise_signal = s_t + gaussian_noise(t)                    # Adicion de ruido

finalsignal = fibra_optica(noise_signal, t, fc=fc)               # aplicacion del modelo de la fibra optica

# Grafica de cambios en la forma de onda
graftimechange(t, s_t, noise_signal, finalsignal)


# Correlación
correlation = correlate(s_t, finalsignal, mode='full')/len(s_t)
lags = np.arange(-len(s_t) + 1, len(s_t))

# Gráfica de Correlación
grafcorrelation(lags, correlation)


# PSD para la señal enviada y la señal recibida
f, Pxx_original = welch(s_t, fs=1e6, nperseg=2048)
f, Pxx_final = welch(finalsignal, fs=1e6, nperseg=2048)

# Gráfica de PSD
grafpsd(f, Pxx_original, Pxx_final)