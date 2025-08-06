from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, IntegerType, TimestampType, DoubleType
from pyspark.sql.functions import col, count, when  # Добавлен импорт функций

spark = SparkSession.builder \
    .appName("Customs Data Analysis") \
    .config("spark.local.dir", "/tmp/spark-temp") \
    .getOrCreate()

# Определение схемы
schema = StructType([
    StructField("month", StringType(), True),
    StructField("country", StringType(), True),
    StructField("code", StringType(), True),
    StructField("value", DoubleType(), True),
    StructField("netto", LongType(), True),
    StructField("quantity", LongType(), True),
    StructField("region", IntegerType(), True),
    StructField("district", IntegerType(), True),
    StructField("direction_eng", StringType(), True),
    StructField("measure_eng", StringType(), True),
    StructField("load_date", TimestampType(), True)
])

try:
    # Загрузка с явной схемой
    df = spark.read.csv(
        "/home/alex/pyspark/data/customs_data.csv",
        sep=";",
        header=True,
        schema=schema,
        mode="PERMISSIVE",
        columnNameOfCorruptRecord="corrupt_record"
    )
    
    # Проверка данных
    total_count = df.count()
    print(f"Количество строк: {total_count}")
    print("\nСтруктура данных:")
    df.printSchema()
    print("\nПервые 5 записей:")
    df.show(5, truncate=False)
    # df.write.format("parquet").save("/home/alex/pyspark/data/customs_data.parquet")

except Exception as e:
    print(f"Ошибка: {str(e)}")
    # Вывод первых строк для диагностики
    sample_df = spark.read.csv(
        "/home/alex/pyspark/data/customs_data.csv",
        sep=";",
        header=True,
        inferSchema=False,
        nrows=5
    )
    print("\nПример данных (первые 5 строк):")
    sample_df.show(5, truncate=False)

finally:
    spark.stop()
    print("Spark сессия остановлена")