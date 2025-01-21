# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Table: Activity
# MAGIC
# MAGIC +----------------+---------+
# MAGIC | Column Name    | Type    |
# MAGIC +----------------+---------+
# MAGIC | machine_id     | int     |
# MAGIC | process_id     | int     |
# MAGIC | activity_type  | enum    |
# MAGIC | timestamp      | float   |
# MAGIC +----------------+---------+
# MAGIC The table shows the user activities for a factory website.
# MAGIC (machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
# MAGIC machine_id is the ID of a machine.
# MAGIC process_id is the ID of a process running on the machine with ID machine_id.
# MAGIC activity_type is an ENUM (category) of type ('start', 'end').
# MAGIC timestamp is a float representing the current time in seconds.
# MAGIC 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
# MAGIC The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
# MAGIC It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.
# MAGIC  
# MAGIC
# MAGIC There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.
# MAGIC
# MAGIC The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
# MAGIC
# MAGIC The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Activity table:
# MAGIC +------------+------------+---------------+-----------+
# MAGIC | machine_id | process_id | activity_type | timestamp |
# MAGIC +------------+------------+---------------+-----------+
# MAGIC | 0          | 0          | start         | 0.712     |
# MAGIC | 0          | 0          | end           | 1.520     |
# MAGIC | 0          | 1          | start         | 3.140     |
# MAGIC | 0          | 1          | end           | 4.120     |
# MAGIC | 1          | 0          | start         | 0.550     |
# MAGIC | 1          | 0          | end           | 1.550     |
# MAGIC | 1          | 1          | start         | 0.430     |
# MAGIC | 1          | 1          | end           | 1.420     |
# MAGIC | 2          | 0          | start         | 4.100     |
# MAGIC | 2          | 0          | end           | 4.512     |
# MAGIC | 2          | 1          | start         | 2.500     |
# MAGIC | 2          | 1          | end           | 5.000     |
# MAGIC +------------+------------+---------------+-----------+
# MAGIC Output: 
# MAGIC +------------+-----------------+
# MAGIC | machine_id | processing_time |
# MAGIC +------------+-----------------+
# MAGIC | 0          | 0.894           |
# MAGIC | 1          | 0.995           |
# MAGIC | 2          | 1.456           |
# MAGIC +------------+-----------------+
# MAGIC Explanation: 
# MAGIC There are 3 machines running 2 processes each.
# MAGIC Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
# MAGIC Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
# MAGIC Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC ### Run Time: </h3> 405 ms
# MAGIC <h3> Beats: </h3> 57.90%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC with start_cte as
# MAGIC (
# MAGIC     /* Select start activities */
# MAGIC     select machine_id, process_id, activity_type as activity_type_start, timestamp as time_start
# MAGIC     from Activity
# MAGIC     where activity_type='start'
# MAGIC     group by machine_id, process_id, activity_type, timestamp
# MAGIC ),
# MAGIC end_cte as
# MAGIC (
# MAGIC     /* Select end activities */
# MAGIC     select machine_id, process_id, activity_type as activity_type_end, timestamp as time_end
# MAGIC     from Activity
# MAGIC     where activity_type='end'
# MAGIC     group by machine_id, process_id, activity_type, timestamp
# MAGIC )
# MAGIC select t1.machine_id, round(sum(time_end - time_start) / count(t1.machine_id), 3) as processing_time
# MAGIC from start_cte t1
# MAGIC inner join end_cte t2
# MAGIC     on t1.machine_id = t2.machine_id and t1.process_id = t2.process_id
# MAGIC group by t1.machine_id
