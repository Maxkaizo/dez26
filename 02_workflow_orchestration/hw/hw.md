# Question 1

- Question 1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

- Answer: 128.3 MiB

```bash
maxkaizo@max:~/tmp$ ls -lash yellow_tripdata_2020-12.csv 
129M -rw-r--r-- 1 maxkaizo maxkaizo 129M Jul 14  2022 yellow_tripdata_2020-12.csv
```


# Question 2. 

- What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

- Answer: green_tripdata_2020-04.csv

# Question 3

- How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

- Answer: 24648663

```bash

maxkaizo@max:~$ bq query --use_legacy_sql=false '
> SELECT COUNT(*)
FROM `dataeng-448500.dez26hw02.yellow_tripdata`
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020
> '
+----------+
|   f0_    |
+----------+
| 24648663 |
+----------+
```
