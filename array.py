# ======== Массивы(Коллекции в Python) ========

"""
list - Список - Упорядочные именяемые коллекции 
tuple - Кортеж - упорядочная неизменяемая коллекция
set - Множество - неупорядочная коллекция уникальных элементов
"""

# a = []
# print(dir(a)) # Просмотр методов

#  =======list===
# литералы листа(обьозначение) - []

numbers = [1, 2, 3, 4]
name = ['hello', True, (1, 2, 3)]

# ========= Методы List ==============
elements_list = [10, 1, 26, True]

print("first element",elements_list[0])
elements_list[0] = 100
print(elements_list)

# append() - Добавляет элемент в конец
elements_list.append(False)
print(elements_list) #[1, 2, 3, "hello", True, False]

#pop() - Удаление элемент по интексу 
# (если индекс не передан, то удаляет последний) 
# и при этом возвращает удаленный элемент

# elements_list.pop()
# print(elements_list)# Удаление 
# deleted_element = elements_list.pop(0)
# print(deleted_element, deleted_element + 10)


# sort() - Метод сортировки

elements_list.sort()
print(elements_list) # [False, 1, True, 10, 26]

a = ["bektur", "asan", "aktan", "john", "atay"]
a.sort()
print(a)

#reverse() - Переворачивает список
elements_list.reverse()
print(elements_list) #[26, 10, True, 1, False]


list_person = ["bektur", "asan", "aktan", "john", "atay"]
# "Azat", Almaz +
# "john", "asan" -
# отсортировать по убыванию
list_person.append("Azat")
list_person.append("Almaz")
print(list_person)
list_person.pop(list_person.index('asan'))
list_person.pop(2)
print(list_person)
list_person.sort(reverse=True)
print(list_person)

print(list_person.index("atay"))

# =============== Tuple ===============
# Литералы tuple (обозначение) (,)
numbers = 1, 2, 3, 4
print(type(numbers)) # <class 'tuple'>

# отличие от list - 
# Скорость - tuple > list
# Tuple - неизменяемый, list - изменяемый
# выделение памяти list > tuple

print(dir(numbers))

# =========== Методы tuple ==============
#count - считает количестыо элементов
# index - выводит индекс элемента

num = (1, 1, 2, 3, 4, 1, 3, 4)
print(num.count(1))
print(num.index(1)) # 0


# ====== set =========
# хранит в себе только неизменяемые типы данных
numbers = {1, 2, 1, 2, 3, 4}
print(numbers) # {1, 2, 3, 4} убирает все дубликаты и хранит уникальные данные 

#========= Методы ==========
numbers = {1, 2, 1, 2, 3, 4}

# add() - Добавление элемента

numbers.add(5)
numbers.add("hello")
numbers.add(False)
numbers.add((6, 7, 8))
# numbers.add({6, 7, 8}) # unhashable
print(numbers)
a = {6, 7, 8}
b = {6, 7, 8}
print(id(a))
print(id(b))

#remove - удаляет элемент
numbers = {10, 2, 1, 2, 3, 4}
numbers.remove(2)
print(numbers) #{1, 3, 4}

# numbers.remove(5) #KeyError: 5

# discard() - удаление без ошибки

numbers.discard(5)
print(numbers)

#pop() - удаление на рандоме
numbers.pop()
print(numbers)

# union() - обьединить множества
a = {2, 3, 10}
b = {"hello", 8, 3, True}
print(a.union(b))

# intersection() - Пересечение
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.intersection(b))

# difference() - Разность
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.difference(b))
print(b.difference(a))

a = list()
a = set()
a = int()
a = tuple()

# =============== Практика ==============
numbers = [1,2,2,3,4,4,5]
set_number = set(numbers)

print(set_number)

# найти пересечение/ разность / обьединить
a = {2, 4, 5, 6}
b = {3, 5, 3, 4}

print(a.intersection(b))
print(a.difference(b))
print(a.union(b))

a = (10, 20, 30, 40)
print(a[a.index(10)])