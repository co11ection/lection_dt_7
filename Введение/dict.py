# =======================  Словарь(Dict) ====================
#dict - изменяемы, итерируемый,  неупорядочный, неиндексируемый тип данных.
# для хранения данных в парах {key: value}
# key - может быть толь неизменяемый тип данных
# value - без разницы

user = {
    "name": "Aktan",
    "age": 19,
    "last_name": "Asanov"
}
print(user["name"]) #Aktan

# если ключи повторяются то сохраняется только последнее значение
dict1 = {
    "a": 1, "b": 2, "c": 3, "a": 4 
}
print(dict1) # {'a': 4, 'b': 2, 'c': 3}

#================== Создание словарей ======================
dict2 = {"a": 1}
dict3 = dict([("a", 4),("b", 6)])
print(dict2)
print(dict3)
dict4 = dict(["ab", "cd", "ef"])
print(dict4) #{'a': 'b', 'c': 'd', 'e': 'f'}

dict5 = {}
dict5["name"] = "Aktan"
dict5["age"] = 20
print(dict5) #{"name": "Aktan", "age": 20}

#==================== Методы словарей ===================
user = {
    "name": "Aktan",
    "age": 19,
    "last_name": "Asanov"
}
# print(user["second_name"])#KeyError: 'second_name'

# get() - метод, который возвращает значение по ключу, если ключа нету, 
# то возвращает None или дефолтное значение которое мы сами передали
print(user.get("second_name"))
print(user.get("name"))
print(user.get("second_name", "Такого ключа нету!!!!!"))

# pop() - удаляет по ключу  и возвращает значение
dict1 = {
    "a": 1, "b":2
}
popped = dict1.pop("a")
print(dict1) 
print(popped)

#popitem() - удаляет последнюю пару и возвращает ее
dict1 = {
    "a": 1, "b":2
}
popped = dict1.popitem()
print(dict1) 
print(popped)

# update() - расширяет словарь парами из второго словаря
dict1 = {
    "a": 1, "b": 2
}
dict2 = {
    "c": 3, "d": 4
}
dict1.update(dict2)
print(dict1)
dict1.update({"e": 9})
print(dict1)

#clear - очищает словарь
dict1 = {
    "a": 1, "b": 2
}
dict1.clear()
print(dict1) # {}


dict1 = dict.fromkeys("hi", 'hello')
print(dict1)

dict2 = dict.fromkeys([1, 2, 3], "Дефолтное значение")
print(dict2)



user = {
    "name": "Aktan",
    "age": 19,
    "last_name": "Asanov"
}

# keys() - метод который возвращает ключи
print(user.keys())
# values() - метод который возвращает значения
print(user.values())
# items() - метод, который возвращает пары ключ - значение в виде tuple
# [("name", "Aktan"), ("age", 19)]
print(user.items()) 


# ================ Итерируемость словарей =====================

user = {
    "name": "Aktan",
    "age": 19,
    "last_name": "Asanov"
}

for key in user.keys(): #["name", "age", "last_name"]
    print(key)

for value in user.values(): # ["Aktan", "19", "Asanov"]
    print(value)

for key, value in user.items():
    print(f"key: {key}, value: {value}")
    

students = {
    "student1": {"name": "Almaz", "age": 20},
    "student2": {"name": "Aigul", "age": 20}
}
print(students["student1"]["name"])
print(students.get("student1").get("name"))


# ========================= Практика =========================
# дана строка 
string = "python is easy python is powerful"
#Подсчитать, сколько раз каждое слово встречается и записать его в словарь
result = {
    "python": 2,
    "is": 2,
    "easy": 1,
    "powerful": 1
}

words = string.split(" ") #["python", "is", "easy" ...]

result = {}
for word in words:
    result[word]= result.get(word, 0) + 1

print(result)


#Найти самую высокую оценку.
grades = {
    "Ali": 90,
    "Sara": 95,
    "Omar": 85,
    "Aziz": 88
}
# Самый высокий бал у Sara 95

max_grade = 0 #95
best_student = None # sara

for name, score in grades.items():
    if score > max_grade:
        max_grade = score
        best_student = name

print(f"Самый высокий бал у {best_student}, {max_grade}")
