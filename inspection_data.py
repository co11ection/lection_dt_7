#===================== Инспекция данных и первичный диагностика =========

#1 Структура DataFrame
# DataFrame - это структура данных в pandas. 
# Это таблица в которой каждая 
# 1)строка - одно наблюдение(один пасажир)
# 2)а каждый столбец  - признак(возраст, пол и тд)
# 3)индекс - номер строки
# 4)ячейка - одно конкретное значение на пересечении строки и столбца

# Типы данных в pandas
# int64 - целые числа - 0 ... бесконечности - возраст, цена, количество - среднее,сумма,мин\макс
# float64 - дробные числа (числа с плавающей точкой) - 0.5, 15.7 - цена, рост, вес - среднее, медиана
# object - str(Текстовое) - пол, имя и тд - value_counts(), unique()
# bool - булевое(логическое) - True, False - выжил? активен?  - sum()
# datetime64 - дата и время - 2024-01-01 - дни рождения, день проишествия - разница в датах, групировка
# category - Категории - Классы, рейтинг, размер - value_counts(), cat.codes

#!!!!!!!!!!!!!!!!!ВАЖНО!!!!!!!!!!!!!!!!!!!!!!!!
# df.dtypes - позволяет проматривать какие типы данных есть
# pd.to_numeric() - если число приходит как object - переводит с object на int64
# pd.to_datetime() - если дата приходит как строка - перводит с object на datetime64

# возраст -> 24 <- 24 лет

# ============================ Команды инспекции ================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# 1 размерность строки Х столбцы
print(df.shape) # 891 x 15
# 2 список всех сталбцов
print(df.columns)
# тип каждого столбца
print(df.dtypes)
# первые три строки
print(df.head(3))
# последние 3 строки
print(df.tail(3))
# вытащить 5 случайных строк
print(df.sample(5))
# типы данных + non-null количество
print(df.info())
# статистика числовых
print(df.describe().round(1))
print(df[df["survived"]>0].describe())
# Кол-во уникальных
print(df.nunique())
# Частоста каждого значения
print(df["sex"].value_counts())

# ============ Практика ===============
tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.columns)
print(tips.dtypes)
print(tips.info())
print(tips.describe().round(3))
print(tips["total_bill"].value_counts())

# Пропуски  и типы пропусков
# пропуски - это пустые ячейки в таблице(NaN, null, None)
#1) MCAR - missing comletely at random - полностью случайные
#2) MAR - missing at random - случайные но зависимые
#3) MNAR - missing not at random - не случайные

# Стратегия работы с пропусками
# 1) удалить строки
# print(df.dropna()) - # мало пропусков < 5%
# 2) заполнить средним
print("средний возраст")
print(df["age"].mean())
print(df["age"].fillna(df["age"].mean())) # - числовые, MCAR 5-30%
# 3) Заполнить медианой
print(tips["tip"].fillna(tips["tip"].median())) # Есть выбросы, 5-30% 
# 4) Заполнить модой 
print(df)
# print(df["deck"].fillna(df["deck"].mode()[0])) # Категорий, 5-30%
# 5) Удалить столбец  >50%
print(df)
print(df.drop("deck", axis=1))

# ============= Выбросы ================
# выбросы - значение которое сильно отличается от остальных. Например большинство билетов продано от 10 до 50 $ 
# но один продали за 1000$ - это выброс. НЕ ВСЕ ВЫБРОСЫ ЯВЛЯЮТСЯ ОШИБКАМИ!!!! это может быть vip-каюта


# Методы нахождения выбросов
# IQR - разница между третьим и первым квантилем. Значение считается выбросом, если оно выходит за границы
# 25 50 75
# Q1 Q2 Q3
# IQR = q3 - q1
# нижняя граница =  q1 - 1.5 * IQR
# верхняя граница = q3 + 1.5 * IQR

q1 = df["fare"].quantile(0.25)
q3 = df["fare"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("lower", lower)
print("upper", upper)
outliers = df[(df["fare"]<lower) | (df["fare"]>upper)]
print(outliers)

# Методы Z-score
# Z-score -  показывает, на сколько стандартных отклонений значение отличается от среднего
# если |Z| > 3(дальше трех сигм) значение считается выбросом
# std - стандартное отклонение

# 165 166 167 168
# std = 1.5

# 150 170 190 200 210 300
# 184
# std = 30
# сигма = 30
# 3 сигма = 90
# std = |среднее значение - min| |max - среднее значение| 
 
# Z = (x - mean) / std
# x - значение (например цена на билет fare)
# mean - среднее значение
# std - стандартное отклонение

from scipy import stats
z_score = stats.zscore(df["fare"].dropna())
print(z_score)
outliers = df[abs(z_score) > 3]

print(outliers)