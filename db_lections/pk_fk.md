# ================== Priamary key Foreign Key ===============
name            age
ali             22
ali             23
ali             25

#   Ключ - это поле или набор нескольких полей, идентифицирует(обозначает)
# запись или обьект и связывает таблицы между собой


id          name        age
1           ali         22
2           ali         23
3           ali         25

# PRIMARY KEY - (первияный ключ ) это поле которое идентифицирует каждую запись

# Свойства:
1) уникален
2) не можеть NUll
3) в таблице не может быть PRIMARY KEY

CREATE TABLE students(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(100),
    -> email VARCHAR(100) UNIQUE,
    -> age INT);

DESC students;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | YES  |     | NULL    |                |
| email | varchar(100) | YES  | UNI | NULL    |                |
| age   | int          | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+


mysql> CREATE TABLE mentors( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(100), 
    salary INT, 
    phone VARCHAR(100) UNIQUE NOT NULL, 
    email VARCHAR(100) UNIQUE NOT NULL);

mysql> desc mentors;                                                                                            
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| name   | varchar(100) | YES  |     | NULL    |                |
| salary | int          | YES  |     | NULL    |                |
| phone  | varchar(100) | NO   | UNI | NULL    |                |
| email  | varchar(100) | NO   | UNI | NULL    |                |
+--------+--------------+------+-----+---------+----------------+


# FOREIGN KEY
это поле которое ссылается на PRIMARY KEY другой таблицы

+------+-------------+----------+-----------+
| id   | course_name | price    | mentor_id |
+------+-------------+----------+-----------+
|    1 | Python      | 15000.00 |         1 |
|    2 | Java        | 18000.00 |         2 |
|    3 | SQL         | 12000.00 |         1 |
|    4 | Frontend    | 20000.00 |         3 |
|    5 | Backend     | 22000.00 |         2 |
+------+-------------+----------+-----------+


+----+-------+--------+--------------+-----------------+
| id | name  | salary | phone        | email           |
+----+-------+--------+--------------+-----------------+
|  1 | Aktan |  15000 | 999663663636 | aktan@gmail.com |
|  2 | Asan  |  30000 | 9967736663   | asan@gmail.com  |
|  3 | almaz |  40000 | 9965534252   | almaz@gmail.com |
+----+-------+--------+--------------+-----------------+


# Пример создания
CREATE TABLE courses ( 
    id INT PRIMARY KEY AUTO_INCREMENT, 
    courses_name VARCHAR(100),
    price INT,
    mentor_id INT ,  
    FOREIGN KEY (mentor_id) 
    REFERENCES mentors(id)
);

mysql> DESC courses;                                                                                                       +--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | NULL    | auto_increment |
| courses_name | varchar(100) | YES  |     | NULL    |                |
| price        | int          | YES  |     | NULL    |                |
| mentor_id    | int          | YES  | MUL | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+


# Создать таблицу groups_table
# id, group_name, mentor_id

CREATE TABLE group_table(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> group_name VARCHAR(100),
    -> mentor_id INT,
    -> FOREIGN KEY (mentor_id)
    -> REFERENCES mentors(id));
Query OK, 0 rows affected (0.029 sec)

mysql> desc groups_table;
ERROR 1146 (42S02): Table 'courses.groups_table' doesn't exist
mysql> desc group_table;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| group_name | varchar(100) | YES  |     | NULL    |                |
| mentor_id  | int          | YES  | MUL | NULL    |                |
+------------+--------------+------+-----+---------+----------------+



# Типы связей

ONE-to-ONE - один к одному ---> пользователь - ИНН (в таблице которя привязывается)
ONE-to-MANY - один ко многим ----> Автор --- книги/ ментор - курсы.  (в таблице которя привязывается)
MANY -to- MANY -многие ко многим ---> студенты - курсы  (промежуточная таблица)
# MANY -to- MANY пример
CREATE TABLE students_courses (
    -> student_id INT,
    -> courses_id INT,
    -> 
    -> PRIMARY KEY (student_id, courses_id),
    -> FOREIGN KEY (student_id)
    -> REFERENCES students(id),
    -> FOREIGN KEY (courses_id)
    -> REFERENCES courses(id));
Query OK, 0 rows affected (0.039 sec)

mysql> desc students_courses;
+------------+------+------+-----+---------+-------+
| Field      | Type | Null | Key | Default | Extra |
+------------+------+------+-----+---------+-------+
| student_id | int  | NO   | PRI | NULL    |       |
| courses_id | int  | NO   | PRI | NULL    |       |
+------------+------+------+-----+---------+-------+

INSERT INTO students_courses(student_id, courses_id)
    -> VALUES (1, 2),
    -> (1, 3),
    -> (2, 1);
Query OK, 3 rows affected (0.006 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from students_courses;
+------------+------------+
| student_id | courses_id |
+------------+------------+
|          2 |          1 |
|          1 |          2 |
|          1 |          3 |
+------------+------------+