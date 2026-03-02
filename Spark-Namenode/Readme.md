Descripción de la práctica

En esta práctica se ha trabajado con un entorno distribuido basado en Hadoop HDFS y Apache Spark utilizando contenedores Docker.

El objetivo principal ha sido:

Aprender a gestionar archivos en HDFS mediante el NameNode.

Ejecutar scripts de Spark sobre datos almacenados en HDFS.

Procesar datasets mediante DataFrames, SQL y UDFs.

Generar resultados distribuidos almacenados nuevamente en HDFS.

El entorno utilizado combina:

Hadoop (HDFS)

Apache Spark

Docker Compose

1. Arranque del entorno

Nos situamos en el directorio del proyecto:

cd docker-hadoop-spark

Levantamos los contenedores:

docker compose up -d

Este comando se ejecuta para asegurar que todos los servicios estén activos.

2. Acceso al NameNode (cliente HDFS)

Entramos al contenedor del NameNode:

docker-compose exec namenode bash

Importante: todos los comandos HDFS comienzan siempre por:

hdfs dfs -
3. Crear estructura en HDFS

Creamos el directorio de entrada:

hdfs dfs -mkdir -p /user/root/input
4. Subir archivos a HDFS

Subimos el dataset al sistema distribuido:

hdfs dfs -put /home/alturasRev.csv /user/root/input/
5. Comprobación de archivos

Listamos usuarios disponibles:

hdfs dfs -ls /user

Comprobamos que el archivo se ha subido correctamente:

hdfs dfs -ls /user/root/input
6. Enviar scripts a Spark

Copiamos el script Python al contenedor Spark:

docker cp C:\Users\ia\Desktop\Spark\script.py spark-master:/tmp/{NOMBRE_ARCHIVO}.py

Accedemos al contenedor Spark:

docker exec -it spark-master bash

Ejecutamos el programa:

/spark/bin/spark-submit /{RUTA}/{NombreArchivo}.py
7. Comprobación de resultados en HDFS

Reiniciamos NameNode si es necesario y verificamos la salida:

hdfs dfs -ls /user/root/output/alturas

Mostrar contenido generado:

hdfs dfs -cat /user/root/output/alturas/*
Ejercicios realizados
Caso 1 — DataFrames (Alturas)
Objetivo

Procesar el fichero alturasRev.csv y calcular la altura media por sexo.

Pasos realizados

Lectura del CSV desde HDFS.

Inferencia automática del esquema.

Limpieza de datos:

Eliminación de valores vacíos.

Eliminación de alturas negativas.

Corrección de unidades (metros a centímetros).

Agrupación por sexo.

Cálculo de la media.

Operaciones Spark utilizadas

read.csv

where

withColumn

when

groupBy

agg

avg

Resultado

Se genera un CSV en:

/user/root/output/alturas
Caso 2 — Uso de UDF
Objetivo

Reemplazar la lógica condicional (when) mediante una User Defined Function.

Pasos

Creación de función personalizada.

Registro de la UDF.

Aplicación sobre columnas del DataFrame.

Ventajas

Código más limpio.

Reutilización de lógica.

Mayor legibilidad.

Caso 3 — Spark SQL
Objetivo

Calcular la altura media utilizando consultas SQL.

Pasos

Convertir DataFrame en vista temporal:

df.createOrReplaceTempView("alturas")

Ejecutar consulta SQL:

spark.sql("SELECT sexo, AVG(altura) FROM alturas GROUP BY sexo")

Registrar la UDF para uso en SQL.

Caso 4 — DataSets (Ejercicios finales)

Se trabajó con distintos datasets aplicando transformaciones distribuidas.

Ejercicio Películas

Objetivos:

Crear clases para datasets.

Calcular nota media por usuario.

Determinar quién puntúa más alto.

Obtener películas mejor valoradas.

Operaciones utilizadas:

map

groupBy

avg

joins

Ejercicio Productos

Objetivos:

Obtener el cliente que más dinero gastó.

Generar informe total de productos vendidos.

Detectar productos nunca vendidos.

Analizar transacciones con mayor stock.

Conceptos aplicados:

joins

agregaciones

filtrado

Ejercicio Hoteles

Objetivos:

Filtrar hoteles pertenecientes a España.

Calcular ingresos asociados.

Obtener los hoteles con mayor beneficio.

Identificar ciudades con más ingresos.

Detectar hoteles sin ingresos.

Ejercicio Netflix

Objetivos:

Obtener el día con precio máximo.

Calcular media del precio de cierre.

Analizar máximo y mínimo volumen.

Generar estadísticas anuales y mensuales.

Convertir valores de USD a EUR mediante dataset externo.

Conceptos clave:

agregaciones temporales

joins por fecha

cálculos estadísticos

Arquitectura utilizada
Docker
 ├── Namenode (HDFS)
 ├── Datanode
 └── Spark Master
        └── Spark Jobs

Flujo de trabajo:

CSV Local → HDFS → Spark → Procesamiento → HDFS Output
Conceptos aprendidos

Funcionamiento de HDFS

Gestión de archivos en Hadoop

Spark DataFrames

Spark SQL

UDFs

Procesamiento distribuido

Ejecución de jobs Spark en Docker

Conclusión

Durante esta práctica se ha simulado un entorno Big Data real donde Hadoop gestiona el almacenamiento distribuido y Spark realiza el procesamiento de datos.

Se ha trabajado el flujo completo:

Subida de datos a HDFS

Procesamiento con Spark

Generación de resultados distribuidos
