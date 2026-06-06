# =================== JOIN =======================
JOIN - это операция обьеденение таблиц по связанным поляи
# Синтаксис
    SELECT <name 0f column>/*
    FROM <table1>
    JOIN <table2>
    ON table1.column_name = table2.column_name;

# Пример
    SELECT * FROM courses AS c
    JOIN mentors AS m
    ON c.mentor_id = m.id LIMIT 100

#               INNER JOIN
1) возвращает только совпадающие данные(записи)

# Синтаксис
    SELECT <name 0f column>/*
    FROM <table1>
    INNER JOIN <table2>
    ON table1.column_name = table2.column_name;


# ================ RIGHT JOIN ==============
возвращает все данные с правой таблицы и совподение с левой таблицы
# Синтаксис
    SELECT * FROM table1
    RIGHT JOIN table2
    ON condition;

# Пример:
    SELECT * from courses AS c
    RIGHT JOIN mentors AS m
    ON c.mentor_id = m.id LIMIT 100


# ========= LEFT JOIN ============
ВОзвращается с левой таблицы все данные а с правоц только связанные данные
# Синтаксис
    SELECT * FROM table1
    LEFT JOIN table2
    ON condition;

# Пример:
    SELECT * from courses AS c
    LEFT JOIN mentors AS m
    ON c.mentor_id = m.id;


# ============ FULL OUTER JOIN ============
LEFT JOIN + RIGHT JOIN

ВОзвращает:
данные первой таблицы так и данные со второй таблицы 
так же возвращает совпадающие данные

# Пример
    SELECT * FROM courses AS c
    FULL OUTER JOIN mentors AS m
    ON c.mentor_id = m.id;  