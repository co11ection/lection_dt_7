==================== INSERT ==================
Команда используется для добавление данных
относится к классу DML

Структура Insert:

    1) Если мы хотим заполнить частично, то указываем название колонок которые надо заполнить
    INSERT INTO <name of table> (name_column1, name_column2 ) 
    VALUE (value1, value2);
    Пример:
        INSERT INTO students (id, name, age, email)
        -> VALUE (3, 'Aidar', 20, 'aidar00@gmail.com');

    2) Если нам надо заполнить все поля
    INSERT INTO <name of table> 
    VALUE (value1, value2)
    Пример:
        INSERT INTO students 
        -> VALUE (4, 'Aiana', 21, 'aiana@gmail.com');
    3) Добавление нескольких данных одновременно
    INSERT INTO <name of table> (column1, column2)
    VALUES (value1, value2), (value3, value4);
    Пример:
        INSERT INTO students (id, name, age, email)
        -> VALUES (5, 'Nursultan', 27, 'nursultan@gmail.com'),
        -> (6, 'Diana', 23, 'diana@gmail.com'),
        -> (7, 'John', 40, 'john@gmail.com');

# Типичные ошибки при INSERT
1) Колонки не совпадают с колличеством значениий
Пример:
    INSERT INTO students (id, name, age, email) VALUE (8, 'Almaz', 30);
    ERROR 1136 (21S01): Column count doesn't match value count at row 1

2) Дубликаты PRIMARY KEY (id)
Пример:
    mysql> INSERT INTO students (id, name, age, email) VALUE (7, 'Almaz', 30, 'almaz@gmail.com');
    ERROR 1062 (23000): Duplicate entry '7' for key 'students.PRIMARY'

3) Неправильные типы данных
Пример:
    mysql> INSERT INTO students VALUE (8, 'Almaz', 'almaz@gmail.com', 30);
    ERROR 1366 (HY000): Incorrect integer value: 'almaz@gmail.com' for column 'age' at row 1
    INCORECT <data type> value: ......


============================= SELECT и фильтрации ========================
Команда для получения данных из таблицы

1) Получение всех данных:
    SELECT * FROM <table name>;
2) Получение одной колонки:
    SELECT  <name of column> FROM <table name>;
Пример:
    SELECT name FROM students;
+-----------+
| name      |
+-----------+
| Asan      |
| Asan      |
| Aidar     |
| Aiana     |
| Nursultan |
| Diana     |
| John      |
| Almaz     |
+-----------+
3) Получение нескольких колонок:
    SELECT  <name of column1>, <name of column2>  FROM <table name>;

Пример:
    SELECT id, name, age FROM students;
+----+-----------+------+
| id | name      | age  |
+----+-----------+------+
|  1 | Asan      |   22 |
|  2 | Asan      |   22 |
|  3 | Aidar     |   20 |
|  4 | Aiana     |   21 |
|  5 | Nursultan |   27 |
|  6 | Diana     |   23 |
|  7 | John      |   40 |
|  8 | Almaz     |   12 |
+----+-----------+------+

====================== Фильтрация ==============
WHERE - фильтрует строки(обьекты) по условию
Стурктура:
    SELECT column_name/* FROM <table_name>
    WHERE <condition>;
Пример:
    SELECT * FROM students WHERE age > 20;
+----+-----------+------+---------------------+
| id | name      | age  | email               |
+----+-----------+------+---------------------+
|  1 | Asan      |   22 | asan@gmail.com      |
|  2 | Asan      |   22 | asan@gmail.com      |
|  4 | Aiana     |   21 | aiana@gmail.com     |
|  5 | Nursultan |   27 | nursultan@gmail.com |
|  6 | Diana     |   23 | diana@gmail.com     |
|  7 | John      |   40 | john@gmail.com      |
+----+-----------+------+---------------------+

# Основные операторы
1) =  -> равно
2) != -> не равно
3) > -> больше
4) < -> меньше
5) >= -> больше или равно
6) <= -> меньше или равно

# Фильтрация строковы столбцов
    SELECT * FROM <table name> WHERE <str column> = <target>
Пример:
    SELECT * FROM students WHERE name = 'Asan';
+----+------+------+----------------+
| id | name | age  | email          |
+----+------+------+----------------+
|  1 | Asan |   22 | asan@gmail.com |
|  2 | Asan |   22 | asan@gmail.com |
+----+------+------+----------------+
2 rows in set (0.002 sec)


# Практика
1) Создать таблицу ментаров (id, name, salary, phone, email)
2) Записать с помощью множественного добавления как минимум 5 данных
3) провести фильтрацию salary, 
4) фильтр по строчным данным