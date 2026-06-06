# ================== CROSS JOIN =================
Создает все возможные комбинации из двух таблиц

ментора
id          name
1           Актан
2           Асан


курсы
id          courses_name
1           SQL
2           Python
3           DS


результат
ментор      курсы
Актан       SQL
Актан       Python
Актан       DS
Асан        SQL
Асан        Python
Асан        DS

2 * 3 = 6

# Синтаксис
    SELECT * FROM <table1>
    CROSS JOIN <table2>;

# Пример
    SELECT * FROM mentors
    CROSS JOIN courses;



# ================= SELF JOIN ================
соединение сама с собой

# Синтаксис
    SELECT */(column_names) FROM <table>
    SELF JOIN <table>
    ON conditions;


# Пример
    SELECT * FROM employees
    LEFT JOIN employees AS m
    ON employees.id = m.manager_id


# =================== UPDATE с JOIN ===============
Иногда обновлять данные одной таблицы приходится делать на основании другой таблицы


# Пример
    UPDATE courses AS c
JOIN mentors AS m
ON c.mentor_id = m.id
SET c.price = c.price * 1.1
WHERE m.salary > 20000;



# ============== DELETE с JOIN ============
Удалять строки по данным другой таблицы


# Пример
    DELETE c
    FROM courses as c
    JOIN mentors as m
    ON c.mentor_id = m.id
    WHERE salary <= 10000;



# Удалить курсы менторов у которых зарплата ниже среднего



# ====== Рекурсия с JOIN ===========\
это когда запрос обращается к результату собственного выполнения

# Синтаксис
    WITH RECURSIVE cte AS (
        -- начальная выборка
        SELECT .....

        UNION ALL

        -- рекурсивня часть
        SELECT ....
    )
    SELECT * FROM cte


almaz - 1
asan - 2
aktan - 2
aiana - 3
asyl - 3