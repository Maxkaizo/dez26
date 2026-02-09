# Preparation

External table creation:

![alt text](image.png)

materialized table creation:

![alt text](image-1.png)

# Question 1

- What is count of records for the 2024 Yellow Taxi Data?

- Answer: 20,332,093

``` sql
maxkaizo@max:~/dez26$ bq query --use_legacy_sql=false '
select count(1) from `dataeng-448500.dez26_hw_03.external_yellow_tripdata`;
'
+----------+
|   f0_    |
+----------+
| 20332093 |
+----------+
```

# Question 2

- What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table

![alt text](image-2.png)

 ![alt text](image-3.png)

 # Question 3

 - Why are the estimated number of Bytes different?

 - Answer: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

 ![alt text](image-4.png)

 ![alt text](image-5.png)