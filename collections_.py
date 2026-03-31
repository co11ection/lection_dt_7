#============= COLLECTIONS ==============
# стандартные структура данных (list, dict, set, tuple) покрывают
# большинство задач

# однако модуль collections предоставляет расширенный контейнера, которые:
"""
1)упрощают код
2) повышают производительность
3) добавляют удобные абстракции
"""

# collections - это часть стандартной библиотеки Python
# реализующая специализированные контейнеры которые оптимизиоованы
# под конкретные сценарии или задачи


# Использовать структуру данных, максимально соответсвующую задаче 
# (дата орентированный дизайн)

# import collections

#================ Counter =================

from collections import Counter
# Counter - больше чем счетчик
# является подклассом dict, где:
# ключ = элемент
# значение = колличество


a = Counter([1, 2, 3, 1, 2, 4, 3])
b = Counter([2, 3, 4, 5, 4, 2, 4])

# + - сумирует частоты
print(a+b)
# - разность
print(a-b)
# & - пересечение (min)
print(a&b)
# | - обьединение (max)
print(a|b)

c = Counter(a=2, b=-1)
# c = Counter(a=2, b=0)
print(c)
print(list(c.elements()))

# Парктический кейс
# анализ логов 
# NLP (частоты слов)


#============== defaultdict=============
# Проблемы стандартного dict
# dict_1 = {}
# dict_1["key1"] +=1

from collections import defaultdict
# defaultdict(factory_function)
# Варианты использования:
# 1 Счетчик
d = defaultdict(int)
print(d)
# список
d = defaultdict(list)
# Множества
d = defaultdict(set)

a = defaultdict(int)
a["key1"] += 1
a["key2"] += 2
print(a)

# ========= deque ===========
# эффективная очередь
        #  list        deque
# append    O(1)        O(1)
# pop(0)    O(n)        O(1)
from collections import deque

dq = deque([1, 2, 3], maxlen=3)
dq.append(4)
print(dq)

dq.rotate(1)
print(dq)

# deque - безопасен для многопоточного использования

# Реальные кейсы:
# кеш

#============= namedtuple =================
from collections import namedtuple
user = namedtuple("user", ['name', 'age', "role"])
u = user(name="Aktan", age=20, role="admin")
print(u.name)
print(u.age)

#============ ordereddict ===========
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2

print(ordered_dict)
ordered_dict.move_to_end("a")
print(ordered_dict)


# =========== ChainMap ========
# обьединение нескольких словарей
from collections import ChainMap
dict1 = {
    "a": 1,
    "b": 2
}
dict2 = {
    "c": 1,
    "d": 4
}
chain_map = ChainMap(dict1, dict2)

print(chain_map["a"])
print(chain_map["d"])

# Реальные кейсы
# конфигурации
# области видимости

# Counter ->  Подсчет частоты
# defaultdict ->  значения по умолчанию
# deque -> очереди
# namedtuple -> структурированные записи
# ChainMap -> обьединение словарей
 
#================= Парктика =====================

text = "hello my name is Aktan. i am 23 years old. I am learning python"
from collections import Counter
words = text.lower().split(" ")
counter_1 = Counter(words)
print(counter_1)

#Реализовать очередь задач с добавлением в начало и конец.

from collections import deque

queue = deque()

queue.append("task1")
queue.appendleft("task")
print((queue))

# print(queue.pop())
# print(queue.popleft())

# найти 3 самых частыч числа 
list1 = [1, 1, 1, 2, 2, 3, 3, 3, 5, 5, 4, 4, 4]
counter = Counter(list1)
print(counter.most_common(3))

# Настройки которые заданы по дефолту
# пользовательские
default = {"theme": "light", "lang": "en"}
user = {"lang": "ru"}
from collections import ChainMap
config = ChainMap(user, default)

print(config["lang"])
print(config["theme"])

# есть список студентов с их курсами

students = [
    ('Alice', 1),
    ('Bob', 2),
    ('Charlie', 1)
]

from collections import defaultdict

groups = defaultdict(list)

for name, cource in students:
    groups[cource].append(name)

print(dict(groups))