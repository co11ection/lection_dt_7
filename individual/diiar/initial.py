# ============= Numpy ==========
# быстрое вычисление с массивами list

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# Numpy

import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 9])

print(a+b)

# Numpy делает математику как в калькуляторе

# 1D - список [1, 2, 3]
# 2D - таблица 
# [
#     [1, 2, 3],
#     [3, 4, 5]
# ]

# 3D - куб данных
# [
#     [1, 2, 3],
#     [3, 4, 5],
#     [3, 4, 5],
# ]

#1D
arr = np.array([1, 2, 3])
print(a)
#2D
arr = np.zeros((2, 3))
print(arr)

arr = np.zeros((2, 10))
print(arr)

# 3D
arr = np.zeros((3, 4))
print(arr)

# Автоматические функции
print(np.ones((2,3)))
print(np.arange(0, 10, 2)) # 1 начало 2 конец 3 шаг
print(np.linspace(0, 1, 5)) # Колличество чисел между отрезком

# Размерность массива:
arr = np.array(
    [
        [1, 2, 3], # 0
        #0  1  2
        [2, 3, 4]  # 1
        #0  1  2
    ]
)
print(arr.shape) # выводит размер массива
print(arr.ndim) # выводит многомерность масссива
print(arr.size) # выводит колличество элементов

# ============== Индексация и срезы ===============
# 1 мерный массив
arr1 = np.array([1, 2, 3])
print(arr1[1]) 
print(arr1[0: 2])

#2 мерный массив

print(arr[0, 0])
print(arr[1][0:2])
# Формат: строка столбец

# Арифматические операции с numpy
arr1 = np.array([1, 2, 3])
print(arr1 + 1) 
print(arr1 * 2)
print(arr1 ** 2)

# Агрегатные функции
arr1 = np.array([1, 2, 3])
print(arr1.sum())
print(arr1.mean())
print(arr1.min())
print(arr1.max())

# Изменение формы

arr = np.arange(6)
print(arr)

b_arr = arr.reshape(2, 3)
print(b_arr)

# Где используется Numpy 
# 1) Анализ данных - Pandas
# 2) Графики - Matplotlib
# 3) Машинное обучение - scikit-learn


# Создать массив из чисел от 1 - 10 (10 включительно)
# Возвести массив в квадрат
# изменить его форму 2Х5
# вывести сумму
# вывести второй столбец и его 3 элемент