# 🚢 Proyecto Titanic: Limpieza y Exploración de Datos (EDA)

Este proyecto ha sido desarrollado como parte del **Máster en Inteligencia Artificial y Big Data**. El objetivo principal es realizar un análisis profundo y una limpieza profesional del dataset del Titanic, simulando un escenario real para una compañía de seguros marítimos.

## 📌 Contexto del Proyecto
Tras el hundimiento del RMS Titanic en 1912, se busca entender los factores que determinaron la supervivencia. Este análisis es fundamental para calibrar modelos actuariales y mejorar protocolos de seguridad en la industria marítima actual.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Librerías:** Pandas (pilar principal para la manipulación de datos)
* **Entorno:** Jupyter Notebook / Google Colab

---

## 📊 Hallazgos Principales del Análisis
Tras explorar los datos, se extrajeron las siguientes conclusiones clave:

| Factor | Impacto en la Supervivencia |
| :--- | :--- |
| **Género** | Las **mujeres** sobrevivieron en un **74.2%**, frente al **18.9%** de los hombres. |
| **Clase (Pclass)** | La **1ª Clase** tuvo la tasa más alta (62.9%), mientras la **3ª Clase** fue la menor (24.2%). |
| **Edad** | Los **niños** tuvieron prioridad, mostrando tasas de supervivencia superiores a los adultos. |
| **Familia** | Viajar en **familias pequeñas (2-4 personas)** aumentó las posibilidades de sobrevivir comparado con viajar solo. |

---

## 🧹 Proceso de Limpieza y Transformación
Se realizó un tratamiento riguroso para asegurar la calidad de los datos:

### 1. Gestión de Valores Faltantes (Missings)
* **Edad (`Age`):** Se utilizó la **mediana** calculada por grupos según el título del pasajero (Mr, Mrs, Miss), evitando sesgos por valores atípicos.
* **Cabina (`Cabin`):** Dada la alta ausencia de datos (77%), se transformó en una variable binaria: *Tiene Cabina / No Tiene*.
* **Embarque (`Embarked`):** Imputación por la **moda** (puerto más frecuente).

### 2. Ingeniería de Variables (Feature Engineering)
Para mejorar el potencial del dataset, se crearon nuevas características:
* **Title:** Extracción de títulos sociales (Mr, Miss, Master, etc.) a partir de los nombres.
* **FamilySize:** Cálculo del total de parientes a bordo.
* **AgeGroup:** Categorización de pasajeros en grupos (Niño, Adolescente, Adulto, Mayor).

---

## ⚙️ Automatización: La Función `limpiar_titanic()`
Se incluye una función optimizada que automatiza todo el proceso anterior. Es ideal para procesar nuevos datos de forma consistente antes de enviarlos a un modelo de Machine Learning.

```python
def limpiar_titanic(df_input):
    # - Imputa nulos
    # - Crea variables de familia y títulos
    # - Categoriza edades
    # - Elimina columnas irrelevantes (Ticket, Name, etc.)
    return df_limpio
