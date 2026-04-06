# ================== Итераторы  и итерируемые обьекты ========================
#итерируемые обьекты: list, tuple, set, dict, file, str


data = [1, 2, 3]
for i in data:
    print(i)
    
from collections.abc import Iterable

print(isinstance(data, Iterable))
print(isinstance(7, Iterable))

# ===================== Итераторы =====================
# итератор - это обьект который:
# 1)хранит текущее состояние 
# 2) возвращает элементы по одному (next())

data = [1, 2, 3]
iteration_data = iter(data)

print(next(iteration_data))
print(next(iteration_data))
print(next(iteration_data))
# print(next(iteration_data)) #StopIteration - так как в итерируемом обьекте закончились элементы

# val - текущее значение
# next - ссылка на следующий элемент

# ListNode - изучить в свободное время!!!!!!!!!!!!

data = [1, 2, 3]
# Как работает for
for i in data:
    print(i)
# Эквивалентно
iter_data = iter(data)
print("Использовали iter")
while True:
    try:
        element = next(iter_data)
        print(element)
    except StopIteration:
        break


# 1 итерация
# val = None
# next = 1
# 2 итерация
# val = 1
# next = 2
# 3 итерация
# val = 2
# next = 3
# 4 итерация
# val = 3
# next = None


# создать список получить итератор и вручную пройтись через next

# list1 = [1, 2, 3, 4, 5]

# iter_list = iter(list1)

# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))

list1 = [1, 2, 3, 4, 5]
iter_list = iter(list1)
print("1 цикл")
for i in iter_list:
    print(i)
    
print("2 цикл")
for j in iter_list:
    print(j)
# print("3 цикл")
# for i in list1:
#     print(i)
# print("4 цикл")
# for j in list1:
#     print(j)
# ИТЕРАТОРЫ ЯВЛЯЮТСЯ ОДНОРАЗОВЫМИ

class Counter:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

c = Counter(10)
print(c.__next__())
print(c.__next__())
print("Запуск цикла")
for i in c:
    print(i)

# Генераторы 
data = [x for x in range(1000000)] # плохой вариант
# print(data) 

data2 = (x for x in range(1000000)) # хороший вариант

# for i in data2:
#     print(i)

next = 1
next = 2


def generator(num):
    for i in range(num):
        yield i ** 2

gen = generator(1000000)

# for i in gen:
    # print(i)
    

# =================== Практика ===================

# data = [10, 15, 20, 25, 30, 40]
# создать генератор 
# только числа  > 20
# умножить на 2

# gen = (i * 2 for i in data if i > 20)
# for i in gen:
    # print(i)
    
    
logs = [
    "INFO start",
    "ERROR failed",
    "INFO processed",
    "ERROR crash"
]

def get_errors(logs):
    for log in logs:
        if "ERROR" in log:
            yield log


errors = get_errors(logs)

# for error in errors:
#     print(error)


def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
            
def count_errors(file_path):
    count = 0
    for line in read_logs(file_path):
        if "ERROR" in line:
            count+=1
    return count

print("count errors: ", count_errors("sample_logs.txt"))


gen = (x for x in range(5))
print(list(gen))#1[0-5] 2[0-5]
print(list(gen))#1[0-5] 2[]


# написать свой range
def my_range(end, start=0):
    current = start
    while current < end:
        yield current
        current+=1


for i in my_range(end=10):
    print(i)