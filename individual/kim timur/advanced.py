# -------------- Feature engenering ---------------
""" 
EDA -> изучение дата сета и понимание что не так
Feature engenering -> решить что с ними делать
Модель - обучение

Ошибки новичков: сразу начинают использовать fillna, не поняв в чем дело

Решение:
что не так с данными?
как это повлдияет на модель?
как это исправить?
"""

import pandas as pd
import numpy as np


df = pd.DataFrame({
    "name": ["Актан", "Асан", "Аяна", "Алмаз", "Никита", "Кадыр", "Яна"],
    "age": [21, 22, 30, None, 43, None, 30],
    "income": [300, 800, 100, None, 2000, 500, None],
    "experience": [1, 10, 3, None, 20, 3, 7],
    "educations": ["Доцент", "Бакалавр", None, "Бакалавр", "Магистр", "Доцент", "Бакалавр"],
    "city": ["Бишкек", "Москва", "Пхеньян", "Сеул", "Манас", "Питер", "Мадрид"],
    "hired": [1, 0, 1, 1, 0, 1, 0]
})

# print(df)

print(df.isnull().sum()) # Колличество пропусков по столбцам
# Что не так с нашим дата сетом
""" 
пропуски с числами
пропуски с категориями
нет полезных признаков
Модель не принимает строки
"""

# Шаг 1 Пропуски
""" 
Есть выбросы - mediana
все нормально - mean
категория - mode
"""

print(df.describe())

df['age'] = df['age'].fillna(df['age'].mean())
df['income'] = df['income'].fillna(df['income'].median())
df["experience"] = df["experience"].fillna(df["experience"].median())

df['educations'] = df['educations'].fillna(df['educations'].mode()[0])
print(df)
print(df.isnull().sum())


# Категории
""" 
Типы категории
Номенальные - city
Порядковые - educations
"""

# Порядковые
educations_map = {
    "Бакалавр": 1,
    "Магистр": 2,
    "Доцент": 3
}

df['educations'] = df['educations'].map(educations_map)
print(df)

# Номенальные
df = pd.get_dummies(df, columns=['city'], dtype=int)
print(df)

print(df.dtypes)


# Feature enginering
# Помогает искомое значение target

# Доход на опыт
df["income_per_experiense"] = df['income'] / df['experience']
# 1000$ при опыте 1 год != 1000$ за 10 лет

# возраст на опыт
df['age_per_experiense'] = df['age'] / df['experience']
# Может показать поздний старт

threshold = df['income'].median()
df['hight_income'] = (df['income']>threshold).astype(int)
print(df[["name", 'income', "hight_income"]])

# Иногда признаки(колонки\столбцы) вы создаете на всякий случай,
# по причине что модели любя простые правила

# Финальная проверка
# Перед моделью проверить стоит:
""" 
Нет ли None
нет ли строк
нет странных значений (выбросов\аномалий)
"""

df = df.drop(columns="name")
print(df)

print(df.dtypes)
print(df.isnull().sum())
print(df.describe())

# Ошибка которую допускают зачастую
# НЕЛЬЗЯ ИСПОЛЬЗЛОВАТЬ TARGE при создании признаков
# print(df.groupby("city")['hired'].mean())

# Разделение данных

y = df["hired"]
x = df.drop(columns=['hired'])