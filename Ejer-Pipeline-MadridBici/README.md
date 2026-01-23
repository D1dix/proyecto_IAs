Modelo de Predicción MadridBici 🚲
Descripción
Modelo de Regresión Lineal desarrollado en NumPy para predecir la demanda diaria del sistema público de bicicletas basado en variables meteorológicas.

Variables Utilizadas
Temperatura (°C)
Humedad (%)
Velocidad del viento (km/h)
Precipitación (mm)
Rendimiento
MAE (Error Medio Absoluto): 210.98 bicicletas.
Instrucciones de uso
Cargar el archivo modelo_madridbici.npz.
Normalizar los datos de entrada con las medias/stds guardadas.
Ejecutar la función predecir_demanda().
Limitaciones
No incluye factores de eventos especiales (manifestaciones, huelgas).
El modelo asume una relación lineal entre el clima y la demanda.
