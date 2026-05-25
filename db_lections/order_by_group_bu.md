=================== ORDER BY ========
сортировка результата запроса
# ORDER BY - зачастую его пишут в конце запроса
# Синтаксис:
    SELECT columns/* 
    FROM TABLE
    ORDER BY column;

# Пример:
    mysql> SELECT * FROM students ORDER BY age;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  9 | Sultan    |   23 | sultan@gamil.com    |
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  8 | Almaz     |   24 | almaz@gmail.com     |
|  1 | Umar      |   25 | umar@gmail.com      |
|  7 | John      |   25 | john@gmail.com      |
+----+-----------+------+---------------------+
9 rows in set (0.002 sec)

# ASC - Сортировка по возрастанию
    SELECT * FROM students ORDER BY age ASC;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  9 | Sultan    |   23 | sultan@gamil.com    |
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  8 | Almaz     |   24 | almaz@gmail.com     |
|  1 | Umar      |   25 | umar@gmail.com      |
|  7 | John      |   25 | john@gmail.com      |
+----+-----------+------+---------------------+
# DESC - Сортировка по убыванию
    SELECT * FROM students ORDER BY age DESC;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  1 | Umar      |   25 | umar@gmail.com      |
|  7 | John      |   25 | john@gmail.com      |
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  8 | Almaz     |   24 | almaz@gmail.com     |
|  9 | Sultan    |   23 | sultan@gamil.com    |
+----+-----------+------+---------------------+

# Сортировка по нескольким полям
    SELECT * FROM <table name> ORDER BY <column name1> ASC, <column_name2> DESC;
# Пример
    SELECT * FROM students ORDER BY age ASC, name DESC;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  9 | Sultan    |   23 | sultan@gamil.com    |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  2 | Asan      |   24 | asan@gmail.com      |
|  8 | Almaz     |   24 | almaz@gmail.com     |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  1 | Umar      |   25 | umar@gmail.com      |
|  7 | John      |   25 | john@gmail.com      |
+----+-----------+------+---------------------+

#                        LIMIT    /    TOP    / FETCH

# LIMIT - огроничение строк в результате
# Синтаксис:
    SELECT * FROM <table_name> LIMIT <count of data>;
# Пример
    SELECT * FROM students LIMIT 3;
+----+-------+------+-------------------+
| id | name  | age  | email             |
+----+-------+------+-------------------+
|  1 | Umar  |   25 | umar@gmail.com    |
|  2 | Asan  |   24 | asan@gmail.com    |
|  3 | Aidar |   24 | aidar00@gmail.com |
+----+-------+------+-------------------+

# LIMIT с помощью сортировки:
    SELECT * FROM mentors ORDER BY salary DESC LIMIT 2;
+----+--------+--------+-------------+------------------+
| id | name   | salary | phone       | email            |
+----+--------+--------+-------------+------------------+
|  2 | Nikita |  70000 | +9967777777 | nikita@gmail.com |
|  3 | Aidai  |  70000 | +996123123  | aidai@gmail.com  |
+----+--------+--------+-------------+------------------+

# LIMIT с пропуском строк
# Синтвксис:
    LIMIT offset, count_of_data
    offset - колличество данных которые надо пропустить
    count_of_data - колличество данных которые нало получить
# Пример:
    SELECT * FROM mentors LIMIT 2, 3;
+----+---------+--------+--------------+-------------------+
| id | name    | salary | phone        | email             |
+----+---------+--------+--------------+-------------------+
|  3 | Aidai   |  70000 | +996123123   | aidai@gmail.com   |
|  4 | nurgazy |  70000 | +99645342324 | nurgazy@gmail.com |
|  5 | Timur   |  60000 | 99611111111  | tima@gmail.com    |
+----+---------+--------+--------------+-------------------+

# TOP - только в SQL серверах
    SELECT TOP <coun of data> * FROM <table name>;

# FETCH - PostgreSQL / ORACLE ...
    SELECT * FROM <table name> FETCH <count of data> ROW ONLY;


#                           DISTINCT
Уникальные значения\данные
# Синтаксис
    SELECT DISTINCT <column_name> FROM <table_name>;
# Пример:
    SELECT DISTINCT age FROM students;
+------+
| age  |
+------+
|   25 |
|   24 |
|   23 |
+------+
# DESTINCT по нескольким столбцам
# Синтаксис:
    SELECT DISTINCT <column_name1>, <column_name2> FROM <table_name>;
# Пример:
    SELECT DISTINCT age, name FROM students;
+------+-----------+
| age  | name      |
+------+-----------+
|   25 | Umar      |
|   24 | Asan      |
|   24 | Aidar     |
|   24 | Aiana     |
|   24 | Nursultan |
|   24 | Diana     |
|   25 | John      |
|   24 | Almaz     |
|   23 | Sultan    |
+------+-----------+

#                             GROUP BY и HAVING
1) Агрегатные функции - функция которая работает с группой строк
# Основные агрегатные функции
COUNT()  --------- считает колличество
SUM()  --------- сумирует
AVG()  --------- среднее
MIN() --------- минимум
MAX() ---------- максимум

# 1) COUNT
    SELECT COUNT(*) as total_students FROM students;
+----------------+
| total_students |
+----------------+
|             11 |
+----------------+

# 2) AVG
    SELECT AVG(salary) as avg_salary FROM mentors;
+------------+
| avg_salary |
+------------+
| 65000.0000 |
+------------+

# MAX
    SELECT MAX(salary) as max_salary FROM mentors;
+------------+
| max_salary |
+------------+
|      70000 |
+------------+

# MIN
    SELECT MIN(salary) as min_salary FROM mentors;
+------------+
| max_salary |
+------------+
|      50000 |
+------------+

# SUM
    SELECT SUM(salary) as sum_salary FROM mentors;
+------------+
| sum_salary |
+------------+
|     325000 |
+------------+

# GROUP BY
обьеденяет данные\строки в группы
# Синтаксис:
    SELECT <column_name>, agregate_funtion 
    FROM <table name> GROUP BY <column_name>;
# Пример:
    SELECT age, COUNT(*) as total
    -> FROM students
    -> GROUP BY age;
+------+-------+
| age  | total |
+------+-------+
|   25 |     2 |
|   24 |     6 |
|   23 |     3 |
+------+-------+

#                   HAVING
Фильтрация групп после GROUP BY
# Разница  WHERE               HAVING
        фильтрует строки        фильтрует группы
        до GROUP BY             после GROUP BY


# Пример
    SELECT age, COUNT(*) as total FROM students GROUP BY age HAVING COUNT(*) > 2;
+------+-------+
| age  | total |
+------+-------+
|   24 |     6 |
|   23 |     3 |
+------+-------+

SELECT salary, COUNT(*) as total from mentors GROUP BY salary HAVING salary > 60000;
+--------+-------+
| salary | total |
+--------+-------+
|  70000 |     3 |
+--------+-------+


Вывести возраст студентов и колличество по каждому возрасту
студенты должны быть старше 23
показать только те группы в которых колличество больше 2
отсортировать результат по колличеству студентов по убыванию

# Правильно, но сжирает много ресурсов
select age, count(*) as total 
from students 
group by age having age > 23 and total > 2 
order by age desc;

# Правильно, не сжирает много ресурсов
SELECT  age, COUNT(*) as total 
    -> FROM students 
    -> WHERE age > 23
    -> GROUP BY age HAVING total > 2
    -> ORDER BY total DESC;
