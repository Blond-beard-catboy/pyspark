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
    
    summary_p = df.limit(10000).toPandas()
    summary_df = spark.createDataFrame(summary_p)
    print(summary_p.head())
    print(summary_p.shape)
    summary_df.printSchema()
    summary_df.show()    

finally:
    spark.stop()
    print("Spark сессия остановлена")

