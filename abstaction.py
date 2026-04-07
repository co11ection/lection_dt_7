# =============== Абстракция и Миксины ================
# Абстракция - это 1 из 4 (5) принципов ООП
# Суть абстракции в том, что мы скрываем сложные детали 
# и предоставляем пользователю только необходимые интерфейсы 

# зачем нужна абстракция
# 1)контракт - какие методы должны быть реализованы в дочерних классах
# 2)гибкость - можно менятоь реализацию не трогая код который находится
# в абстракции. и расширять его
# 3)масштабируемость - легко добавлять новые реализации


# Основная роль абстракции - в том чтобы была правильностоь
# работы полиморфизма и наследования

from abc import ABC, abstractmethod 
# чтобы клвсс или метод были абстрактными надо класс унаследовать от ABC
# а метод обернуть в декоратор abstractmethod

# class A(ABC):
#     @abstractmethod
#     def __init__(self):
#         pass

# class B(A):
#     pass

# b = B()
# print(b)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetr(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r**2
    
    def perimetr(self):
        return 2 * 3.14 * self.r

circle = Circle(5)
print(circle.area())
print(circle.perimetr())

# shape = Shape()
# print(shape)
# От абстрактного класса создавать обьект нельзя


# ================ MIXINS ====================
# Миксины - это класс, который предостовляет определенный функционал,
# для расширения в дочерние классы.
# Но не преднозначен для самостоятельного использования.
# Способ использования повторно код без жесткой иерархии (наследования)


# Правила хорошего миксина
# 1) Миксин не должен иметь собственного __init__ 
# (или должен вызывыать super().__init__())
# 2) Миксин не преднозначен для солздания экземляров (обьектов) самостоятельно
# 3) Миксин добавляет ОДНУ конкретную возможность
# 4) Название миксинов ДОЛЖНЫ заканчиваться на Mixin
# 5) Миксин идет ПЕРЕД основными класами в списке наследования

class MotorMixin:
    def start(self):
        print("Мотор запустился")

class ShinaMixin:
    def krutitsia(self):
        print("Шины крутятся")

class Transport:
    def __init__(self, brand):
        self.brand = brand       

class Car(MotorMixin, ShinaMixin, Transport):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car1 = Car("hunday", "sonata")
car1.start()
car1.krutitsia()

class CreateMixin:
    def create(self):
        print("User is created")

class SaveMixin:
    def save(self):
        print("User is saved")

class User(CreateMixin, SaveMixin):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"{self.username} -- {self.email}"

user1 = User("timatima", "1qazxcvB", "tima.j.zh@gmail.com")
print(user1)
user1.create()
user1.save()


# ============== Практика =============
"""
Создать класс Product
добавить туда классы миксины 
DiscountMixin - высчитывать скидку
apply_discount(price, precent)
LogerMixin - логирует действие
log(message)
"""

class DiscountMixin:
    def apply_discount(self, price, precent):
        discount = price * (precent / 100)
        return price - discount
    
class LogerMixin:
    def log(self, message):
        return f"[LOG] --- {message}"


class Product(DiscountMixin, LogerMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} -- {self.price}"
        
product1 = Product("milk", 45)
print(product1.apply_discount(product1.price, 10))
print(product1.log("Вытащили скидку"))