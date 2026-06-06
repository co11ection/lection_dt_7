# =================== VIEWS ===========
Представление - это виртульная таблица, которая хранит SQL-запросы, но не данные

# Синтаксис
    CREATE VIEW course_info AS
    SELECT .....

    Как вытаскивать запрос чтобы отработал
    SELECT * FROM course_info;

# Преимущество: Упрощает сложные запросы и повторяющиеся запросы
# Безопасность, один раз запрос прописали и изпользуем много раз

# Создание VIEW
    CREATE VIEW <view_name> AS
    SELECT .....

# Пример:
    CREATE VIEW course_mentor_info AS
SELECT  c.courses_name,
c.price,
m.name AS mentor_name
FROM courses AS c
JOIN mentors AS m
ON c.mentor_id = m.id


# Создать VIEW совершеннолетних студентов

CREATE VIEW adult_students AS
SELECT * FROM students
WHERE age >=18

SELECT * FROM adult_students;


# Работа с VIEW

Выборка:
    SELECT * FROM <view_name>;

Сортировка:
    SELECT * FROM <view_name>
    ORDER BY age ASC/DESC;

Фильтрация:
    SELECT * FROM <view_name>
    WHERE conditions;

Агрегации:
    SELECT COUNT(*) FROM <view_name>;



#           Обновление VIEW

CREATE VIEW students_name AS
SELECT id, name
FROM students;


UPDATE students_name
SET name = "Samat"
WHERE id = 1;


SELECT * FROM students_name

SELECT * FROM students

# Когда VIEW обновляемый именно сами данные которые вытаскиваем
1) одна таблица
2) нет GROUP BY
3) нет DISTINCT
4) нет агрегатных функций


# Обновление самого запроса в VIEW
1) CREATE OR REPLACE ....
    CREATE OR REPLACE VIEW students_name AS
    SELECT *
    FROM students;

    # Просмотр
    SHOW CREATE VIEW students_name
    
    SELECT * FROM students_name

2) ALTER VIEW ......
    ALTER VIEW students_name AS
    SELECT id, name
    FROM students
    # Просмотр
    SELECT * FROM students_name



# INSERT с VIEW
    INSERT INTO students_name (name)
    VALUE ("Nurs")

    SELECT * FROM students_name

    SELECT * FROM students


# Переименование VIEW
courses_view - course_view
# Синтаксис
    RENAME TABLE <old_name>
    TO <new name>;
# Пример
    RENAME TABLE course_mentor_info
    TO courses_mentors_info

# ======= Удаление View ====== 

# Синтаксис
    DROP VIEW <view name>;

# Пример
    DROP VIEW courses_mentors_info

# Огроничения View
1) VIEW не хранит в себе данные
2) Сложные запросы работают медленнее
3) Не в каждый VIEW можно обновлять данные
4) при использования GROUP BY - VIEW открывается только для чтения


# ================= Практика ==========
CREATE VIEW mentors_courses_count AS
SELECT m.name,
    COUNT(c.id) AS courses_count
FROM  mentors as m 
JOIN courses as c 
ON c.mentor_id = m.id
GROUP BY m.name


SELECT * FROM mentors_courses_count