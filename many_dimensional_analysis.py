# ===================== Многомерный анализ ===================
# Многомерный анализ - это иследование взаимосвязей между 3 или более переменными одновременно
# Цель: найти скрытые структуры, убрать лишнее, понять главное


# Снижение размерности - из 100 признаков оставить 10 без потери главной информации
# Отбор признаков - какие переменные важны для модели, а что является обычным шумом
# Обноружение мультиколлинерности - это когда признаки дублируются
# Класстеризация - группировка обьектов по множеству признаков сразу
# Визуализация высокоразмерных данных - как показать 10 измерений на 2Д экране



import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy import stats 
  
# -- Датасет 1: iris (ирисы Фишера) -- 
iris = sns.load_dataset('iris') 
 
  
# -- Датасет 2: penguins (пингвины Палмера) -- 
penguins = sns.load_dataset('penguins').dropna() 
 
  
# -- Датасет 3: diamonds (бриллианты) -- 
diamonds = sns.load_dataset('diamonds') 
 
  
# -- Датасет 4: California Housing -- 
from sklearn.datasets import fetch_california_housing 
housing = fetch_california_housing(as_frame=True).frame 
 
  
# -- Датасет 5: Wine (вина) -- 
from sklearn.datasets import load_wine 
wine_data = load_wine(as_frame=True) 
wine = wine_data.frame


# Матрица корреляции - взгляд на все связи сразу
# Матрица корреляции - это таблица, где на пересечении каждой пары переменны стоит их поэфицент корреляции

corr_matrix = wine.drop("target", axis=1).corr()
print(corr_matrix)

# plt.figure(figsize=(12,10))
# sns.heatmap(
#     corr_matrix, annot=True, fmt=".2f",
#     vmin=-1, vmax=1, center=0,
#     cmap="RdBu_r", square=True, linewidths=0.5
# )
# plt.title("Матрицв корреляции")
# plt.tight_layout()
# plt.show()

# Показать половину матрицы
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
# plt.figure(figsize=(12,10))
# sns.heatmap(
#     corr_matrix, mask=mask, annot=True,
#     fmt=".2f", center=0, square=True, cmap="RdBu_r"
# )
# plt.title("Только нижний")
# plt.tight_layout()
# plt.show()

# Находим самые сильные корреляции программно

corr_pairs = (
    corr_matrix.where(np.triu(
        np.ones_like(corr_matrix, dtype=bool), k=1
    )).stack().reset_index()
)
# triu  - возврат нижней половины
# one_likes - деление по диагонали
# stack - обьединяет по парам
# reset_index - возвращает индекс
corr_pairs.columns = ["var1", "var2", "correlation"] # название колонок
corr_pairs["abs_corr"] = corr_pairs["correlation"].abs() # добавили новую колонку abs_corr

# top 10

top10 = corr_pairs.nlargest(10, "abs_corr") # фильтрация 10 наисельнейших связей(корреляций)
print(top10)


# Мультиколлинеарность - это ситуация, когда один признак можно предсказать по другим. 
# напимер площадь м^2 и площадь в футах. Оно мешает моделям ML и искожает коэфиценты регресии

# Модель не может разделить эффекты - если два признака почти одинаковые, коэфицент становится нестабильным
# Растет дисперсия оценок - p_value завышается, важные признакие кажутся незначительные
# Модель переобучается - лишние данные добавляет шум, но не информацию


# обноружение: VIF
# VIF - показывает, на сколько каждый признак предсказывается остальными
# VIF = 1 - нет коллинериальности
# VIF = 5 -10 - умеренная
# VIF > 10 сильная. нужно удалять признаки

# from statsmodels.stats.outliers_influence import variance_inflation_factor

# print(housing)
# x = housing.drop("MedHouseVal", axis=1)

# x_scaled = (x - x.mean())/x.std() # Стандартизация

# VIF_data = pd.DataFrame(
#     {
#         "feature": x_scaled.columns,
#         "VIF": [variance_inflation_factor(x_scaled.values, i) for i in range(x_scaled.shape[1])]
#     }
# )

# print(VIF_data.sort_values("VIF", ascending=False))


# Pairplot - все пары в одном графике
# pairplot - сетка графиков, где каждая пара переменных показана как scatter plot, 
# а на диоганали распределение каждой переменной. Расскараска по категориям

# sns.pairplot(
#     iris, hue="species", diag_kind='kde', plot_kws={"alpha": 0.6}   
# )
# plt.title("Pairplot")
# plt.show()

# # print(penguins.columns)
# sns.pairplot(
#     penguins, 
#     hue='species',
#     vars=[
#         'bill_length_mm',
#         "bill_depth_mm",
#         "flipper_length_mm",
#         "body_mass_g"
#     ],
#     diag_kind="kde", palette="Set2",
#     plot_kws={"alpha": 0.5}
# )
# plt.show()



penguins = penguins.dropna() # Удаляет строки с пропусками None/NaN/null
print(penguins.describe())

# Scaling
# Решает проблему: разные масштабы ломают алгоритмы
# Пример:
# рост = 183
# зарплата - 200 000 сом

# Виды масштабирования:
# standartScaler - среднее, дисперсия - почти всегда
# MinMaxScaler - значение между [0,1] - для нейросетей, картинок
# RobustScaler - устойчив к выбросам - если есть выбросы

# Если не знаете что брать берем StandartScaler

from sklearn.preprocessing import StandardScaler, MinMaxScaler

penguins_data = penguins[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]

print(penguins_data)

standart = StandardScaler() # Создали обьект от класса стандарт скалер

penguins_scalled = standart.fit_transform(penguins_data)
print(penguins_scalled)
# 1) изучает данные (считает среднее и std для каждой колонки)
# 2) применяет формулу (x- mean) / std

penguins_df = pd.DataFrame(penguins_scalled, columns=penguins_data.columns)
print(penguins_df)
print(penguins_df.describe())


minmax_scaller = MinMaxScaler()
penguins_minmax = minmax_scaller.fit_transform(penguins_data)
# (x - min)/(max - min)
penguins_df = pd.DataFrame(penguins_minmax, columns=penguins_data.columns)
print(penguins_df) 
print(penguins_df.describe())


# Feature Selection
# решает проблемы такие как:
# лишние признаки, выбросы - ШУМ -> модель начинает путаться
# дубли - две одинаковые колонки
# больше признаков = дольше обработка и обучение

# Нам нужно оставить только полезные признаки  


penguins_corr = penguins.corr(numeric_only=True)

plt.figure(figsize=(4, 4))
sns.heatmap(
    penguins_corr,
    annot=True,
    cmap='RdBu_r',
    fmt=".2f"
)
plt.title("Корреляция")
plt.show()

# Удаление дубликатов
penguins_corr = penguins.corr(numeric_only=True).abs()
# знак не важен - нам важна сила связи

mask = penguins_corr.where(
    np.triu(
        np.ones(penguins_corr.shape),
        k=1
    ).astype(bool)
)
# where - оставляет значение там где условие проверки выдает True
# triu - оставляет один треугольник

to_drop = [
    column for column in mask.columns
    if any(mask[column] > 0.8)
]
print("Колонки для удаления", to_drop)

clen_data = penguins.drop(columns=to_drop)
print(penguins.shape)
print(clen_data.shape)

from sklearn.feature_selection import mutual_info_regression
#Mutual Information - измеряет любую связь а не только линейную

target = penguins['body_mass_g']
features = penguins[["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]]

mi = mutual_info_regression(features, target)

data = pd.Series(
    mi, index=features.columns
)
data_sort = data.sort_values(ascending=False)
print("MI")
print(data_sort)