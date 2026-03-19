"===================== Функция ====================="

# Функция - именованный блок кода, который может принимать аргументы 
# и возвращать результат
# def - инициализация (создание) функции

a = 5
b = 4
print(a+b)

def my_sum(a, b):
    result = a + b
    return result
    
summ = my_sum(3, 5)
print(summ)

"""
def <название>(<параметры>):
    <логика>
    return <что либо> "если не прописать return то вернется None"

<название>(<аргументы>)
"""

# Функция соблюдает принцип DRY (don't repeat yourself)

#================= Аргументы и параметры =======================
"""Параметры - переменные внутри функции,
значения которым задаем при вызове функции.
тоесть переменные которые мы пишем в круглых скобках
когда создаем функцию (def my_sum(параметры))
"""

"""
Аргументы - значения которые мы передаем при вызове функции
my_sum(аргументы)
"""

# ================ Виды параметров ==================
"""
1 - Обязательные 
2 - Не обязательные
    2.1 Дефолтные
    2.2 args - все позиционные аргументы, которые не попали в обязательные 
    и с дефолтом попадают сюда. принимает в виде tuple
    2.3 kwargs - все лишние именнованные аргументы записываются в kwargs,
    в виде словаря dict
"""
# =============== Виды аргументов ===============
"""
1 - Позиционные (по позиции)
2 - именованные (по названию параметра (параметр = значение))
"""

def my_sum(a, b): # Обязательные параметры
    result = a + b
    return result
    
print(my_sum(3, 5)) # Позиционные
print(my_sum(a=9, b=2)) # именованные
print(my_sum(b=7, a=2))
#print(my_sum()) #my_sum() missing 2 required positional arguments: 'a' and 'b'


def func(a, b, c=2): # 2.1 Дефолтные
    return a * b * c

print(func(a=2, b=3))
print(func(a=3, b=4, c=2))
print(func(2, 3, 4))

def func(a, b, *args):
    print("a", a)
    print("b", b)
    print("args", args)

func(1, 2, 3, 4, 5, 6, 7, 8) #args 2.2

def func(a, b, **kwargs):
    print("a", a)
    print("b", b)
    print("kwargs", kwargs)

a = func(a=7, b=3, c=8, d=2, e=5)
print(a)


def square(num):
    result = num ** 2
    return result

print(square(num=3))
print(square(4))

# написать функцию is_even(num), которая возвращает True если число четное, 
# и False если число нечетное

def is_even(num=3):
    if num % 2 == 0:
        return True
    return False

print(is_even(4))
print(is_even())



# ================== Практика ===================================
# 1 Создайте функцию factorial(n), которая возвращает факториал числа.
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
        # result = result * i
    return result
    
print(factorial(5))

# 2 Напишите функцию count_vowels(text), которая считает количество гласных в строке.
def count_vowels(text: str) -> int:
    vowels = "aeiuoy"
    count = 0
    
    for char in text:
        if char.lower() in vowels:
            count += 1
    
    print(count)

text1 = input("Введите текст")
print(count_vowels(text1))

#3 Напишите функцию is_palindrome(word), которая проверяет, является ли слово палиндромом.

def is_palindrome(word: str) -> bool:
    return word == word[::-1] # True/False

print(is_palindrome("level"))
print(is_palindrome("taxi"))


# Напишите функцию sum_list(numbers), которая возвращает сумму всех элементов списка.

def sum_list(numbers: list[int]) -> int:
    result = 0
    for num in numbers:
        result += num
    return result

print(sum_list([1, 2, 3, 4, 5]))