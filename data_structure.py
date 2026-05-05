#================= Структура данных ==============

# list1 = []
# for i in range(1, 1000001):
#     list1.append(i ** 2)
    
import numpy as np
import pandas as pd


# arr = np.arange(1000000)
# result = arr ** 2


# df = pd.DataFrame({"a": range(1000000)})
# df["b"] = 0
# # плохой пример
# for i in range(len(df)):
#     df.loc[i, "b"] = df.loc[i, 'a'] ** 2
# #правильно
# df["b"] = df['a'] ** 2


# # apply() - ваш скрытый враг - по причине того что он тот же самы цикл

# df['b'] = df['a'].apply(lambda x: x**2)# - плохой пример

# df["b"] = df['a'] ** 2 # - правильно


# result = []
# # не правильно
# for i in df['a']:
#     if i > 10:
#         result.append(i)
        
# # правильно pandas
# df_filter = df[df["a"]>10]

# # правильно numpy
# arr = np.array([1, 2, 3, 4, 5, 6])
# result = arr[arr > 3]

# df = pd.DataFrame({
#     "name": ["Актан", "Асан", "Аяна", "Алмаз", "Никита", "Кадыр", "Яна"],
#     "age": [21, 22, 30, 13, 43, 12, 30],
#     "income": [300, 800, 100, None, 2000, 500, None],
#     "experience": [1, 10, 3, None, 20, 3, 7],
#     "educations": ["Доцент", "Бакалавр", None, "Бакалавр", "Магистр", "Доцент", "Бакалавр"],
#     "city": ["Бишкек", "Москва", "Пхеньян", "Сеул", "Манас", "Питер", "Мадрид"],
#     "hired": [1, 0, 1, 1, 0, 1, 0]
# })


# df["category"] = ''
# # не правильно
# for i in range(len(df)):
#     if df.loc[i, 'age'] > 18:
#         df.loc[i, "category"] = 'adult'
#     else:
#         df.loc[i, 'category'] = 'child'
        

# # where - правильно

# df['category'] = np.where(
#     df['age'] > 18,
#     'adult',    
#     'child'
# )

# # работа с пропусками
# # не правильный

# for i in range(len(df)):
#     if pd.isna(df.loc[i, 'age']):
#         df.loc[i, "age"] = df["age"].median()

# # правильно
# df["age"] = df['age'].fillna(df['age'].median())

import seaborn as sns
df = sns.load_dataset("titanic")
print(df.info())
df['pclass'] = df['pclass'].astype("int8") # уменьшили память
df['sex'] = df['sex'].astype("category") # категория быстрее и легче по памяти

print(df.info())


# 1 fare возвести в квадрат и создать новый ключт fare2
# 2 категория по возрасту 
# 3 фильтрация fare > 100

# 1
# df["fare2"] = df["fare"] ** 2
# # 2
# df['age_category'] = np.where(
#     df['age'] > 18,
#     'adult',
#     'child'
# )
# rich = df[df["fare"]>100]
# print(df)
# print(rich)