from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, avg, stddev

# Создаем Spark сессию с настройкой временной директории
spark = SparkSession.builder \
    .appName("Customs Data Analysis") \
    .config("spark.local.dir", "/tmp/spark-temp") \
    .getOrCreate()

try:
    df = spark.read.csv(
        "/home/alex/pyspark/data/customs_data.csv",
        sep=";",
        header=True,
        inferSchema=True
    )

    df.printSchema()
    parsed = df.groupBy("country").count().orderBy(col("count").desc()).show()
    parsed_len = df.groupBy("country").count().orderBy(col("count").desc()).count()
    print(f"Длина сводной таблицы country | count составила {parsed_len} записей")

    df.agg(avg("netto"), stddev("netto")).show()

finally:
    # Гарантированное завершение сессии
    spark.stop()
    print("Spark сессия остановлена")