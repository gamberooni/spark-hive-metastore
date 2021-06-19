from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()

spark.sql("CREATE DATABASE testdb;")
spark.sql("CREATE TABLE testdb.testtable (id INT, name STRING, age INT);")