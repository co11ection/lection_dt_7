#=================== Pandas ============
# pandas - это библиотека Python для работы с табличными данными
# (Exel, CSV, База данных) но мощнее

#Работа с данными
# загрузка данных с файлов
# Exel, CSV, базы данных

#Очистки данных
# пропуски, ошибки, лишние строки

# Анализ данных
# Можно быстро получить статистику

# Основные структуры:
# Series - одномерный массив(как сталбец)
# DataFrame - таблица (строки +  столбцы)

#==============Series ==============
# это структура данных состоящая из:
# значение и индексов(меток)

# создание Series
import pandas as pd

series_1 = pd.Series([10, 20, 30, 40])
print(series_1)
print(series_1[1])
#Series с индексами

series_2 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(series_2)
print(series_2["b"])

# Операции
series_3 = pd.Series([1, 2, 3])
print(series_3 + 10)
print(series_3 * 10)


series_4 = pd.Series([10, 20, 30, 40])
print(series_4.mean())
print(series_4.sum())
print(series_4.max())



#========== DataFrame ===========
# DataFrame - это таблица
# строки(индексы)
# столбцы (название колонок)

#Создание DataFrame

data = {
    "name": ["Akyl", "Aktan", "Asan"],
    "age": [23, 20, 18]
}

df = pd.DataFrame(data)
print(df)

# Доступы
# Столбец
print(df["name"])
#Строка
print(df.loc[0])

# Добавление столбца
df["salary"] = [50, 60, 40]
print(df)

# Фильтрация
print(df[df["age"]>18])

#Основныфе методы

print(df.head())
df.info()
print(df.describe())

# ============== Практика =============
# Возвести каждый эллемент в квадрат
series_5 = pd.Series([5, 10, 15, 20])
print(series_5 ** 2)

# вывести среднюю цену
data = {
    "product": ["apple", "banana", 'wotermelon'],
    "price": [45, 120, 150]
}
df = pd.DataFrame(data)
print(df["price"].mean())

# [1, 2, 4, 5] вывести сумму
series_6 = pd.Series([1, 2, 4, 5])
print(series_6.sum())

# вывести тех у кого баллы выше 85
data = {
    "name": ["Anna", "Almaz", "katya"],
    "score": [80, 95, 90]
}

df = pd.DataFrame(data)

print(df[df["score"]>85])

# Добавить столбец "Прошел"
# если балы больше 85 True
# False

df["Прошел"] = df["score"] > 85
print(df)

# Создать DataFrame из 5 людей (имя, возраст)
# средний возрас
# максимальный возраст
# вывести людей старше среднего

data = {
    "name": ["Akyl", "Aktan", "Asan", "Akzhol", "john"],
    "age": [23, 20, 18, 21, 43]
}
df = pd.DataFrame(data)

print(df["age"].mean())
print(df["age"].max())
print(df[df["age"]>df["age"].mean()])