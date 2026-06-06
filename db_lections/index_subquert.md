# =========== INDEX ==============

id          name
1           Ali
2           Aktan
3           Asan
...
6000        Nurs
10000       Aman

Select * FROM students WHERE name = "Nurs"
Без индекса SQL будет проверять каждую строку одну за другой

# Индекс специальная структура данных успоряющая поиск записей

Индексация накидывается не на все поля(стобцы)
PRYMARY KEY, UNIQUE - можем накидывать INDEX



# Создание индексов

# Синтаксис:
    CREATE INDEX index_name
    ON table_name(column_name)

# Пример:
    CREATE INDEX idz_students_email
    ON students(email);


# Состовной INDEX
Можете индексировать несколько полей разом

CREATE INDEX indx_name_age
ON students(name, age)


# Уникальные индексы
Запрещает повторяющиеся значения

Email - долден быть уникальным

CREATE UNIQUE INDEX indx_unique_email
ON students(email);

                        PRIMARY KEY             UNIQUE
уникальность                да                     да
NULL                        нельзя                можно
Колличество                   1                 несколько


# Просмотр Индексов
    SHOW INDEX
    FROM students;


# Удаление индексов
#   Синтаксис
        DROP INDEX index_name
        ON table_name;

#   Пример
    DROP INDEX idz_students_email
    ON students;


# EXPLAIN
Показывает выполнение запроса
# Синтаксис
    EXPLAIN 
    тело запроса

# Пример:
    EXPLAIN
SELECT * FROM students
WHERE email = "ali31@gmail.com"


type = ref/const - Используется индексацияъ
type = ALL - Индексов нету


# ================ Подзапросы =================

внешний запрос (
    внутренний под запрос
)
WHERE, IN, JOIN

# Найти курсы дороже средней цены

SELECT * FROM courses
WHERE price > (
    SELECT AVG(price) FROM courses
)

# Найти курсы менторов выше 15000
Подсказка
IN

SELECT * FROM courses
WHERE mentor_id IN(
    SELECT id FROM mentors
    WHERE salary > 15000
)


