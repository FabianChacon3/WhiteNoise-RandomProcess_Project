from funciones import *
from graficas import *
import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
n = 10000
fs = 5000
alpha = np.exp(-1)
media_x = 0  # ¡Importante para el análisis no lineal!
varianza_x = 4.0
sigma_w = np.sqrt(varianza_x * (1 - alpha**2))

# --- Generar señal AR(1) ---
x = generar_AR1(alpha, sigma_w, n, media_x)
t = np.arange(n) / fs

# --- Aplicar filtros ---
y_fir = filtro_fir_custom(x, alpha)
y_impulso = filtro_impulso(x)
y_sen = filtro_senoidal(x, frecuencia=0.01, fs=fs)
y_sinc = filtro_sinc(x, ancho=0.05, fs=fs)

# --- Sistema no lineal y(t) = x²(t) ---
y_no_lineal = sistema_no_lineal(x)
r_y = calcular_autocorrelacion(y_no_lineal)
f, Pxx_y = calcular_PSD(y_no_lineal, fs)

# --- Cálculos teóricos no lineal ---
media_teorica = varianza_x  # E[y] = σ²
varianza_teorica = 2 * varianza_x**2  # Var[y] = 2σ⁴

# --- Graficar ---
# 1. Señales filtradas
graficar_senal_y_espectro(x, fs, "x[n] original")
graficar_senal_y_espectro(y_fir, fs, "y[n] (FIR)")
graficar_senal_y_espectro(y_impulso, fs, "y[n] (Impulso)")
graficar_senal_y_espectro(y_sen, fs, "y[n] (Senoidal)")
graficar_senal_y_espectro(y_sinc, fs, "y[n] (Sinc)")

# 2. Autocorrelaciones
graficar_autocorrelacion(calcular_autocorrelacion(x), "x[n]", *calcular_estadisticas(x))
graficar_autocorrelacion(calcular_autocorrelacion(y_fir), "y[n] (FIR)", *calcular_estadisticas(y_fir))
graficar_autocorrelacion(calcular_autocorrelacion(y_impulso), "y[n] (Impulso)", *calcular_estadisticas(y_impulso))
graficar_autocorrelacion(calcular_autocorrelacion(y_sen), "y[n] (Senoidal)", *calcular_estadisticas(y_sen))
graficar_autocorrelacion(calcular_autocorrelacion(y_sinc), "y[n] (Sinc)", *calcular_estadisticas(y_sinc))

# 3. Sistema no lineal
graficar_resultados_no_lineales(t, y_no_lineal, r_y, f, Pxx_y, media_teorica, varianza_teorica)


# --- Resultados numéricos ---
print("\n--- Estadísticas ---")
print(f"x[n]: Media = {np.mean(x):.2f}, Varianza = {np.var(x):.2f}")
print(f"y[n] FIR: Media = {np.mean(y_fir):.2f}, Varianza = {np.var(y_fir):.2f}")
print(f"y[n] Impulso: Media = {np.mean(y_impulso):.2f}, Varianza = {np.var(y_impulso):.2f}")
print(f"y[n] Senoidal: Media = {np.mean(y_sen):.2f}, Varianza = {np.var(y_sen):.2f}")
print(f"y[n] Sinc: Media = {np.mean(y_sinc):.2f}, Varianza = {np.var(y_sinc):.2f}")
print("\n--- Sistema no lineal y(t) = x²(t) ---")
print(f"Media teórica: {media_teorica:.4f} | Media simulada: {np.mean(y_no_lineal):.4f}")
print(f"Varianza teórica: {varianza_teorica:.4f} | Varianza simulada: {np.var(y_no_lineal):.4f}")

plt.show()