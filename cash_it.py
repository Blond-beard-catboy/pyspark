from pyspark.sql import SparkSession
from pyspark.sql.types import *

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
    print(f"Количество строк: {df.count()}")
    n = 10
    print(f"Первые {n} строк:")
    df.show(n, truncate=False)
    df.cache()
    print("Данные кэшированы!\n")
    

finally:
    # Гарантированное завершение сессии
    spark.stop()
    print("Spark сессия остановлена")