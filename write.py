def hdfs_example(**kwargs):
        spark = SparkSession.builder.appName("PySpark Example - Write Parquet").getOrCreate()
        data = [{
                'collumn1': 'A',
                'collumn2': 1
            }, {
                    'collumn1': 'B',
                    'collumn2': 2
            }, {
                    'collumn1': 'C',
                    'collumn2': 3
            }]
        df = spark.createDataFrame(data)
        df.show()
        df.write.mode('overwrite').parquet("hdfs://namenode:9000/user/hadoop/example1")
