#===================Принципы ООП==============
# 1) Инкапсуляция
# 2) Наследование
# 3) Абстракция
# 4) Ассоциация (Композиция и Агрегация)
# 5) Полиморфизм


# 1) Инкапсуляция - это сокрыти внутренних реализаций обьекта 
# и предоставление доступа к данным

# element = 12 - Общедоступный, публичный
# _element = 12 - 'это защищенный' (protected)
# __element = 12 - "приватный" (prived)

class BankAcount:
    def __init__(self, balance: float, card_number: int, username: str):
        self.username = username
        self._card_number = card_number
        self.__balance = balance
        
    def info(self):
        print(f"""
              Пользователь: {self.username}, 
              Номер карты: {self._card_number}, 
              Баланс: {self.__balance}"""
            )
    
    def deposit(self, amount:float):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance


aktans_account = BankAcount(username="Aktan3000", card_number=12312312311, balance=120.12)
aktans_account.info()
aktans_account.deposit(100)
print(aktans_account.get_balance())
aktans_account.info()
print(aktans_account.username)
print(aktans_account._card_number)
# print(aktans_account.__balance) - вне класса не имеем доступа
# print(aktans_account._BankAcount__balance) обходной путь для получения (НЕ СОВЕТУЕТСЯ ТАК ДЕЛАТЬ!!!!!!!)


# 2) Наследование

class Animal:
    def speak(self):
        print("Определенный звук")

class Dog(Animal):
    def speak(self):
        print("GAV GAV")
    

barsik = Dog()
barsik.speak()


# 5) Полиморфизм

print(5+5) #10
print("5"+"5") #"55"

class Dog:
    def speak(self):
        print("GAV GAV")
        

class Cat:
    def speak(self):
        print("MEOW MEOW")
        
def animal_sound(animal):
    animal.speak()
    
barsik = Dog()
pifagor = Cat()

animal_sound(barsik) 
animal_sound(pifagor) 
       

# 3) Абстракция - Правильная постройка классов и правильная работа полиморфизма
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimetr(self):
        pass
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def info(self):
        print(f"side = {self.side}, area: {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
        

sq1 = Square(12)
print(sq1.side)
print(sq1.area())
print(sq1.info())

ci = Circle(10)
print(ci.radius)
print(ci.area())


# 4) Ассоциация (Композиция и Агрегация)

# Агрегация - слабая связь

class Motor:
    def start(self):
        print("Motor started")

e_110 = Motor()

class Car:
    def __init__(self, motor):
        self.motor = motor
    
    def start(self):
        self.motor.start()

nissan = Car(e_110)
nissan.start()


#Композиция - сильная связь

class Motor:
    def start(self):
        print("Motor started 2")

class Car:
    def __init__(self):
        self.motor = Motor()
    
    def start(self):
        self.motor.start()

nissan = Car()
nissan.start()


# проект Онлайн магазин попытаться использовать все принципы
# абстрактный класс Product + Инкапсуляцию 
# Наследуетесь и создаете класс Мясные продукты или Мыломоющие средства
# используете методы (получение цены)
# корзина - добавляем продукты и выводите конечную цену закупок
