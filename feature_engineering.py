# ============== Feature Engineering ======================
"""
Eda -> изучение дата сета и понимание что не так
Feature Engineering - решить что с ними делать
Модель - обучение

Ошибка новичков: сразу использорвать fillna, не поняв в чем дело

Решение:
Что не так с данными?
Как это повлияет на модель?
Как это исправить?
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

print(df)

print(df.isnull().sum()) # колличество пропусков по столбцам
# Что не так в нашем дата сете
"""
Пропуски с числами
пропуски с категорими
Нет полезных признаков
Модель не принимает строки
"""
# Шаг 1 Пропуски

"""
есть выбросы - meadian
все нормально - mean
категория - mode
"""

print(df.describe())

df['age'] = df["age"].fillna(df['age'].mean())
df["income"] = df['income'].fillna(df['income'].median())
df["experience"] = df["experience"].fillna(df["experience"].median())

df["educations"] = df["educations"].fillna(df["educations"].mode()[0])

print(df)
print(df.isnull().sum())

# Шаг 2 Категории

"""
Типы категорий

Номенальные - city
Порядковые - educations
"""

# Порядковые
educaation_map = {
    "Бакалавр": 1,
    "Магистр": 2,
    "Доцент": 3
}

df["educations"] = df['educations'].map(educaation_map)
print(df)

# Номинальная
df = pd.get_dummies(df, columns=['city'], dtype=int)
print(df)

print(df.dtypes)


# Feature Engineering
# Почему он помогает предсказать target(Искомое значение или результат)

# Доход на опыт
df["income_per_experience"] = df['income'] / df['experience']
# 1000$ при опыте 1 год != 1000$ через 10 лет

# возраст на опыт
df["age_per_experience"] = df['age'] / df['experience']
print(df[['name', "age", "experience", "age_per_experience"]])
# Может показать поздний страт

threshold = df['income'].median()
print(threshold)
df["high_income"] = (df["income"]>threshold).astype(int)
print(df[["name", "income", "high_income"]])

# Иногда признаки(колонки\столбцы) вы создаете на всякий случай, по причине что модели любят простые правила

# Финальная проверка
# перед моделью надо просмотреть:
"""
Нет ли None
нет ли строк
нет странных значений (выбросы\анамалии)
"""



df = df.drop(columns="name")
print(df)

print(df.isnull().sum())
print(df.dtypes)
print(df.describe())


# Ошибка которая допускает зачастую
# НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ TARGE ПРИ СОЗДАНИИ ПРИЗНАКОВ

# print(df.groupby("city")["hired"].mean())

# Разделение данных

y = df['hired']

x = df.drop(columns=['hired'])