from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, IntegerType, TimestampType, DoubleType

spark = SparkSession.builder \
    .appName("JSON Data Analysis") \
    .getOrCreate()

# Определение схемы (аналогично CSV)
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

# Чтение JSON
df = spark.read.json(
    "/home/alex/pyspark/data/large_data.json",
    schema=schema
)

# Проверка данных
print("Схема данных:")
df.printSchema()

print("\nДанные:")
df.show(truncate=False)

spark.stop()