from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col

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
    print(f"Длина сводной таблицы составила {parsed_len} записей")

finally:
    # Гарантированное завершение сессии
    spark.stop()
    print("Spark сессия остановлена")