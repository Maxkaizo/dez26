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