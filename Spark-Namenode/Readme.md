# Big Data con Hadoop HDFS y Apache Spark
### Entorno distribuido con contenedores Docker

Repositorio de la práctica de procesamiento distribuido de datos utilizando **Hadoop HDFS** y **Apache Spark** sobre un entorno **Docker**.

---

## Entorno utilizado

| Tecnología | Rol |
|---|---|
| Hadoop HDFS | Almacenamiento distribuido |
| Apache Spark | Procesamiento de datos |
| Docker Compose | Orquestación de contenedores |

**Arquitectura:**
```
Docker
 ├── Namenode (HDFS)
 ├── Datanode
 └── Spark Master
        └── Spark Jobs
```

**Flujo de trabajo:**
```
CSV Local → HDFS → Spark → Procesamiento → HDFS Output
```

---

## Arranque del entorno

```bash
# Situarse en el directorio del proyecto
cd docker-hadoop-spark

# Levantar los contenedores
docker compose up -d
```

---

## Comandos principales

```bash
# Acceder al NameNode
docker-compose exec namenode bash

# Crear directorio en HDFS
hdfs dfs -mkdir -p /user/root/input

# Subir archivo a HDFS
hdfs dfs -put /home/alturasRev.csv /user/root/input/

# Verificar archivos subidos
hdfs dfs -ls /user/root/input

# Copiar script Python al contenedor Spark
docker cp C:\Users\ia\Desktop\Spark\script.py spark-master:/tmp/{NOMBRE_ARCHIVO}.py

# Acceder al contenedor Spark
docker exec -it spark-master bash

# Ejecutar script con Spark
/spark/bin/spark-submit /{RUTA}/{NombreArchivo}.py

# Ver resultados generados en HDFS
hdfs dfs -ls /user/root/output/alturas
hdfs dfs -cat /user/root/output/alturas/*
```

> Todos los comandos HDFS comienzan siempre por `hdfs dfs -`

---

## Ejercicios realizados

### Caso 1 — DataFrames (Alturas)
Procesamiento del fichero `alturasRev.csv` para calcular la **altura media por sexo**.

Operaciones aplicadas: `read.csv` · `where` · `withColumn` · `when` · `groupBy` · `agg` · `avg`

Limpieza realizada:
- Eliminación de valores vacíos
- Eliminación de alturas negativas
- Corrección de unidades (metros → centímetros)

Resultado almacenado en: `/user/root/output/alturas`

---

### Caso 2 — UDFs (User Defined Functions)
Reemplazo de la lógica condicional `when` por funciones personalizadas registradas como UDF, consiguiendo código más limpio, reutilizable y legible.

---

### Caso 3 — Spark SQL
Cálculo de la altura media mediante consultas SQL directamente sobre el DataFrame.

```python
df.createOrReplaceTempView("alturas")
spark.sql("SELECT sexo, AVG(altura) FROM alturas GROUP BY sexo")
```

---

### Caso 4 — Datasets (Ejercicios finales)

**Películas** — Nota media por usuario, película mejor valorada y usuario que más puntúa. Operaciones: `map` · `groupBy` · `avg` · `joins`

**Productos** — Cliente con mayor gasto, informe de productos vendidos y productos sin ventas. Conceptos: `joins` · agregaciones · filtrado

**Hoteles** — Hoteles en España, ingresos asociados, ciudades con más ingresos y hoteles sin beneficio.

**Netflix** — Estadísticas de precios y volumen, agregaciones temporales y conversión USD → EUR mediante dataset externo. Conceptos: `joins` por fecha · cálculos estadísticos · agregaciones anuales y mensuales

---

## Lo aprendido

- Funcionamiento y gestión de HDFS
- Spark DataFrames, SQL y UDFs
- Procesamiento distribuido de datos
- Ejecución de jobs Spark dentro de Docker
- Flujo completo Big Data: ingesta → procesamiento → almacenamiento

---

*Práctica de Big Data | Hadoop HDFS + Apache Spark + Docker*
