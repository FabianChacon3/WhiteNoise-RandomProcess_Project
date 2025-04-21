import matplotlib.pyplot as plt

# Gráfica de Correlación
def grafcorrelation(lags, correlation):
    plt.figure(figsize=(10, 4))
    plt.plot(lags, correlation)
    plt.title("Correlación cruzada entre señal transmitida y recibida")
    plt.xlabel("Retardo [muestras]")
    plt.ylabel("Correlación")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Gráfica de cambios temporales en la señal
def graftimechange(t, s_t, noise_signal, finalsignal):
    
    plt.figure(figsize=(14, 10))

    # 1. Señal original
    plt.subplot(3, 1, 1)
    plt.plot(t, s_t)
    plt.title("1. Señal modulada AM (sin ruido)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # 2. Señal con ruido
    plt.subplot(3, 1, 2)
    plt.plot(t, noise_signal)
    plt.title("2. Señal con ruido blanco")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # 3. Señal final (después de la fibra)
    plt.subplot(3, 1, 3)
    plt.plot(t, finalsignal)
    plt.title("3. Señal después del canal de fibra óptica")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------- ESPECTRO ----------
def grafpsd(f, Pxx_original, Pxx_final):
    plt.figure(figsize=(12, 5))
    plt.semilogy(f, Pxx_original, label='Original')
    plt.semilogy(f, Pxx_final, label='Después de la fibra')
    plt.title("4. Densidad espectral de potencia (Welch)")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Potencia [dB]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()