# Question 1 

- pip version on `python:3.13` image

- Answeer: 25.3

``` bash
maxkaizo@max:~/dez26$ docker run -it --rm python:3.13 pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```
---

# Question 2

- postgress host and port

- Answer: db:5432

![alt text](images/image.png)

---
# Question 3

- Counting short trips

- Answer: 8007

``` sql
postgres@localhost:ny_taxi> SELECT
     count(1)
 FROM
     green_trips
 WHERE lpep_pickup_datetime >= '2025-11-01'
   AND lpep_pickup_datetime <  '2025-12-01'
   AND trip_distance <= 1
+-------+
| count |
|-------|
| 8007  |
+-------+
SELECT 1
Time: 0.032s
postgres@localhost:ny_taxi>

```
---

# Question 4

- Longest trip for each day

- Answer: 2025-11-14

``` sql
postgres@localhost:ny_taxi> SELECT
     CAST(lpep_pickup_datetime AS DATE) AS "day",
     MAX(trip_distance) AS max_distance
 FROM
     green_trips
 WHERE
     trip_distance < '100'
 GROUP BY
     "day"
 ORDER BY max_distance DESC
 LIMIT 5;
+------------+--------------+
| day        | max_distance |
|------------+--------------|
| 2025-11-14 | 88.03        |
| 2025-11-20 | 73.84        |
| 2025-11-23 | 45.26        |
| 2025-11-22 | 40.16        |
| 2025-11-15 | 39.81        |
+------------+--------------+
SELECT 5
Time: 0.040s
postgres@localhost:ny_taxi>
```
---

# Question 5

- Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025? 

- Answer: East Harlem North

``` sql
postgres@localhost:ny_taxi> SELECT
     z.zone,
     ROUND(SUM(t.total_amount)::numeric, 2) AS gt
 FROM 
     green_trips t
 JOIN taxi_zones z
     ON t.pulocationid = z.locationid
 WHERE t.lpep_pickup_datetime >= '2025-11-18'
   AND t.lpep_pickup_datetime <  '2025-11-19'
 GROUP BY
     z.zone
 ORDER BY
     gt desc
 LIMIT
     5;
+--------------------------+---------+
| zone                     | gt      |
|--------------------------+---------|
| East Harlem North        | 9281.92 |
| East Harlem South        | 6696.13 |
| Central Park             | 2378.79 |
| Washington Heights South | 2139.05 |
| Morningside Heights      | 2100.59 |
+--------------------------+---------+
SELECT 5
Time: 0.131s
postgres@localhost:ny_taxi>
```
---

# Question 6

- For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip? 

- Answer: Yorkville West

``` sql
 postgres@localhost:ny_taxi> SELECT
     zdo.zone, MAX(tip_amount) as top_tip
 FROM 
     green_trips t
 JOIN
     taxi_zones zpu ON t."pulocationid" = zpu."locationid"
 JOIN
     taxi_zones zdo ON t."dolocationid" = zdo."locationid"
 WHERE
     EXTRACT(MONTH FROM lpep_pickup_datetime) = 11
     AND EXTRACT(YEAR FROM lpep_pickup_datetime) = 2025
     AND zpu.zone = 'East Harlem North'
 GROUP BY
     zdo.zone
 ORDER BY
     top_tip DESC
 LIMIT 1;
+----------------+---------+
| zone           | top_tip |
|----------------+---------|
| Yorkville West | 81.89   |
+----------------+---------+
SELECT 1
Time: 1.447s (1 second), executed in: 1.442s (1 second)
```
---

# Question 7
