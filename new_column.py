from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F

# Создаем Spark сессию
spark = SparkSession.builder \
    .appName("Customs Data Analysis") \
    .config("spark.local.dir", "/tmp/spark-temp") \
    .getOrCreate()

try:
    # 1. Загрузка данных
    df = spark.read.csv(
        "/home/alex/pyspark/data/customs_data.csv",
        sep=";",
        header=True,
        inferSchema=True
    )
    df_cached = df.cache()
    df_cached.filter(F.col("netto") > 10).show()
    df_with_netto_difference = df_cached.withColumn("netto_info", F.when(
        F.column("netto") > 10, F.lit("More then 10 points")        
    ).when(
        F.column("netto") < 10, F.lit("Less then 10 points")

    )).show()

finally:
    spark.stop()
    print("Spark сессия остановлена")

