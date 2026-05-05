# =========== Автомптизированный EDA отчет ===================

#Sweetviz - библиотека для автомотизированного анализа
""" 
строит визуальные отчеты
показывает распределение
выевляет пропуски 
сравнивать датасеты
находить зависимости между признаками(столбцы)
"""

#  pip install sweetviz

import pandas as pd
import seaborn as sns
import sweetviz as sv

df = sns.load_dataset("titanic")

print(df.head())

# Полноценный анализ
# report = sv.analyze(df)
# report.show_html("titanic_report.html")

# Анализ с таргетом
# report = sv.analyze(df, target_feat="survived")
# report.show_html("titanic_target.html")

#Анализ сравнения двух датасетов
# df = df.drop(columns=['adult_male'])
# male = df[df['sex'] == 'male']
# female = df[df['sex'] == 'female']
# report = sv.compare([male, "Мужчины"], [female, "Женщины"])
# report.show_html("titanic_compare.html")

#Выборочный анализ
# report = sv.analyze(
#     df[['age', 'fare', 'pclass', 'survived']]
# )

# report.show_html("titanic_select.html")


#Работа с пропущенными значениями
print(df.isnull().sum())

df['age'] = df['age'].fillna(df['age'].median())

report = sv.analyze(df)
report.show_html("no_mising_report.html")


