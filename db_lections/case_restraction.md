# =======================    CASE    =========================
CASE - условная канструкция такая же как if/else но в SQL
# Синтаксис
    CASE
        WHEN <condition> THEN <result>
        WHEN <condition> THEN <result>
        ELSE <result>
    END


# Как работает
1) Проверяет условия сверху вних
2) Если условие выдает True возвращает результат
3) Если ничего не подошло то возвращает результат ELSE


# Пример
    SELECT name, age, 
    CASE
        WHEN age > 23 THEN 'adult' 
        ELSE 'child' 
    END AS age_category 
    from students;
+-----------+------+--------------+
| name      | age  | age_category |
+-----------+------+--------------+
| Umar      |   25 | adult        |
| Asan      |   24 | adult        |
| Aidar     |   24 | adult        |
| Aiana     |   24 | adult        |
| Nursultan |   24 | adult        |
| Diana     |   24 | adult        |
| John      |   25 | adult        |
| Almaz     |   24 | adult        |
| Sultan    |   23 | child        |
| Sultan    |   23 | child        |
| Sultan    |   23 | child        |
+-----------+------+--------------+


1) категори курсов:
    Cheap - ниже 15 000
    Medium - 15 000 и 20 000
    Expensive - все остальное

# Ответ
    SELECT course_name, price,
    CASE 
        WHEN price < 15000 THEN 'Cheap'
        WHEN price BETWEEN 15000 AND 20000 THEN 'Medium'
        ELSE 'Expensive'
    END AS category_courses
    FROM courses_list;
+-------------+----------+------------------+
| course_name | price    | category_courses |
+-------------+----------+------------------+
| Python      | 15000.00 | Medium           |
| Java        | 18000.00 | Medium           |
| SQL         | 12000.00 | Cheap            |
| Frontend    | 20000.00 | Medium           |
| Backend     | 22000.00 | Expensive        |
+-------------+----------+------------------+

# Категоризация данных
Разделение данных по группам
1) Аналитика
2) dashboards
3) CRM
4) финансы
5) отчеты


#  CASE + GROUP BY
    SELECT  
    CASE 
        WHEN age <= 18  THEN 'Child'
        WHEN age BETWEEN 20 AND 24 THEN 'Young'
        ELSE 'Adult'
    END as age_group ,
    COUNT(*) AS total 
    FROM students 
    GROUP BY age_group;
+-----------+-------+
| age_group | total |
+-----------+-------+
| Adult     |     2 |
| Young     |     6 |
| Child     |     3 |
+-----------+-------+

SELECT 
    CASE  
        WHEN price < 15000 THEN 'Cheap' 
        WHEN price BETWEEN 15000 AND 20000 THEN 'Medium' 
        ELSE 'Expensive' 
    END AS category_courses,
    COUNT(*) AS total_courses  
    FROM courses_list 
    GROUP BY category_courses;
+------------------+---------------+
| category_courses | total_courses |
+------------------+---------------+
| Medium           |             3 |
| Cheap            |             1 |
| Expensive        |             1 |
+------------------+---------------+

#               CASE + агрегатные функции
# синтаксис
SELECT
    агрегатная функция SUM, AVG, COUNT, MAX, MIN(
        CASE
            условия
        END
    ) 
# CASE + SUM
SELECT  
    SUM(
        CASE 
            WHEN price BETWEEN 15000 AND 20000 THEN 1 
            ELSE 0 
        END 
    ) AS cheap_courses 
FROM courses_list;
+---------------+
| cheap_courses |
+---------------+
|             3 |
+---------------+
# CASE + COUNT
SELECT 
    COUNT(
        CASE
            WHEN age > 19 THEN 1
        END
    ) AS adults
FROM students;
+--------+
| adults |
+--------+
|      8 |
+--------+



# ================================== Ограничения =====================
Правила для данных в таблиц
Ограничения                 Назначение
NOT NULL                    значение обязательное и не должно быть пустым
DEFAULT                     значение по умолчанию
UNIQUE                      уникальное значение
CHECK                       проверка условия

CREATE TABLE employes( 
    id INT, 
    email VARCHAR(100) NOT NULL UNIQUE, 
    full_name VARCHAR(100) NOT NULL,
    is_active BOOL DEFAULT true,
    age INT CHECK (age >=18)
);

