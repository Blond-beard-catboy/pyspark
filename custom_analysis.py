from pyspark.sql import SparkSession
from pyspark.sql.types import *

schema = StructType([
    StructField("month", StringType(), True),
    StructField("country", StringType(), True),
    StructField("load_date", TimestampType(), True)
])

# Создаем Spark сессию с настройкой временной директории
spark = SparkSession.builder \
    .appName("Customs Data Analysis") \
    .config("spark.local.dir", "/tmp/spark-temp") \
    .getOrCreate()

try:
    # Чтение данных
    # df = spark.read.csv(
    #     "/home/alex/pyspark/data/customs_data.csv",
    #     sep=";",
    #     header=True,
    #     inferSchema=True
    # )
    df = spark.read.schema(schema).csv("/home/alex/pyspark/data/customs_data.csv")
    
    # Анализ данных
    # print(f"Количество строк: {df.count()}")
    # df.printSchema()
    n = 10
    print(f"Первые {n} строк:")
    df.show(n, truncate=False)

finally:
    # Гарантированное завершение сессии
    spark.stop()
    print("Spark сессия остановлена")