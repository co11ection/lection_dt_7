#=============== структура данных =============

# list1 = []
# for i in range(1, 100001):
#     list1.append(i ** 2)

import numpy as np
import pandas as pd

arr = np.arange(100000)
result = arr ** 2
print(result)

df = pd.DataFrame({"a": range(1000000)})

# Плохой пример !!!!!!!!
# for i in range(len(df)):
#     df.loc[i, "b"] = df.loc[i, "a"]**2
# Правильно!!!!!!!!!! 
# df["b"] = df["a"] ** 2
# print(df)

# apply() - ваш скрытый враг - он является тем же самым циклом
df['b'] = df['a'].apply(lambda x: x**2) # - Плохой пример
# df["b"] = df["a"] ** 2 - Правильно

result = []
# Не правильно!!!!!
# for i in df['a']:
#     if i > 10:
#         result.append(i)

# Правильно использовать пандас\
df_filter = df[df["a"] > 10]
# print(df_filter)

# Правильно использовать numpy
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# result= arr[arr > 3]
# print(result)


df = pd.DataFrame({
    "name": ["Актан", "Асан", "Аяна", "Алмаз", "Никита", "Кадыр", "Яна"],
    "age": [21, 22, 30, 13, 43, 12, 30],
    "income": [300, 800, 100, None, 2000, 500, None],
    "experience": [1, 10, 3, None, 20, 3, 7],
    "educations": ["Доцент", "Бакалавр", None, "Бакалавр", "Магистр", "Доцент", "Бакалавр"],
    "city": ["Бишкек", "Москва", "Пхеньян", "Сеул", "Манас", "Питер", "Мадрид"],
    "hired": [1, 0, 1, 1, 0, 1, 0]
})


df["category"] = ""
# Не правильно!!!!!!!!!!
# for i in range(len(df)):
#     if df.loc[i, "age"] > 18:
#         df.loc[i, 'category'] = "adult"
#     else:
#         df.loc[i, 'category'] = "child"


# where - правильное решение
# df['category'] = np.where(
#     df['age'] > 18,
#     'adult',
#     'child'
# )



# 1) Стянуть датасет титаник
# 2) fare возвести его в квадрат записать в новый столбец fare2
# 3) фильтрация по fare > 100