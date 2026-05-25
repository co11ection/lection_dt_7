# ============== Автоматический анализ ============
# Sweetviz - библиотека для автоматического анализа
""" 
строит визуальные отчеты
показывает распределение 
выевлять пропуски
сравнивать признаки
находить зависимомти между признаками
"""
# pip install sweetviz

import pandas as pd
import seaborn as sns
import sweetviz as sv

df = sns.load_dataset("titanic")
print(sns.get_dataset_names())

# print(df.head())

# Полноценный анализ
# report = sv.analyze(df)
# report.show_html("titanic_report.html")

# Анализ с таргетом
# report = sv.analyze(df, target_feat="survived")
# report.show_html("titanic_target.html")

# Анализ двух датасетов
# df = df.drop(columns=["adult_male"])
# male = df[df["sex"] == 'male']
# female = df[df['sex'] == 'female']
# report = sv.compare([male, "Мужчины"], [female, "Женщины"])
# report.show_html("titanic_compare.html")

# выборочный анализ 
# report = sv.analyze(
#     df[["age", "fare", "pclass", "survived"]]
# )
# report.show_html("titanic_select.html")

# print(df.isnull().sum())

# df['age'] = df['age'].fillna(df['age'].median())
# report = sv.analyze(df)
# report.show_html("no_missing_titanic.html")