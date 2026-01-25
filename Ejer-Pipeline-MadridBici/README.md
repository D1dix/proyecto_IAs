# 🚲 Predicción de Demanda: MadridBici

Este proyecto implementa un pipeline completo de **Machine Learning** utilizando exclusivamente **NumPy**. El objetivo es predecir la demanda diaria de alquiler de bicicletas en Madrid basándose en factores meteorológicos.

## 📊 Resumen del Proyecto
El modelo utiliza una **Regresión Lineal** (entrenada mediante la Ecuación Normal) para entender cómo variables como la temperatura, la lluvia o el viento afectan al uso de las bicicletas públicas.

### Variables del Modelo (Features)
* **Temperatura (°C):** Influencia positiva (a mejor tiempo, más alquileres).
* **Lluvia (mm):** Influencia negativa principal.
* **Viento (km/h):** Factor disuasorio.
* **Humedad (%):** Variable de control ambiental.

## 🛠️ Pipeline de Desarrollo
1.  **Limpieza:** Tratamiento de NaNs y corrección de valores atípicos (Outliers) mediante el método IQR y `np.clip`.
2.  **Análisis:** Cálculo de correlaciones de Pearson para seleccionar las variables con mayor poder predictivo.
3.  **Entrenamiento:** División de datos (Train/Test) y normalización estadística ($\mu = 0, \sigma = 1$).
4.  **Simulación:** Ejecución de una simulación de Monte Carlo (10,000 escenarios) para predecir la demanda ante una ola de calor.
5.  **Producción:** Exportación del modelo en formato `.npz` y creación de una función de predicción lista para usar.

## 📈 Resultados
* **MAE (Error Medio Absoluto):** 185.76 - 210.98 de bicicletas.
* **Capacidad de Respuesta:** El modelo identifica correctamente la caída de demanda en días lluviosos y el pico en días templados.

## 🚀 Cómo usar
Para predecir la demanda de un día específico, carga el modelo y usa la función `predecir_demanda`:

```python
import numpy as np

def predecir(t, h, v, l):
    # Carga pesos y parámetros de normalización
    m = np.load('modelo_madridbici.npz')
    # ... (ver código en notebook)
    return demanda_estimada
