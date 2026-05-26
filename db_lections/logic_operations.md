====================== Логические опреаторы ==========================

Базовы синтаксис WHERE:
    SELECT *\<column_names>
    FROM <table_name>
    WHERE condition;

Как работает WHERE:
    1) берет строки из таблицы
    2) проверяет на условие
    3) оставляет только подходящие


#                AND
# True and True = True
# False and True = False
Оператор AND требует, чтобы все условия True

# Синтаксис
    WHERE conditin1
    AND condition2

# Пример
    SELECT * FROM students WHERE age = 24 AND  name = 'Nursultan';
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  5 | Nursultan |   24 | nursultan@gmail.com |
+----+-----------+------+---------------------+

age = 24 -> True
                                + -> True
name = 'Nursultan' -> True


# Вытащить курсы дороже 15000 и где mentor_id = 2
    SELECT * FROM courses_list WHERE price > 15000 AND mentor_id = 2;
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    2 | Java        | 18000.00 |         2 |
|    5 | Backend     | 22000.00 |         2 |
+------+-------------+----------+-----------+


#                       OR
# True + True = True
# True + False = True
# False + False = False

# Хотябы одно условие должно выдать True

# Синтаксис:
    WHERE condition1
    OR condition2;

# Пример:
    SELECT * FROM students WHERE age = 24 OR name = 'John';
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  7 | John      |   25 | john@gmail.com      |
|  8 | Almaz     |   24 | almaz@gmail.com     |
+----+-----------+------+---------------------+

# Курсы дешевле 15000 или где mentor_id = 1
    SELECT * FROM courses_list  WHERE price < 15000 OR mentor_id = 1;
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    1 | Python      | 15000.00 |         1 |
|    3 | SQL         | 12000.00 |         1 |
+------+-------------+----------+-----------+


#                   NOT
True - превращает > False
False - превращает > True
# Синтаксис
    WHERE NOT contidion

# Пример
    SELECT * FROM students WHERE NOT age = 24;
+----+--------+------+------------------+
| id | name   | age  | email            |
+----+--------+------+------------------+
|  1 | Umar   |   25 | umar@gmail.com   |
|  7 | John   |   25 | john@gmail.com   |
|  9 | Sultan |   23 | sultan@gamil.com |
| 11 | Sultan |   23 | sultan@gamil.com |
| 12 | Sultan |   23 | sultan@gamil.com |
+----+--------+------+------------------+

    WHERE age != 24

# Вытащить либо курс назывался Python или цена ниже 20000 и ментор не равен 2
    SELECT  * FROM courses_list WHERE 
    -> (course_name = 'Python' OR price < 20000)
    -> AND NOT mentor_id = 2;
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    1 | Python      | 15000.00 |         1 |
|    3 | SQL         | 12000.00 |         1 |
+------+-------------+----------+-----------+

#                   BETWEEN
Проверяет диапазон (начало и конец)
# Синтаксис
    WHERE value/<column_name> BETWEEN min AND max

# Пример:
     SELECT * FROM students WHERE age BETWEEN 23 AND 24;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  2 | Asan      |   24 | asan@gmail.com      |
|  3 | Aidar     |   24 | aidar00@gmail.com   |
|  4 | Aiana     |   24 | aiana@gmail.com     |
|  5 | Nursultan |   24 | nursultan@gmail.com |
|  6 | Diana     |   24 | diana@gmail.com     |
|  8 | Almaz     |   24 | almaz@gmail.com     |
|  9 | Sultan    |   23 | sultan@gamil.com    |
| 11 | Sultan    |   23 | sultan@gamil.com    |
| 12 | Sultan    |   23 | sultan@gamil.com    |
+----+-----------+------+---------------------+

23<= age <= 24

# Вытащить курсы цены которых между 15 000 и 30 000 
     SELECT * FROM courses_list WHERE price BETWEEN 15000 AND 30000;
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    1 | Python      | 15000.00 |         1 |
|    2 | Java        | 18000.00 |         2 |
|    4 | Frontend    | 20000.00 |         3 |
|    5 | Backend     | 22000.00 |         2 |
+------+-------------+----------+-----------+

# BETWEEN с использованием NOT
# Синтаксис:
    WHERE value/<column_name> NOT BETWEEN min AND max

# Пример 
    SELECT * FROM students WHERE age NOT BETWEEN 23 AND 24;
+----+------+------+----------------+
| id | name | age  | email          |
+----+------+------+----------------+
|  1 | Umar |   25 | umar@gmail.com |
|  7 | John |   25 | john@gmail.com |
+----+------+------+----------------+


#                           ANY
True, если хотябы совподает один подзапрос

# Синтаксис 
    WHERE value/<column_name> > ANY (
        subquery
    )

# Пример
    SELECT * FROM courses_list WHERE price > ANY( SELECT price FROM courses_list WHERE mentor_id = 3);
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    5 | Backend     | 22000.00 |         2 |
+------+-------------+----------+-----------+

#                           ALL
True, толькко если подходит ко всем условиям подзапроса

# Синтаксис
    WHERE value/column_name > ALL(
        subquery
    )



# ALL и ANY - работают почти всегда с подзапросам


# Частые ошибки
1) Путаница между AND и OR
2) Отсуствие скобок   -> неожиданный результат
3) BETWEEN наоборот - min - max -> max - min
4) ANY/ALL без подзапросов - Ошибка синтаксиса
5) Пропусккают NOT 
6) писать сложные условия не поэтапно