# ================ INSERT ===================
Команда для добавления данных
относится к классу DML
# Структура:
    1) Если хотим заполнить частично, то указываем название колонок которые надо заполнить
    INSERT INTO <name of table> (<name of column1>, <name of column2>)
    VALUE (value1, value2);
    Пример:
        INSERT INTO students(id, name, age, email) VALUE (1, 'Ali', 25, 'ali@gmail.com');

    2) Если надо заполнить все поля
        INSERT INTO <name of table>
        VALUE (value1, value2);
    Пример:
        INSERT INTO students VALUE (2, 'asan', 17, 'asan@gmail.com');

    3)Добавление нескольуих данных
    INSERT INTO <name of table>  (<name of column1>, <name of column2>)
    VALUES (value1, value2), (value3, value4);
    Пример:
        INSERT INTO students (id, name, email, age)
    -> VALUES (3, 'Nurs', 'nurs@gmail.com', 34),
    -> (4, 'Almaz', 'almaz@gmail.com', 20);


# Типичные ошибки с INSERT
1) Колонки не совпадают с кол значений
    INSERT INTO students(id, name, age, email) VALUE (1, 'Ali', 25);
2) Дубликаты PRIMARY KEY (id)
3) Не правильные типы данных:
INSERT INTO students(id, name, age, email) VALUE (5, 'Ali', 'ali@gmail.com', 25);
ERROR 1366 (HY000): Incorrect integer value: 'ali@gmail.com' for column 'age' at row 1

