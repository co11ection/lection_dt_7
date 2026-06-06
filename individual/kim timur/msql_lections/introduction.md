#                   База данных 
База данных - хранилище где хранится определенная информация
СУБД - Система управления базами данных (Mysql, PostgreSQL, MongoDB)
SQL (Structured query language) - язык для работы с базами данными
с помощью SQL:
    1) Создавать(бд, таблицы данные таблицы)
    2) обновлять
    3) Просмотреть
    4) удалять


# ============== Типы данных =================
Числовые = INT, BIGINT, DECIMAL, FLOAT
# ---------------------------------------
строчные - CHAR(255), VARCHAR(255), TEXT(без ограничений)
CHAR(100) = 'hello                                           ' - остаток заполнит пробелами
VARCHAR(100) = 'hello' - лишнее отрезает

name - VARCHAR
description - TEXT
dockument_field_description - CHAR
# ------------------------------------------
буулевые - BOOL = true/false
is_admin - BOOL = true/false
# ------------------------------------------
дата и время - DATE (дата), TIME (время), DATETIME(дата и время)
birth_day - DATE
created_at - DATETIME
start/finish - TIME

# ================= SQL - операторы и классы команд  =================
ВСЕ КОМАНДЫ ПИСАТЬ КАПСОМ (БОЛЬШИМИ БУКВАМИ)

# DDL - data definition language
Команды для создания и изменения базы данных и работой с ним
Команды
CREATE - создать
ALTER - изменить
DROP - удалить
RENAME - переименовать
TRUNCATE - очистка таблицы
===============================================
DML - DATA MANIPULATION LANGUAGE
команды для работы с самими данными
INSERT -> Добавить 
UPDATE -> обновить
DELETE -> удалить
==============================================
DQL - DATA QUERY LANGUAGE
Команды для получения данных
SELECT - выборка данных(получение или отображение)
==================================================
DCL - data control language
команда для управление правами доступа
GRANT - выдать права
REVOKE - забираем права
================================================
TCL - transaction control language
Команда для управления транзакциями (все, либо ничего)

COMMIT - сохранение изменений
ROLLBACK - отмена изменений
SAVEPOINT - точка сохранения

=====================================================
# ---------------- Работа с бд --------------------

# Открыть
    для винды открыть MYSQL COMMAND LINE CLIENT
    на маке/линукс - прописать в терминале msql -u <username/root> -p
# Закрыть 
    \q

# Посмотреть какие БД/таблицы существуют
    SHOW DATABASES;
    SHOW TABLES;

# Создать базу данных
    CREATE DATABASE <name of db>;

# Подключение к базе данных
    USE <name of db>;

# удаление базы данных 
    DROP DATABASE <name of db>;

# Создание таблицы
# структура
    CREATE TABLE <name of table>(
        <name of column> <description_of_column>
    )

# Пример
    CREATE TABLE students (
    -> id INT PRIMARY KEY,
    -> name VARCHAR(100),
    -> age INT,
    -> email VARCHAR(100)
    -> );
ERROR 1046 (3D000): No database selected
mysql> USE courses1
Database changed
mysql> CREATE TABLE students ( id INT PRIMARY KEY, name VARCHAR(100), age INT, email VARCHAR(100) );
Query OK, 0 rows affected (0.028 sec)

mysql> SHOW TABLES
    -> ;
+--------------------+
| Tables_in_courses1 |
+--------------------+
| students           |
+--------------------+

# Просмотр структуры таблицы
    DESC <name of table>;
    DESC students;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| id    | int          | NO   | PRI | NULL    |       |
| name  | varchar(100) | YES  |     | NULL    |       |
| age   | int          | YES  |     | NULL    |       |
| email | varchar(100) | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+

# Добавление данных (записей) в таблицу
    INSERT INTO <name of table> (<column_name1>) VALUE (value1);
# Пример
    INSERT INTO students(id, name, age, email) VALUE (1, 'Ali', 25, 'ali@gmail.com');
Query OK, 1 row affected (0.008 sec)

# Получение данных 
    SELECT  */column_name FROM <name of table>;
# Пример:
    SELECT * FROM students;
+----+------+------+---------------+
| id | name | age  | email         |
+----+------+------+---------------+
|  1 | Ali  |   25 | ali@gmail.com |
+----+------+------+---------------+

# Д\З
создать БД library
создать таблицу books
добавить как минимум 3 записи
Выполнить:
    SELECT
    UPDATE
    DELETE