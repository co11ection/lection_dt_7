# ================ JSON ==================
# JSON - это текстовый формат обмена данными

# Почему JSON?
# читаемость
# Компактность - меньше изботочных данных по сравнению с XML
# Универсальность - поддерживается всеми современными языками программирования
# стандарт веба

# =================== Типы данных которые работают с json ================
dict, list, str, int, float, bool, None
#=========================================================================

{
    "name": "Aktan",
    "age": 20,
    "course": ["Python", "PSQL", "DS"],
    "adress": {
        "city": "Bishkek",
        "country": "Kyrgyzstan"
    }
}
# После послдних данных ставить "," нельзя
# когда json строка созлдается вручную 
# обязательно использовать двойные ковычки

# Сериализация - с питона на json
# Десериализация - с json на питон

import json

# json.dumps() # сериализация с python обьекта на json строку 
# json.loads() # десериализация с json строки в python обьект
# Буква s в конце означает string
#========================================================
# json.dump() # Python обьект сериализует на json файл
# json.load() # десериализация с json файла на python обьект
# рвботают с файлами

# ============== dumps ==================
import json

student = {
    "name": "Актан",
    "age": 20,
    "course": ['Python', "PSQL", "DS"],
    "adress": {
        "city": "Bishkek",
        "country": "Kyrgyzstan"
    },
    "is_citithen" : True,
    "email": None
}
# True/False - > true/false
# None  - >  null
json_string = json.dumps(student, indent=4, ensure_ascii=False)
print(json_string)

# =================== loads ================
json_string1 = """
{
    "title": "Мастер и Маргарита",
    "author": "Михаил Булгаков",
    "year": 1967,
    "genres": ["роман", "фантастика", "сатира"]
}
"""
book = json.loads(json_string1)
print(book)
print(type(book))
print(book['title'])
print(book.get("title1"))

#====================================
student = {
    "name": "Актан",
    "age": 20,
    "course": ['Python', "PSQL", "DS"],
    "adress": {
        "city": "Bishkek",
        "country": "Kyrgyzstan"
    },
    "is_citithen" : True,
    "email": None
}
print(json.dumps(student, sort_keys=True, ensure_ascii=False))

my_data = {
    "name": "Тима",
    "age": 23,
    "hobbies": ['Python', "Баскетбол"],
    "adress": {
        "city": "Bishkek",
        "country": "Kyrgyzstan"
    },
}

json_string_data = json.dumps(my_data, indent=4, ensure_ascii=False, sort_keys=True)
print(json_string_data)
print(type(json_string_data))

my_data = json.loads(json_string_data)
print(my_data)
print(type(my_data))

# ================ dump ===================
students = [
    {
        "name" : "Актан",
        "age": 25,
        "course": 3
    },
    {
        "name" : "Асан",
        "age": 23,
        "course": 2
    },
    {
        "name" : "Айдана",
        "age": 22,
        "course": 1
    }
]
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4, ensure_ascii=False)

print("файл создан!")


with open("students.json", "r", encoding="utf-8") as file:
    students_data = json.load(file)

# print("файл загружен")
# print(students_data)
# print("Получение каждого студента по очереди")
# for student in students_data:
#     print(student)
    
    
# создать файл с данными о 5 продуктах (название, цена, количество, категория)
# прочитать этот файл и вывести только те продукты у которых цена выше 500 сом

products = [
    {"title": "ноутбук", "price": 120000, "qty": 10, "category": "Техника"},
    {"title": "телефон", "price": 5000, "qty": 13, "category": "Техника"},
    {"title": "молоко", "price": 90, "qty": 100, "category": "Молочные изделия"},
    {"title": "хлеб", "price": 25, "qty": 100, "category": "Хлебо булочные изделия"},
    {"title": "Мясо", "price": 1000, "qty": 100, "category": "Мясо"}
]

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4, ensure_ascii=False)
print("File created and add products")

with open("product.json", "r", encoding="utf-8") as file:
    products_data = json.load(file)
    
print("GET products")
for product in products_data:
    if product.get("price") > 500:
        print(product)
        
