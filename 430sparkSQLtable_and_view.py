from __future__ import print_function
!echo $PYTHON_PATH
import os, sys
#import path
from pyspark.sql import *

# create spark sql session
myspark = SparkSession\
    .builder\
    .config("spark.executor.instances", 3 ) \
    .config("spark.executor.memory", "3g") \
    .config("spark.executor.cores", 2) \
    .config("spark.scheduler.listenerbus.eventqueue.size", 10000) \
    .config("spark.sql.parquet.compression.codec", "snappy") \
    .appName("Sample_07_kmeans") \
    .getOrCreate()



sc = myspark.sparkContext
print ( myspark)
myspark.sql("SET spark.sql.parquet.binaryAsString=true")
from pyspark.sql import HiveContext
hive_context = HiveContext(sc)
myview = hive_context.table("default.sample_07p")

myview.show(5)
