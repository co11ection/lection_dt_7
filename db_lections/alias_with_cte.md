#                      Псевдонимы 
Псевдонимы(Alias) - временные названия имен столбцов или таблиц

1) улучшает читабельность
2) короткие названия
3) кразивые результаты
4) работа с JOIN
5) работа с агрегаторами
6) работа с CTE

# Синтаксис:
    SELECT <column_name> AS <column_alias>
    FROM <table_name>;

# Пример:
    SELECT name AS students_name FROM students;
+---------------+
| students_name |
+---------------+
| Umar          |
| Asan          |
| Aidar         |
| Aiana         |
| Nursultan     |
| Diana         |
| John          |
| Almaz         |
| Sultan        |
| Sultan        |
| Sultan        |
+---------------+

# Псевдоним к нескольким столбцам
    SELECT name AS students_name,
    -> age AS students_age,
    -> email AS students_email
    -> FROM students;
+---------------+--------------+---------------------+
| students_name | students_age | students_email      |
+---------------+--------------+---------------------+
| Umar          |           25 | umar@gmail.com      |
| Asan          |           24 | asan@gmail.com      |
| Aidar         |           24 | aidar00@gmail.com   |
| Aiana         |           24 | aiana@gmail.com     |
| Nursultan     |           24 | nursultan@gmail.com |
| Diana         |           24 | diana@gmail.com     |
| John          |           25 | john@gmail.com      |
| Almaz         |           24 | almaz@gmail.com     |
| Sultan        |           23 | sultan@gamil.com    |
| Sultan        |           23 | sultan@gamil.com    |
| Sultan        |           23 | sultan@gamil.com    |
+---------------+--------------+---------------------+

# Псевдоним с агрегаторами
1) Без alias
     SELECT COUNT(*) FROM students;
+----------+
| COUNT(*) |
+----------+
|       11 |
+----------+
1 row in set (0.023 sec)
2) C Alias
    SELECT COUNT(*) AS total_students FROM students;
+----------------+
| total_students |
+----------------+
|             11 |
+----------------+

# Псевдоним таблиц
Используется:
    с JOIN
    сложных запросах
    CTE
    подзапросах

# Синтаксис
    SELECT <alias_table_name>.<column_name> 
    FROM <table_name> as <alias_table_name>

# Пример:
    SELECT s.name, s.age, s.email 
    -> FROM students AS s;
+-----------+------+---------------------+
| name      | age  | email               |
+-----------+------+---------------------+
| Umar      |   25 | umar@gmail.com      |
| Asan      |   24 | asan@gmail.com      |
| Aidar     |   24 | aidar00@gmail.com   |
| Aiana     |   24 | aiana@gmail.com     |
| Nursultan |   24 | nursultan@gmail.com |
| Diana     |   24 | diana@gmail.com     |
| John      |   25 | john@gmail.com      |
| Almaz     |   24 | almaz@gmail.com     |
| Sultan    |   23 | sultan@gamil.com    |
| Sultan    |   23 | sultan@gamil.com    |
| Sultan    |   23 | sultan@gamil.com    |
+-----------+------+---------------------+

#                                    WITH (CTE)

# CTE - Common Table Expression 
Временный результат запрома

# CTE: не сохраняется и существует только во время запроса

Создвется через: WITH

# Плюсы CTE:
    разбивать сложные запросы, на более мелкие
    делать запрос более чистым
    заменяет вложенные запросы
    возможность несколько раз использовать

# Базовый синтаксис:
WITH cte_name AS (
    select .....
)
SELECT * from cte_name;

# Пример:
    WITH adult_students AS   # - создалась временная таблица 
    ( SELECT  * 
    FROM students WHERE age > 23  # - фильтрация
    ) 
    SELECT * FROM adult_students; # - вытащили из временной таблицы данные
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  1 | Umar      |   25 | umar@gmail.com      |
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  7 | John      |   25 | john@gmail.com      |
|  8 | Almaz     |   24 | almaz@gmail.com     |
+----+-----------+------+---------------------+

# CTE с агрегатами
# Пример:
    WITH age_statistic AS ( SELECT age, 
    -> COUNT(*) AS total_students
    -> FROM students GROUP BY age
    -> )
    -> SELECT * FROM age_statistic;
+------+----------------+
| age  | total_students |
+------+----------------+
|   25 |              2 |
|   24 |              6 |
|   23 |              3 |
+------+----------------+


# Практика
Создать CTE менторов с зарплатой выше среднего

    WITH hight_avarage_mentors_salary AS ( # Создали временную таблицу
    -> SELECT * FROM mentors 
    -> WHERE salary > (  # Фильтрация
    -> SELECT AVG(salary)  # среднюю зарплату
    -> FROM mentors)
    -> )
    -> SELECT * FROM hight_avarage_mentors_salary; # вытаскиваем все данные с временной таблицы
+----+---------+--------+--------------+-------------------+
| id | name    | salary | phone        | email             |
+----+---------+--------+--------------+-------------------+
|  2 | Nikita  |  70000 | +9967777777  | nikita@gmail.com  |
|  3 | Aidai   |  70000 | +996123123   | aidai@gmail.com   |
|  4 | nurgazy |  70000 | +99645342324 | nurgazy@gmail.com |
+----+---------+--------+--------------+-------------------+