import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import min as spark_min, max as spark_max, mean as spark_mean
import time

# Configurações do Spark
spark = SparkSession.builder \
    .appName("OneBillionRowChallenge") \
    .getOrCreate()

filename = "data/generated/medicoes_1000000000.txt"

schema = StructType([
    StructField("station", StringType(), True),
    StructField("temperature", DoubleType(), True)
])

def create_df_with_pyspark(filename):
    df = spark.read.csv(filename, sep=";", schema=schema)
    aggregated_df = df.groupBy("station").agg(
        spark_min("temperature").alias("min"),
        spark_max("temperature").alias("max"),
        spark_mean("temperature").alias("mean")
    ).orderBy("station")
    return aggregated_df

if __name__ == "__main__":
    print("Iniciando o processamento do arquivo com PySpark.")
    start_time = time.time()
    df = create_df_with_pyspark(filename)
    df.show(10)
    took = time.time() - start_time
    print(f"PySpark Processing took: {took:.2f} sec")
    spark.stop()
