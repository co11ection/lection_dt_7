# =================== Цикл ===================
#Цикл - это блок кода, который отрабатывает несколько раз

#Виды циклов: for, while

#for - цикл,который работает с итерируемыми обьектами
#list - [1, 2, 3], set, tuple, dict, str
#заканчивает свою работу, когда доходит до последнего элемента
#range() - генерирует числа

# while  - цикл который работает до тех пор пока условие выдает True

for i in range(1, 11):
    print(i)
    
n = 1
while n <= 10:
    print(n)
    n += 1


# =============== Клячевые слова в циклах ========================
#break - полностью останавливает работу цикла (выход из цикла)
#continue - переход к следующей итерации

for i in range(10):
    if i == 3:
        continue
    print(i)


    
for i in range(10):
    print(i)
    if i == 3:
        continue

for i in range(10):
    if i == 5:
        break
    print(i)
#0, 1, 2 3 4

for i in range(10):
    print(i) 
    if i == 5:
        break
0, 1, 2, 3, 4, 5


# WHILE

#while <учловие>:
# действие



while True:
    age = int(input("Введите возраст: "))
    if age < 18:
       print("Укажи возраст выше")
    else:
        print("Отлично")
        break
# i = 0
# while True:
#     i+=1
#     print("hello", i)


# a = [1, 2, 3, "Hello"]
# for i in a:
#     a.append(i)
#     print(a)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    print(num)


string = "hi hi ai academy".split(" ")

["hi", "hi", "ai", "academy"]

for letter in string:
    print(letter)


# ============== Практика =================

# суммировать от 1 до 100 и вывести вывод

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# range (1, 100) запринтить только те числа которые являются четными 

#1 
print("=======1 вариант========")
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
        
print("=======2 вариант========")
for num in range(1, 101):
    if num % 2 != 0:
        continue
    print(num)
    
print("=======3 вариант========")
for i in range(2, 101, 2):
    print(i)
    

num = 0 
for i in range(1, 3): 
    for j in range(1, 3):
        print(f"i: {i}     j: {j}")
        


secret = 7
attempts = 5

while attempts > 0:
    num = int(input("Введите число: "))
    
    if num == secret:
        print("Вы угодали!!")
        break
    elif num < secret:
        print("Загаданное число больше")
        attempts -= 1
    else:
        print("Загаданное число меньше")
        attempts -= 1
    print(attempts)
    if attempts > 0:
        print("Попробуй еще раз")
    else:
        print("Вы проиграли, попыток не осталось!")
        

# Написать калькулятор и пока я не напишу exit программа работает
# + - * /

while True:
    num1 = input("Введите 1 число: ")
    if num1 == "exit":
        break
    num2 = input("Введите 2 число: ")
    if num2 == "exit":
        break
    num1 = int(num1)
    num2 = int(num2)
    while True:
        command = input("Выберите операцию(+, -, *, /) ")
        if command in "+-*/":
            break
        else:
            print("Введите корректную операцию!!")
        
    if command == "exit":
        break
    elif command == "+":
        result = num1 + num2
    elif command == "-":
        result = num1 - num2
    elif command == "*":
        result = num1 * num2
    else:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "На 0 делить нельзя"
    
    print(result)