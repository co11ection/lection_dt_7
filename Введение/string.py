# ================ Стриоки ========================
# Строки - неизменяемый тип данных, который обозначается (литералы) '' или ""
# типом данных который хранит в себе текст (последовательности символов)

string1 = 'строки с одинарными ковычками'
string2 = "строки с двойными ковычками"

#error 'не коректная строка "

string3 = '''Многострочная строка
в одинарных ковычках
тут можно "использовать" любые 'ковычки'
'''
print(string3)

string4 = """
Многострочная строка 
с двойными ковычками
тут можно "использовать" любые 'ковычки'
"""
print(string4)

#Конкатенация

string5 = "hello" + " " + "world" + "!"
print(string5)

greeting = "Hi!"
name = "Asan"
result = greeting + ' ' +name
print(result)


string7 = "A" * 8
print(string7) # AAAAAAAA

#======= Экранизация строк==========
"\n" # перенос на новыую строку
print("hello world!\nMy name is Aktan")

"\t" # табуляция
print("Hello\tworld!")

"\v" #перенос на новую строку со смещением в право на длину предыдущей строки
print("Hello world\vi am study\vin ai academy")


# "\" - Используется для отображения и сохранения знаков
a = "Hello\\tworld"
print(a)


#==================== Форматирование строк =========================
greeting = "Hi!"
name = "Asan"
result = f"{greeting} {name}"
print(result)


title = 'Iphone13'
price = '100'
format1 = "Название: {}\n Цена:{}"
print(format1.format(title, price))


title = 'Хлеб'
price = '30'
format3 = "Название: %s \nЦена: %s" % (title, price)
print(format3)

a = " Don't"
b = ' don"t '


# ================ Методы строк =============

# методы - функции, которые относятся к определенному классу типов данных,
# к ним мы обращаемся через точку

# print(dir(str))

string_test = "heLLo WorLd"
print(string_test.lower()) # переносит все в нижний регистр
print(string_test.upper())# Переносит все в верхний регистр

print(string_test.swapcase()) #Меняет регистр
print(string_test.title()) #Hello World
print(string_test.capitalize()) # Hello world

print(string_test.count("L"))
print(string_test.count("LL"))
print(string_test.count("heLLo"))


print(string_test.startswith("l"))
print(string_test.endswith("d"))

print(string_test.islower())
print(string_test.isupper())

print(string_test.isnumeric()) # Проверка состоит ли наша строка из чисел
print(string_test.isalpha()) # Проверка состоит ли наша строка из символов
print(string_test.isalnum()) # Проверка состоит ли наша строка из чисел и символов



string = '     hi my name is Uson      '
print(string)
print(len(string.lstrip())) #hi my name is Uson  #24
print(len(string.rstrip())) #     hi my name is Uson 23
print(len(string.strip()))#hi my name is Uson 18

# ============= Индексы ==============
'h e l l o a i a c a d   e  m y'
#0 1 2 3 4 5 6 7 8 9 10 11 12 13

string = 'John Snow'
#Один элемент
print(string[0])# J
print(string[8])# w
print(string[-1]) # w

# срез
print(string[0:4])
print(string[5:9])
print(string[5:])

print(string[::2])
print(string[::3])
print(string[::-1])
print(string[::-2])


# у вас есть переменная string в которой ханирится слово Python
# вам надо вывести 1 и последний элемент
# Ответ:   Первый элемент - {}, Последний элемент - {}.

string = "Python"
first_element = string[0]
last_element = string[-1]
print(f"Первый элемент - {first_element}, Последний элемент - {last_element}.")


# выведите строку через каждые два элемента
# В формате Ответ: {значение}
result = string[::2]
print(f"Ответ: {result}")

#Количество символов
string = "banana"  #a

count_element = string.count("a")
print(count_element)
