from funciones import (
    generar_AR1, filtro_fir_custom, filtro_impulso,
    filtro_senoidal, filtro_sinc, sistema_no_lineal,
    calcular_autocorrelacion
)
from graficas import graficar_senal_y_espectro, graficar_autocorrelacion
import numpy as np

# Parámetros generales
n = 10000
alpha = np.exp(-1)
sigma = np.sqrt(1 - alpha**2)

# Generar proceso AR(1)
x = generar_AR1(alpha, sigma, n)

# Filtros
y_fir = sistema_no_lineal(filtro_fir_custom(x, alpha))
y_impulso = sistema_no_lineal(filtro_impulso(x))
y_sin = sistema_no_lineal(filtro_senoidal(x))
y_sinc = sistema_no_lineal(filtro_sinc(x))

# Estadísticas
# Aquí debes implementar o importar la función `estadisticas` si es necesaria

# Gráficas
graficar_senal_y_espectro(x, 1, "x[n] original")
graficar_senal_y_espectro(y_fir, 1, "y filtro ℎ[k] = [1, -1/a, 1/2a]")
graficar_senal_y_espectro(y_impulso, 1, "y filtro ℎ[k] = 3δ(k−2)")
graficar_senal_y_espectro(y_sin, 1, "y filtro senoidal")
graficar_senal_y_espectro(y_sinc, 1, "y filtro sinc[k]")

# Autocorrelaciones
r_x = calcular_autocorrelacion(x)
graficar_autocorrelacion(r_x, "Autocorrelación x[n]", np.mean(x), np.var(x))

r_fir = calcular_autocorrelacion(y_fir)
graficar_autocorrelacion(r_fir, "Autocorrelación y FIR", np.mean(y_fir), np.var(y_fir))

r_impulso = calcular_autocorrelacion(y_impulso)
graficar_autocorrelacion(r_impulso, "Autocorrelación y impulso", np.mean(y_impulso), np.var(y_impulso))

r_sin = calcular_autocorrelacion(y_sin)
graficar_autocorrelacion(r_sin, "Autocorrelación y senoidal", np.mean(y_sin), np.var(y_sin))

r_sinc = calcular_autocorrelacion(y_sinc)
graficar_autocorrelacion(r_sinc, "Autocorrelación y sinc", np.mean(y_sinc), np.var(y_sinc))

# Mostrar todas las gráficas
import matplotlib.pyplot as plt
plt.show()
