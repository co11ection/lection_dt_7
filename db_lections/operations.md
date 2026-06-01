#                                 IN
# Проверяет наличие значения в списке

WHERE age = 23
OR age = 24
OR age = 25

WHERE age IN (23, 24, 25)

# Синтаксис
WHERE column_name IN (value1, value2 .....)

# Пример
     SELECT * FROM students WHERE age IN (23, 24);
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


# NOT с IN
# Синтаксис
    WHERE column_name NOT IN (value1, value2 .....)

# Пример
    SELECT * FROM students WHERE age NOT IN (23, 24);
+----+------+------+----------------+
| id | name | age  | email          |
+----+------+------+----------------+
|  1 | Umar |   25 | umar@gmail.com |
|  7 | John |   25 | NULL           |
+----+------+------+----------------+

#                       LIKE
LIKE - нужен для поиска по схожести

# Синтаксис
    WHERE <column_name> LIKE "pattern"

# Спец символы LIKE
%                    любое колличество символов
_                    один любой символ

# Пример
    SELECT * FROM students WHERE name  LIKE 'J%';
+----+------+------+-------+
| id | name | age  | email |
+----+------+------+-------+
|  7 | John |   25 | NULL  |
+----+------+------+-------+

# как использовать _
    SELECT * FROM courses_list WHERE course_name  LIKE "___";
+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    3 | SQL         | 12000.00 |         1 |
+------+-------------+----------+-----------+


#                       NULL
# 1 Значение отсуствует
# 2 Данные не известны
# 3 Поле пустое

# ЗАПОМНИИИИИИИИИИ
NULl != 0
NULL != ''

# НЕ ПРАВИЛЬНО!!!!
    WHERE name = NULL

# Правильно
    WHERE name IS NULL


# Пример

    SELECT * FROM students WHERE email IS NULL;
+----+------+------+-------+
| id | name | age  | email |
+----+------+------+-------+
|  7 | John |   25 | NULL  |
+----+------+------+-------+

# WHERE name IS NOT NULL - Проверка на не пустая ли



#                   EXISTS
Проверяет существует ли строка в подзапросе

# Синтаксис
    WHERE EXISTS (
        subquery
    )

# Пример
    SELECT * FROM mentors AS m
    -> WHERE EXISTS (
    -> SELECT * FROM courses_list c
    -> WHERE c.mentor_id = m.id
    -> );
+----+--------+--------+-------------+------------------+
| id | name   | salary | phone       | email            |
+----+--------+--------+-------------+------------------+
|  1 | Aktan  |  55000 | +996969696  | aktan@gmail.com  |
|  2 | Nikita |  70000 | +9967777777 | nikita@gmail.com |
|  3 | Aidai  |  70000 | +996123123  | aidai@gmail.com  |
+----+--------+--------+-------------+------------------+



#                               UNION
Обьединяет результаты нескольких SELECT
При этом Типы данных должны быть совместимы

# Синтаксис

SELECT <column_name>/* FROM table1
UNION
SELECT <column_name>/* FROM table2

# Пример 
    SELECT name FROM students
    -> UNION
    -> SELECT name FROM mentors;
+-----------+
| name      |
+-----------+
| Umar      |
| Asan      |
| Aidar     |
| Aiana     |
| Nursultan |
| Diana     |
| John      |
| Almaz     |
| Sultan    |
| Aktan     |
| Nikita    |
| Aidai     |
| nurgazy   |
| Timur     |
+-----------+

# Особенность UNION: убирает дубликаты

#                   UNION ALL
# Отличие в том он не убирает дубликаты
    SELECT name FROM students UNION ALL SELECT name FROM mentors;
+-----------+
| name      |
+-----------+
| Umar      |
| Asan      |
| Aidar     |
| Aiana     |
| Nursultan |
| Diana     |
| John      |
| Almaz     |
| Sultan    |
| Sultan    |
| Sultan    |
| Aktan     |
| Nikita    |
| Aidai     |
| nurgazy   |
| Timur     |
+-----------+

UNION                   UNION ALL
дубликатов нету         дубликаты есть
медленнее               быстрее


#                               EXCEPT/ INTERSECT
# EXCEPT - Пока зывает строки (которые есть ы первом запросе но нет во втором)

(1, 2, 3, 4)
(3, 4, 5, 6)
(1, 2)

# Пример
    SELECT name FROM students EXCEPT SELECT name FROM mentors;
+-----------+
| name      |
+-----------+
| Asan      |
| Aidar     |
| Aiana     |
| Nursultan |
| Diana     |
| John      |
| Almaz     |
| Sultan    |
+-----------+

#  INTERSECT - Показывает общие строкки двух запросов
(1, 2, 3, 4)
(3, 4, 5, 6)
(3, 4)

# Пример:
    SELECT name FROM students INTERSECT SELECT name FROM mentors;
+------+
| name |
+------+
| Umar |
+------+


NOT