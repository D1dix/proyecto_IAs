Este es un README.md diseñado para ser profesional, directo y fácil de entender, resumiendo todos los puntos clave de tu proyecto de limpieza y exploración del dataset Titanic.

🚢 Proyecto: Limpieza y Exploración del Dataset Titanic
Este proyecto forma parte del Máster en Inteligencia Artificial y Big Data. El objetivo es realizar un análisis exhaustivo y una limpieza de datos (EDA) sobre el famoso dataset del Titanic para entender qué factores influyeron en la supervivencia de los pasajeros.

📋 Contexto del Proyecto
Una compañía de seguros marítimos requiere analizar los datos históricos del naufragio del RMS Titanic (1912) para mejorar sus modelos de riesgo y políticas de evacuación en cruceros modernos.

🛠️ Tecnologías Utilizadas
Lenguaje: Python


Librerías: Pandas (Carga, manipulación y limpieza) 

Entorno: Jupyter Notebook / Google Colab

🔍 Hallazgos Principales (EDA)
Tras explorar los 891 registros del dataset, se identificaron los siguientes patrones clave:

Supervivencia por Sexo: Las mujeres tuvieron una tasa de supervivencia del 74.2% frente al 18.9% de los hombres, confirmando la política de "mujeres y niños primero".

Impacto de la Clase: La Primera Clase tuvo la mayor probabilidad de supervivencia (62.9%), mientras que la Tercera Clase fue la más afectada (24.2%).

Factores Combinados: Una mujer de tercera clase tenía más probabilidades de sobrevivir que un hombre de primera clase, lo que indica que el género fue un factor más determinante que el nivel económico.

Tamaño Familiar: Las personas que viajaban en familias pequeñas (2-4 miembros) sobrevivieron más que las que viajaban solas o en familias muy grandes.

🧹 Proceso de Limpieza de Datos
El dataset original presentaba varios desafíos de calidad que fueron resueltos:

Gestión de Nulos:


Edad (Age): Se imputaron los valores faltantes usando la mediana según el título del pasajero (Mr, Mrs, Miss, etc.), ya que es más robusta frente a valores atípicos que la media.


Cabina (Cabin): Al faltar el 77% de los datos, se creó la variable binaria HasCabin (Tiene/No tiene cabina) para rescatar la información útil.

Embarque (Embarked): Se completaron los 2 valores faltantes con la moda (puerto 'S' - Southampton).

Ingeniería de Variables (Feature Engineering):


Title: Extraído del nombre del pasajero.


FamilySize: Suma de hermanos, cónyuges, padres e hijos.


AgeGroup: Categorización en Niños, Adolescentes, Adultos y Mayores.


Detección de Anomalías: Se verificó que no existieran edades o tarifas negativas y se identificaron tarifas extremadamente altas (>300 libras) como posibles outliers.

🚀 Función Reutilizable: limpiar_titanic()
Se desarrolló un pipeline de limpieza automatizado que permite transformar el dataset crudo en uno listo para modelos de Machine Learning en un solo paso.

Python
# Ejemplo de uso:
df_limpio = limpiar_titanic(df_original)
Acciones de la función:

Extrae títulos y crea grupos de edad.

Imputa valores nulos automáticamente.

Elimina columnas irrelevantes (PassengerId, Name, Ticket, Cabin).
