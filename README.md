# Simulación de Ruido Blanco Gaussiano y Dispersión en Fibra Óptica

Este proyecto simula el efecto de la dispersión cromática y el ruido blanco gaussiano en un sistema de comunicación óptica que utiliza modulación QAM. Se analiza cómo estos factores afectan la calidad de la señal y se proponen estrategias para mitigar sus efectos.

## Contexto

En una red metropolitana de fibra óptica que conecta universidades y centros de datos, se transmite información digital a 1 Gbps mediante modulación en cuadratura (QAM). Sin embargo, la dispersión cromática provoca que las señales de diferentes longitudes de onda viajen a velocidades ligeramente distintas, generando distorsión acumulativa en el receptor. Además, el sistema se ve afectado por ruido térmico y de cuantización, modelado como ruido blanco gaussiano.

La empresa responsable de la red necesita evaluar el impacto de la dispersión sobre el ruido del sistema y proponer estrategias de mitigación, como el uso de filtros digitales adaptados o ecualizadores.

## Tareas Desarrolladas

1. **Generación de ruido blanco gaussiano** con potencia unitaria utilizando convolución recursiva (ventana cuadrada).
2. **Modelado de un canal de fibra óptica** con dispersión cromática y atenuación, basado en el parámetro β₂ y la longitud de onda de la portadora.
3. **Modulación QAM** de una señal digital aleatoria para simular el proceso de transmisión real.
4. **Adición de ruido** a la señal transmitida.
5. **Aplicación del canal de fibra óptica** al mensaje modulado + ruido.
6. **Gráficas de autocorrelación** y **densidad espectral de potencia (PSD)** para analizar cómo cambia la señal tras pasar por el canal.
7. **Cálculo de correlación cruzada** entre la señal original y la recibida para evaluar el nivel de distorsión.

## Análisis

- La dispersión genera un ensanchamiento temporal de los pulsos, lo cual produce solapamiento entre bits (interferencia intersimbólica).
- El ruido blanco gaussiano afecta principalmente la amplitud de la señal, generando una degradación del SNR.
- La correlación cruzada muestra una pérdida de alineamiento en la forma de onda, aunque el retardo es bajo.
- El análisis espectral evidencia un ensanchamiento de la banda útil tras el canal dispersivo.