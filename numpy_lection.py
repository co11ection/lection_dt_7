#==============NumPy=============

#NumPy - это библиотека для быстрых вычислений с массивами (list, set, tuple)

# Почему не обычные списки Python

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# Numpy

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a+b)

# NumPy делает математику как в калькуляторе
# ndarray - n-dimensional array (многомерный массив)

# 1D - список [1, 2, 3]
# 2D - таблица [
#    [1, 2, 3],
#    [1, 2, 3]
# ]
# 3D - куб данных
# [
#    [1, 2, 3],
#    [1, 2, 3],
#    [1, 2, 3]
# ]

# 1D
a = np.array([1, 2, 3])
print(a)

#2D
a = np.zeros((2, 3))
print(a)

a = np.zeros((2, 10))
# 3D

a = np.zeros((3, 10))
print(a)

#Афтоматические функции
print(np.ones((2, 2)))
print(np.arange(0, 10)) # шаг (как в range)
print(np.linspace(0, 1, 5)) # колличество чисел

# Размерность массива
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.shape) # выводит размер массива (2, 3)
print(a.ndim) # многомерность массива 2
print(a.size) # колличество эллементов в целом 6

# ========= Индексация и срезы ===========
# Одномерный массив
a = np.array([1, 2, 3])
print(a[1])
print(a[0:2])

# Двухмерный массив
a = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(a[0, 1])
print(a[0][1])

# формат: строка, столбец

# Арифматические операции

a = np.array([1, 2, 3])

print(a + 1)
print(a * 2)


# Агрегатные функции
a = np.array([1, 2, 3])
print(a.sum()) #10
print(a.mean()) # 2.0
print(a.max()) # 3
print(a.min()) # 1

# ======= Изменение формы ======

a = np.arange(6)
print(a)

b = a.reshape(2, 3)
print(b)
c = a.reshape(3, 2)
print(c)

# Где используется NumPy
"""
1)Анализ данных - Pandas
2)Графиуи - Matplotlib
3)Машинно обучение - scikit-learn
"""

# ================== Практика ===========
# создать массив из чисел 1 - 10 (10 включительно)

arr = np.arange(1, 11)
print(arr)

# возвести массив в квадрат
arr = np.array([1, 2, 3])
print(arr**2)


# Создать Массив и изменить его форму 3Х3
arr = np.arange(9)
b = arr.reshape(3,3)
print(b)

#дан массив
arr = np.array(
    [
        [1, 2, 3],
        [3, 4, 5]
    ]
)
# надо вывести сумму
print(arr.sum())

# Получить второй столбец
arr = np.array(
    [
        [1, 2, 3],
        [3, 4, 5],
        [4, 6, 7]
    ]
)

print(arr[:, 1])
print(arr[:, 1:2])


# Найти среднее значение массива 
[10, 20, 30, 40]

arr = np.array([10, 20, 30, 40])
print(arr.mean())

# Создайте массив из четных чисел от 0 до 20
arr = np.arange(0, 21, 2)
print(arr)

# Создать массив 3Х3 со случайными числами
arr = np.random.rand(3, 3)
print(arr)