#================Декораторы================
"""
Функция высшего порядка - функция которая принимает аргументом другую функции
создает внутри себя функцию, вызывает функцию и так же возвращает функцию

декораторы - функция высшего порядка, которая нужна чтобы расширить функцию
не изменяя ее (ее функционал) это просто функция обертка
"""

def decorator1(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print("start", datetime.now())
        func(*args, **kwargs)
        print("finish", datetime.now())
    return wrapper

def hello():
    print("hello world!")

decorator1(hello)()

wrapper = decorator1(hello)
wrapper()


#========= Синтаксический сахар ===========
@decorator1
def bye():
    print("bye guys")
    
bye()

@decorator1
def my_sqrt(num):
    print(num**0.5)

my_sqrt(16)


def decorator2(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator2(5)
def hello():
    print("hello world!")

hello()


@decorator2(5)
@decorator1
def sums(a, b):
    print(f"result: {a+b}")

sums(2, 3)

func = decorator2(decorator1(sums))

func(5)


def logs(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logs
def test():
    print("Все работает!!")
    
test()

def check_password(func):
    def wrapper(password):
        if password == "hihi":
            return func(password)
        else:
            print("Пароль не верный")
    return wrapper


@check_password
def secret(password):
    print("Доступ разрешен")

secret("hihi")
secret("1234")


def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls>=max_calls:
                print("Лимит превышен")
                return
            calls+=1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(3)
def test():
    print("testing......")


test()
test()
test()
test()


def cache(func):
    memory = {}
    def wrapper(x):
        if x in memory:
            print("Из кеша")
            return memory[x]
        result = func(x)
        memory[x] = result
        return result
    return wrapper

@cache
def get_square(x):
    print("Считаем.....")
    return x * x

print(get_square(2))
print(get_square(5))
print(get_square(2)) # !
print(get_square(4))
print(get_square(5)) # !


#================Практика=================
"""
Создать декоратор call_counter, 
который считает,
сколько раз была вызвана функция.
"""

def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1
        print(f"Функция вызвана {count} раз")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def hi():
    print("hi")
    

hi()
hi()
hi()
hi()
hi()


# Функция должна выполняться если роль пользователя "admin"
def check_admin(func):
    def wrapper(role):
        if role != "admin":
            print("Доступа нету")
            return
        return func(role)
    return wrapper

@check_admin
def delete_data(role):
    print(f"Данные успешно удалены ролью {role}")


delete_data("admin")
delete_data("user")



# Функция должна отрабатывать если у пользователя роль admin либо менеджер
# пользователя можно выбрать по имени

users = [
    {
        "name": "Aktan",
        "role": "admin"
    },
    {
        "name": "Asan",
        "role": "user"
    },
    {
        "name": "Aigul",
        "role": "manager"
    }
]

def check_permissions(func):
    def wrapper(name):
        for user in users:
            if user["name"] == name:
                if user["role"] in ["admin", "manager"]:
                    func(name)
                    return
                else:
                    print("Доступ закрыт")
                    return
        print("Пользователь не найден")
    return wrapper

@check_permissions
def delete_data(name):
    print(f"Данные успешно удалены пользователем {name}")
    
    
delete_data("Aktan") 
delete_data("Asan")
delete_data("Aigul")
delete_data("Tima")
