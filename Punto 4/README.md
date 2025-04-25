# Simulación de Ruido Blanco Gaussiano y Dispersión en Fibra Óptica

Este proyecto simula un sistema de transmisión óptico donde se evalúa el impacto del **ruido blanco gaussiano** y la **dispersión cromática** sobre una señal digital modulada a partir de medidas estadisticas.

## Estructura del Proyecto

- `FibreSimu.py`: script principal que organiza la simulación, genera gráficas y estadísticas.
- `functions.py`: contiene las funciones de modulación, ruido, canal de fibra y filtros.
- `graphics.py`: se encarga de todas las gráficas necesarias para el análisis.

## Contexto

En una red metropolitana de fibra óptica que conecta universidades y centros de datos, se transmite información digital a 1 Gbps mediante modulación en cuadratura (QAM). Sin embargo, la dispersión cromática provoca que las señales de diferentes longitudes de onda viajen a velocidades ligeramente distintas, generando distorsión acumulativa en el receptor. Además, el sistema se ve afectado por ruido térmico y de cuantización, modelado como ruido blanco gaussiano.

La empresa responsable de la red necesita evaluar el impacto de la dispersión sobre el ruido del sistema y proponer estrategias de mitigación, como el uso de filtros digitales adaptados o ecualizadores.

## Tareas Desarrolladas

1. **Generación de señal digital aleatoria** dentro de un rango de niveles determinado.
2. **Modulación AM tipo QAM**, donde la amplitud de la portadora varía según la señal digital.
3. **Inyección de ruido blanco gaussiano**, suavizado mediante convolución recursiva (ventana cuadrada).
4. **Simulación del canal de fibra óptica**, que incluye atenuación y dispersión cromática (β₂).
5. **Análisis de correlación cruzada** entre señal transmitida y recibida.
6. **Estimación espectral (PSD)** usando el método de Welch.
7. **Visualización de la densidad de probabilidad (PDF)** para ver la distorsión estadística.
8. **Aplicación de filtros de compensación**:
   - **Filtro de dispersión inversa**
   - **Filtro de frecuencia tipo pasa banda**

## Resultados y Análisis

- **Ensanchamiento temporal**: La dispersión genera un ensanchamiento temporal de los pulsos, lo cual produce solapamiento entre bits (interferencia intersimbólica).
- **Ruido gaussiano**: Afecta principalmente la amplitud, generando una distribución más dispersa en la salida.
- **Correlación cruzada**:  Se evidencia que la señal recibida ha perdido estructura debido al canal dispersivo por la forma ancha y difusa del patrón, sin un pico definido. 
- **PSD**: Se observa un aumento de la banda ocupada por la señal tras pasar por la fibra, confirmando el efecto de dispersión.
- **PDF**: La señal de salida tiene mayor varianza y menor concentración alrededor de la media debido a la dispersión generada.

Ahhh buena esa bro, eso **sí vale la pena mencionarlo**, pero con estilo. Esos valores **aportan un análisis cuantitativo importante**, que complementa lo visual.

### Análisis Cuantitativo

- **Estadísticas de la señal**:
  - La **media** de la señal apenas cambia entre entrada y salida, lo que indica que el canal no introduce sesgo, aunque sí hay pequeñas variaciones.
  - La **varianza** se reduce ligeramente lo que refleja cierta atenuación del contenido energético tras pasar por la fibra.

- **Coeficiente de correlación**:
  - Se obtiene un valor cercano a 1 pero no 1, lo cual indica que, aunque la forma global de la señal se mantiene, existe cierta distorsión no despreciable provocada por la dispersión y el ruido del canal.


## Estrategias de Mitigación

Se implementan dos filtros digitales para recuperar la señal:

- **Filtro inverso de dispersión cromática**, basado en invertir la fase generada por el canal.
- **Filtro de frecuencia pasa banda**, centrado en la frecuencia portadora con un ancho de banda ajustado.

Estos filtros ayudan a reducir el ensanchamiento y mejorar la correlación con la señal original.
