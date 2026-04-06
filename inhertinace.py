# ==================== Наследование =======================

# Родительский класс - Класс от которого наследубт:
# Базовый, супер, parrent class

# Дочерний класс - класс который наследует:
# подкласс, производный класс, child cldss

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"{self.name} издает звук"
    
    def info(self):
        return f"{self.name}, возраст: {self.age}"

class Dog(Animal):
    def __init__(self, name: str, age: int, legs: int):
        super().__init__(name, age)
        self.legs = legs
    
    def speak(self):
        return f"{self.name} говорит ГАВ!"
    
    def fetch(self):
        return f"{self.name} приносит мяч"        
# super() -> обращение к родительскому методу (__init__)

barsik = Dog(name="barsik", age=1, legs=4)
print(barsik.age)
print(barsik.name)
print(barsik.legs)

print(barsik.info())
print(barsik.speak())
print(barsik.fetch())

# ============== Типы наследования ===============
#1 Одиночное наследование - дочерний класс наследуется от одного родительского класса
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# 2 Множественное наследование - дочерний класс наследуется от нескольких родительских классов
class Flyable:
    def fly(self):
        return "может летать"

class Swimmable:
    def swim(self):
        return "Умеет плавать"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Кря!"
    

duck = Duck()
print(duck.swim())
print(duck.fly())
print(duck.quack())

# 3) Многоуровневое наследование: 
# A(самый первый род класс) -> B(A) дочерний класс наследуется от класса А -> C(B)

class Animal:
    def live(self):
        return "Живет"

class Mammal(Animal):
    def feed_milk(self):
        return "Кормит молоком"

class Cow(Mammal):
    def speak(self):
        return "muuu"

cow = Cow()
print(cow.live())
print(cow.feed_milk())
print(cow.speak())

#4) Иерархичное наследование 
# несколько дочерних классов наследуются от одного класса
class Mammal:
    def feed_milk(self):
        return "Кормит молоком"

class Cow(Mammal):
    def speak(self):
        return "muuu"
    
class Dog(Mammal):
    def speak(self):
        return "GAV"

# ================ Проблема ромба ===============
class Dog:
    def speak(self):
        return "GAV"

class Dolmatines(Dog):
    def info(self):
        return "Доматинец"
    
    def sleep(self):
        return "мношго спит"
    
class Chihuahua(Dog):
    def info(self):
        return "Чихуахуа"
    
    def agression(self):
        return "Агрессивный"
    
class NewParoda(Dolmatines, Chihuahua):
    def info(self):
        return "Новая порода"


new = NewParoda()
print(new.speak())
# MRO - Method Resolution Order
print(NewParoda.__mro__)

# ================ Переопределение методов ==================
# !) Базовое переопределение
class Shape:
    def area(self):
        return 0
    
    def describe(self):
        return f"Площадь равна {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)
    
circle = Circle(5)
print(circle.area())
print(circle.describe())

# Расширение метода

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        from datetime import datetime
        time = datetime.now().strftime("%H:%M:%S")
        return super().log(message=f"[{time} ---- {message}]")
    
logs = TimestampLogger()
logs.log("Сервер запущен")
