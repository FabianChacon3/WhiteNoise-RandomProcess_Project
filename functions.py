import numpy as np
from scipy.signal import lfilter
from scipy.fft import fft, ifft, fftfreq, fftshift

# Genera una señal de ruido blanco gaussiano (media 0, varianza 1)
def gaussian_noise(t, A):
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

# Simula la atenuación y dispersion en una fibra optica monomodo
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