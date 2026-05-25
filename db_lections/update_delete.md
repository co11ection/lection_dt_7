#============================ UDATE DELETE===============
1 UPDATE - Команда созданные данные в таблице
Относится к DML

Базовый синтаксис:
    UPDATE <table name>
    SET column = value
    WHERE condition;

#!!!!!!!!!!!!!!!!!!
Важное правило:
Если не указать WHERE , изменятся  все строки в таблице

Изменение одной записи:
    UPDATE students
    -> SET age = 23
    -> WHERE id = 1;

Изменение нескольких записей:
    UPDATE students
    -> SET
    -> name = 'Umar',
    -> email = 'umar@gmail.com'
    -> WHERE id = 1;

Изменение с условием имени:
    UPDATE students 
    -> SET age = 24
    -> WHERE name = 'John';

Массовое обновление:
    UPDATE students
    -> SET age = age + 1;

Обновление с несколькими условиями
    UPDATE students
    -> set email = 'almaz@gmail.com'
    -> WHERE name = 'Almaz'
    -> AND id = 8;


Типичные частые ошибки
нет WHERE - изменяется все строки
Не правильное условие - обновляются не те данные
Не правильный тип данных - ошибки типов данных

Очень важная правктика
сначала Select и только после него делаем UPDATE

######################################################
-------------------- Delete -------------------------
DELETE - Команда для удаления строки из таблицы

Синтаксис:
    DELETE FROM <table name>
    WHERE condition;

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ГЛАВНОЕ ПРАВИЛО!!!!!!!!!!!!!!!!!!!!!!!!
Если не прописать WHERE и условие, то удалятся все данные

Удаление одной записи(по id):
    DELETE FROM students
    -> WHERE id = 15;

Удаление с несколькими условиями:
     DELETE FROM students
    -> WHERE id = 14
    -> and name = 'Almaz';

Удаление нескольки строк
    DELETE FROM students
    -> WHERE age < 18 ;

Очистка таблицы
    DELETE FROM students;

Удаление таблицы 
    DROP TABLE <table name>;

DELETE                              DROP
удаляет даннные                     удаляет всю таблицу или базу данных
структура остается                  структура полностью удаляется
Можно использовать WHERE            WHERE не используется


# Дубликаты
Поиск Дубликатов
    SELECT email, COUNT(*) as total
    -> FROM students
    -> GROUP BY email
    -> HAVING COUNT(*) > 1;
+------------------+-------+
| email            | total |
+------------------+-------+
| sultan@gamil.com |     2 |
+------------------+-------+

# GROUP BY - Групирует одинаковые значения
# COUNT(*) - считает колличество строк
# HAVING - фильтр для групп

Удаление дубликатов
    mysql> DELETE FROM students
    -> WHERE id NOT IN (
    -> SELECT min_id FROM(
    -> SELECT MIN(id) as min_id
    -> FROM students
    -> GROUP BY email
    -> ) AS temp
    -> );
Query OK, 1 row affected (0.022 sec)

mysql> select * from students;
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
|  9 | Sultan    |   23 | sultan@gamil.com    |
+----+-----------+------+---------------------+
Что делает внутренний запрос:
    -> SELECT MIN(id) as min_id
    -> FROM students
    -> GROUP BY email
Оставил минимальное id для каждого email

Внешний DELETE - удалил остальные записи которые не входят в условия



===================== Практика =====================

1) Изменить возраст студента под id 7 на 22  \/
2) Удалить студента под email  nursultan@gmail.com
3) Создать дубликаты, Найти дубликаты, Удалить дубликаты
