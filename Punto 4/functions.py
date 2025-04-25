import numpy as np
from scipy.signal import lfilter
from scipy.fft import fft, ifft, fftfreq, fftshift

# Genera una señal de ruido blanco gaussiano (media 0, varianza 1)
def gaussian_noise(t, A):
    # Entrada: 
    #   t : vector de tiempo (define la longitud del ruido)
    #   A : tamaño de la ventana para la convolución
    # Salida: 
    #   x_gauss : señal de ruido blanco suavizado por convolución

    x = np.random.normal(0, 1, len(t))
    ventana = np.ones(A) / A
    x_gauss = lfilter(ventana, [1], x)      # Convolución recursiva
    return x_gauss

# Modulador QAM modo AM
def qam_modulator(message, Tbit=0.001, A=1, ka=0.5, fc=1e9, fs=5e9):
    # Entrada:
    #   message : señal digital (lista o array de bits)
    #   Tbit : duración de un bit (en segundos)
    #   A : amplitud de la portadora
    #   ka : índice de modulación
    #   fc : frecuencia de la portadora (Hz)
    #   fs : frecuencia de muestreo (Hz)
    # Salida:
    #   t : vector de tiempo correspondiente a la señal modulada
    #   s_t : señal modulada en AM

    Ns = int(fs * Tbit)                    # Muestras por bit
    total_samples = Ns * len(message)      # Total de muestras
    t = np.arange(0, total_samples) / fs   # Vector de tiempo

    # Expande el mensaje: cada valor se repite Ns veces
    message_expanded = np.repeat(message, Ns)

    # Modulación AM
    s_t = A * (1 + ka * message_expanded) * np.cos(2 * np.pi * fc * t)

    return t, s_t

# Modelo de canal de una fibra optica monomodo
def fibra_optica(signal, t, D=17, L=0.1, atenuation=0.2, fc=1e9):
    # Entrada:
    #   signal : señal modulada a transmitir
    #   t : vector de tiempo de la señal
    #   D : parámetro de dispersión cromática (ps/nm/km)
    #   L : longitud de la fibra (km)
    #   atenuation : pérdida en dB/km
    #   fc : frecuencia de la portadora (Hz)
    # Salida:
    #   signal_out : señal recibida después de la propagación

    # Constantes
    c = 3e8  # velocidad de la luz (m/s)
    lambda_m = c / fc  # longitud de onda en metros a partir de fc

    # Convertir parámetros
    alpha_np = atenuation / 4.343  # dB/km --> Np/km

    # Coeficiente de propagación
    beta2 = (D * 1e-6) * (lambda_m**2) / (2 * np.pi * c)  # s^2/m

    # Tiempo y frecuencia
    dt = t[1] - t[0]
    N = len(t)
    f = fftshift(fftfreq(N, dt))

    # FFT de la señal
    S = fft(signal)

    # Respuesta del canal
    phi = beta2 * (2 * np.pi * (f - fc))**2 * (L*1e3)
    H = np.exp(-alpha_np * L) * np.exp(1j * phi)

    # Aplicar canal
    S_out = S * H
    signal_out = np.real(ifft(S_out))
    
    return signal_out



# Filtro de dispersion
def disperfilter(signal, t, D=17, L=0.1,  fc=1e9):
    # Entrada:
    #   signal : señal afectada por la dispersión
    #   t : vector de tiempo de la señal
    #   D : parámetro de dispersión cromática (ps/nm/km)
    #   L : longitud de la fibra (km)
    #   fc : frecuencia de la portadora (Hz)
    # Salida:
    #   signal_out : señal corregida tras aplicar el filtro de dispersión

    c = 3e8                    # velocidad de la luz en m/s
    lambda_c = c / fc          # longitud de onda en metros

    # Coeficiente de propagación
    beta2 = (D * 1e-6) * (lambda_c**2) / (2 * np.pi * c)  # s^2/m

    # FFT
    N = len(t)
    dt = t[1] - t[0]
    f = fftshift(fftfreq(N, dt))
    S = fft(signal)

    # Filtro inverso (fase negativa)
    phi = beta2 * (2 * np.pi * (f - fc))**2 * (L*1e3)
    H_inv = np.exp(-1j * phi)

    # Aplicar filtro
    S_out = S * H_inv
    signal_out = np.real(ifft(S_out))

    return signal_out


# Filtro de frecuencia 
def freqfilter(signal, fs=5e9, fc=1e9, bw=2e4):
    # Entrada:
    #   signal : señal a filtrar
    #   fs : frecuencia de muestreo (Hz)
    #   fc : frecuencia central del filtro (Hz)
    #   bw : ancho de banda del filtro (Hz)
    # Salida:
    #   signal_filtrada : señal tras aplicar el filtro en frecuencia

    N = len(signal)
    dt = 1 / fs
    freqs = fftshift(fftfreq(N, dt))
    
    # FFT de la señal
    S = fftshift(fft(signal))
    
    # Filtro pasa banda
    filtro = np.logical_and(freqs >= (fc - bw/2), freqs <= (fc + bw/2)).astype(float)

    # Aplicar filtro
    S_filtrado = S * filtro

    # Volver al dominio del tiempo
    signal_filtrada = np.real(ifft(S_filtrado))
    
    return signal_filtrada