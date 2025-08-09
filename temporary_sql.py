from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, avg, stddev, count, round

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
    
    # 2. Регистрация DataFrame как временной таблицы
    df.createOrReplaceTempView("customs_data")
    
    # 3. Анализ с помощью SQL
    print("\nРезультаты SQL-запроса:")
    spark.sql("""
        SELECT country, COUNT(*) AS count
        FROM customs_data
        GROUP BY country
        ORDER BY count DESC
    """).show()
    
    # 4. Анализ с помощью DataFrame API
    print("\nРезультаты DataFrame API:")
    country_stats = df.groupBy("country").agg(count("*").alias("count"))
    country_stats_sorted = country_stats.orderBy(col("count").desc())
    country_stats_sorted.show()
    
    print(f"Количество уникальных стран: {country_stats.count()}")
    
    # 5. Анализ числовых столбцов
    stats_df = df.select(
    round(avg("netto"), 3).alias("avg_netto"),
    round(stddev("netto"), 3).alias("stddev_netto")#
    )
    print("\nСтатистика по столбцу 'netto' (округленная до 3 знаков):")
    stats_df.show()    
    
    # 6. Дополнительная диагностика
    print("\nСхема данных:")
    df.printSchema()

finally:
    spark.stop()
    print("Spark сессия остановлена")

