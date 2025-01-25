# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Movies
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | movie_id      | int     |
# MAGIC | title         | varchar |
# MAGIC +---------------+---------+
# MAGIC movie_id is the primary key (column with unique values) for this table.
# MAGIC title is the name of the movie.
# MAGIC  
# MAGIC
# MAGIC Table: Users
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | user_id       | int     |
# MAGIC | name          | varchar |
# MAGIC +---------------+---------+
# MAGIC user_id is the primary key (column with unique values) for this table.
# MAGIC The column 'name' has unique values.
# MAGIC Table: MovieRating
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | movie_id      | int     |
# MAGIC | user_id       | int     |
# MAGIC | rating        | int     |
# MAGIC | created_at    | date    |
# MAGIC +---------------+---------+
# MAGIC (movie_id, user_id) is the primary key (column with unique values) for this table.
# MAGIC This table contains the rating of a movie by a user in their review.
# MAGIC created_at is the user's review date. 
# MAGIC  
# MAGIC
# MAGIC Write a solution to:
# MAGIC
# MAGIC Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
# MAGIC Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Movies table:
# MAGIC +-------------+--------------+
# MAGIC | movie_id    |  title       |
# MAGIC +-------------+--------------+
# MAGIC | 1           | Avengers     |
# MAGIC | 2           | Frozen 2     |
# MAGIC | 3           | Joker        |
# MAGIC +-------------+--------------+
# MAGIC Users table:
# MAGIC +-------------+--------------+
# MAGIC | user_id     |  name        |
# MAGIC +-------------+--------------+
# MAGIC | 1           | Daniel       |
# MAGIC | 2           | Monica       |
# MAGIC | 3           | Maria        |
# MAGIC | 4           | James        |
# MAGIC +-------------+--------------+
# MAGIC MovieRating table:
# MAGIC +-------------+--------------+--------------+-------------+
# MAGIC | movie_id    | user_id      | rating       | created_at  |
# MAGIC +-------------+--------------+--------------+-------------+
# MAGIC | 1           | 1            | 3            | 2020-01-12  |
# MAGIC | 1           | 2            | 4            | 2020-02-11  |
# MAGIC | 1           | 3            | 2            | 2020-02-12  |
# MAGIC | 1           | 4            | 1            | 2020-01-01  |
# MAGIC | 2           | 1            | 5            | 2020-02-17  | 
# MAGIC | 2           | 2            | 2            | 2020-02-01  | 
# MAGIC | 2           | 3            | 2            | 2020-03-01  |
# MAGIC | 3           | 1            | 3            | 2020-02-22  | 
# MAGIC | 3           | 2            | 4            | 2020-02-25  | 
# MAGIC +-------------+--------------+--------------+-------------+
# MAGIC Output: 
# MAGIC +--------------+
# MAGIC | results      |
# MAGIC +--------------+
# MAGIC | Daniel       |
# MAGIC | Frozen 2     |
# MAGIC +--------------+
# MAGIC Explanation: 
# MAGIC Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
# MAGIC Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 434 ms
# MAGIC <h3> Beats: </h3> 94.71%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Write your T-SQL query statement below */
# MAGIC --PROCESS 1, 434 ms, 94.71 %
# MAGIC with cte1 as 
# MAGIC (
# MAGIC select t2.name as results, count(t1.user_id) as total
# MAGIC from MovieRating t1
# MAGIC left join Users t2
# MAGIC on t1.user_id = t2.user_id   
# MAGIC group by t2.name
# MAGIC )
# MAGIC , cte2 as(
# MAGIC     select round(sum(rating)*1.0/count(t1.movie_id),2) as av, title as results
# MAGIC from MovieRating t1
# MAGIC left join Movies t2
# MAGIC on t1.movie_id = t2.movie_id
# MAGIC where created_at between '2020-02-01' and '2020-02-29'
# MAGIC group by t1.movie_id, title
# MAGIC )
# MAGIC select top 1 results
# MAGIC from cte2
# MAGIC where av = (select max(av) from cte2)
# MAGIC union all
# MAGIC select top 1 results
# MAGIC from cte1
# MAGIC where total = (select max(total) from cte1)
# MAGIC order by results
# MAGIC -----------------------------------------------------------
# MAGIC --PROCESS 2  538 ms, 78.84%
# MAGIC -- SELECT t1.results FROM 
# MAGIC
# MAGIC -- (SELECT TOP 1 t1.user_id, t2.name as results, count(*) as total FROM MovieRating t1
# MAGIC -- LEFT JOIN Users t2 on t1.user_id = t2.user_id
# MAGIC -- GROUP BY t1.user_id, t2.name
# MAGIC -- ORDER BY total DESC, t2.name
# MAGIC -- ) as t1
# MAGIC
# MAGIC -- UNION ALL
# MAGIC
# MAGIC -- SELECT t2.results FROM 
# MAGIC -- (
# MAGIC
# MAGIC -- SELECT top 1 t1.movie_id,t2.title as results, avg(t1.rating*1.00) as avg_rating from MovieRating t1
# MAGIC -- INNER JOIN Movies t2 on t1.movie_id = t2.movie_id
# MAGIC -- WHERE left(created_at,7) = '2020-02'
# MAGIC -- GROUP BY t1.movie_id , t2.title
# MAGIC -- ORDER BY avg_rating   DESC , t2.title
# MAGIC -- ) as t2
# MAGIC
# MAGIC -- ORDER BY results
# MAGIC
# MAGIC
