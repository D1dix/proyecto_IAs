# 📊 Proyecto 01 – Análisis de Datos Meteorológicos con NumPy

Máster en Inteligencia Artificial y Big Data
Módulo: Programación de IA

---

## 🧭 Descripción general

Este proyecto consiste en el análisis de un **dataset meteorológico sintético** utilizando **NumPy** como herramienta principal de computación numérica. El objetivo es demostrar el dominio de:

* Creación y manipulación de arrays multidimensionales
* Indexación y slicing
* Operaciones vectorizadas
* Uso correcto del parámetro `axis`
* Broadcasting
* Estadística descriptiva
* Análisis climatológico básico
* Visualización de resultados con `matplotlib`

Todo el proyecto se ha desarrollado **sin usar bucles innecesarios**, priorizando siempre soluciones vectorizadas.

---

## 🗂️ Dataset

El dataset simula datos de la AEMET para **5 estaciones meteorológicas** durante **30 días** (enero), con **24 mediciones diarias** y **6 variables**.

### 📐 Dimensiones

```
(5, 30, 24, 6)
(estaciones, días, horas, variables)
```

### 🌡️ Variables

| Índice | Variable             | Unidad |
| ------ | -------------------- | ------ |
| 0      | Temperatura          | °C     |
| 1      | Humedad relativa     | %      |
| 2      | Presión atmosférica  | hPa    |
| 3      | Velocidad del viento | km/h   |
| 4      | Precipitación        | mm/h   |
| 5      | Radiación solar      | W/m²   |

### 📍 Estaciones

| Índice | Estación           |
| ------ | ------------------ |
| 0      | Madrid-Retiro      |
| 1      | Barcelona-El Prat  |
| 2      | Sevilla-Aeropuerto |
| 3      | Bilbao-Sondica     |
| 4      | Granada-Base Aérea |

---

## 🔍 Bloque 1 – Exploración y acceso a datos

* Verificación de estructura (`shape`, `size`, `dtype`)
* Extracción de series temporales
* Comparación entre estaciones
* Extracción de bloques de datos mediante slicing

👉 Objetivo: comprender y manejar correctamente arrays multidimensionales.

---

## 📈 Bloque 2 – Estadística descriptiva

* Temperatura media por estación
* Perfil horario medio de temperatura
* Variabilidad térmica (desviación estándar)
* Detección de valores extremos

Se incluyen **visualizaciones con matplotlib**, como:

* Perfil horario medio (línea)
* Variabilidad térmica por estación (barras)

---

## 🧪 Bloque 3 – Filtrado y selección condicional

* Detección de heladas (temperatura < 0 °C)
* Días con lluvia significativa (> 10 mm)
* Condiciones de confort climático

Se utiliza **indexación booleana** y operaciones lógicas vectorizadas.

📊 Gráfico destacado:

* Número de heladas por estación (gráfico de barras)

---

## ⚙️ Bloque 4 – Operaciones avanzadas

### Ejercicio 12 – Normalización

* Normalización de cada variable al rango [0, 1]
* Aplicación independiente por variable
* Uso de broadcasting

### Ejercicio 13 – Anomalías térmicas

* Cálculo de anomalías respecto a la media de cada estación
* Identificación de la mayor anomalía positiva

### Ejercicio 14 – Correlación temperatura-humedad

* Correlación calculada **por estación**
* Interpretación física de los resultados

### Ejercicio 15 – Energía solar

* Energía solar diaria por estación
* Media diaria mensual
* Ranking de estaciones por potencial solar

---

## 🧾 Bloque 5 – Informe meteorológico automatizado

Se ha desarrollado un **informe completo por estación**, generado sin bucles, que incluye:

### 🌡️ Temperatura

* Media
* Mínima
* Máxima
* Amplitud térmica media diaria

### 🌧️ Precipitación

* Total acumulado mensual
* Número de días con lluvia (>1 mm)

### 💨 Viento

* Velocidad media
* Porcentaje de horas con viento fuerte (>40 km/h)

### ☀️ Radiación solar

* Energía total acumulada mensual

Los resultados se agrupan en un **diccionario estructurado** y se imprimen de forma formateada, con redondeo a 2 decimales.

---

## 📊 Visualizaciones

Se han utilizado gráficos con `matplotlib` para facilitar la interpretación:

* Perfil horario medio de temperatura
* Variabilidad térmica por estación
* Número de heladas por estación

Los gráficos incluyen:

* Etiquetas claras
* Títulos descriptivos
* Valores destacados en negrita

---

## 🎓 Conclusiones

Este proyecto demuestra el uso eficiente de NumPy para el análisis de grandes volúmenes de datos meteorológicos, aplicando técnicas reales utilizadas en contextos profesionales como:

* Climatología
* Energías renovables
* Agricultura de precisión
* Análisis ambiental

Además, se han seguido buenas prácticas de programación científica y visualización de datos.

---

## 🧠 Autor

Proyecto desarrollado como parte del Máster en Inteligencia Artificial y Big Data.

---

✅ **Proyecto completo, vectorizado y listo para defensa oral.**

