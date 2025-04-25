import numpy as np
from scipy.signal import correlate, welch
from graphics import *
from functions import *


# ---------------- ANALISIS DE a y G --------------------------
codigos  = [2,2,0,4,2,7,7,  2,2,1,4,1,9,2,  2,2,1,0,4,1,3]
digfinal = [codigos[i] for i in range(6, len(codigos), 7)]

G = sum(digfinal) % 10     # Dígito final de la suma de los últimos dígitos de los código
a = np.median(codigos)     # La mediana de los dígitos del código
A = 10 + G                 # Número de muestras
# -------------------------------------------------------------



minlevel = 1; maxlevel = 6; bits = 50
message = 2*np.random.randint(minlevel, maxlevel, bits)     # Mensage digital aleatorio 

fs = 5e7            # Frecuencia de muestreo
fc = 1e7            # Frecuencia portadora
Tbit = 1e-4         # Tiempo de bit
Ac = 1              # Amplitud Portadora

t, s_t = qam_modulator(message, fc=fc, fs=fs, Tbit=Tbit, A=Ac)    # Mensaje modulado

noise_signal = s_t + gaussian_noise(t, A)                         # Adicion de ruido

finalsignal = fibra_optica(noise_signal, t, fc=fc)                # aplicacion del modelo de la fibra optica


# Grafica de cambios en la forma de onda
graftimechange(t, s_t, noise_signal, finalsignal)


# --------------------- Correlación ---------------------------
correlation = correlate(s_t, finalsignal, mode='full')/len(s_t)
lags = np.arange(-len(s_t) + 1, len(s_t))

# Gráfica de Correlación
grafcorrelation(lags, correlation)
# -------------------------------------------------------------


# ------- PSD para la señal enviada y la señal recibida -------
f, Pxx_original = welch(s_t, fs=1e6, nperseg=2048)
f, Pxx_final = welch(finalsignal, fs=1e6, nperseg=2048)

# Gráfica de PSD
grafpsd(f, Pxx_original, Pxx_final)
# -------------------------------------------------------------


# ------------ Funcion de Densidad de Probabilidad ------------
grafPDF(s_t, finalsignal)
# -------------------------------------------------------------


# ------------------- Medidas estadísticas --------------------
# Media y Varianza
print("Entrada -> media:", np.mean(s_t), "varianza:", np.var(s_t))
print("Salida -> media:", np.mean(finalsignal), "varianza:", np.var(finalsignal))

# Correlación
correlacion = np.corrcoef(s_t, finalsignal)[0, 1]
print("Coeficiente de correlación:", correlacion)
# -------------------------------------------------------------


# ------------------ Filtrado de la señal ---------------------
filtrada = disperfilter(finalsignal, t, fc=fc, D=17)     # Filtro de dispersion
filtrada = freqfilter(filtrada, fc=fc, fs=fs, bw=2e5)    # Filtro de frecuencia
filtrada = filtrada*(max(s_t)/max(filtrada))             # Ganancia

#Gráfica de la señal filtrada
graffilter(t, filtrada)
# -------------------------------------------------------------



plt.show()