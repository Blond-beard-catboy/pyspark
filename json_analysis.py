from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("JSON Data Analysis") \
    .getOrCreate()

df = spark.read.json(
    "/home/alex/pyspark/data/large_data.json",
)

# Проверка данных
print("Схема данных:")
df.printSchema()

print("\nДанные:")
df.show(truncate=False)

spark.stop()