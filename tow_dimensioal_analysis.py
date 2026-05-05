# ===================== Двумерный анализ ========================
# Двумерный анализ - это иследование взаимосвязи двух переменных одновременно
# мы смотрим если одна переменная меняется, что произойдет со второй

# Типы кобинации
#1) число + число - метод коряляции(пирсона, спирмена)  - пример: конечный счет и чаевые
#2) категория + категория - выживаемость и класс (датасет титаник)
#3) категория + число - выживаемость и возраст(датасет титаник)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#DataFrame Tips
tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.columns)
# print(tips.head())
# print(tips.tail())

#DataFrame diamonds
diamonds = sns.load_dataset("diamonds")
print(diamonds.shape)
print(diamonds.columns)


#DataFrame titanic
titanic = sns.load_dataset("titanic")
print(titanic.shape)
print(titanic.columns)

#DataFrame california
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing(as_frame=True)
housing = california.frame
print(housing.shape)
print(housing.columns)


# Корреляция - это связь между двумя переменными.
# Обозначается буквой r и принимает значение в диапазоне от -1 до 1
# 1 -  идеальное положительная связь
# 0.7 - 0.9 - сильная положительная мвязь - карат - цена
# 0.4 - 0.7 - умеренная положительная связь - конечный чек - чайвые
# 0.1 - 0.4 - слабая положительная связь - 
# 0 - нет связи
# -0.4 - -0.7 - умеренная отрицательная связь 
# -1 - идеальной отрицательная связь

# Пирсона = r = сумма((Xi - X_mean)(Yi - y_mean)) / корень(сумма(Xi-x_mean)**2 * сумма(Yi - y_mean)**2)
# Xi - каждый элемент первого столбца
# Yi - каждый элемент второго столбца

# Спирмена  r = 1 - (
#    (6 * сумма(Di**2))/ n(n**2-1)  
# )
# Di = rank(Xi) - rank(Yi)

# x = [10, 20, 30] - [1, 2, 3]
# y = [100, 50, 200] - [2, 1, 3]

# # Метод Пирсона
# from scipy import stats
# r_pearson, p_value = stats.pearsonr(tips["total_bill"], tips["tip"])
# print(r_pearson)
# print(p_value)

# # Метода Спирмена
# r_sperman, p_value = stats.spearmanr(tips['total_bill'], tips['tip'])
# print(r_sperman)
# print(p_value)

# # ---------- Матрица  Корреляций ---------
corr_matrix = tips.select_dtypes(include="number").corr() 
# print(corr_matrix)

# # Корриляция не равно причина-следствию 


# # Тепловая карта корреляции

# corr_matrix = housing.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(
#     corr_matrix,
#     annot=True,
#     fmt=".2f",
#     cmap="RdBu_r",
#     center=0,
#     vmin=-1, vmax=1,
#     square=True,
#     linewidths=0.5
# )
# plt.title("Тепловая корреляция")
# plt.tight_layout()
# plt.show()


# #Визуализация взаимосвязей
# # Базовая
# plt.figure(figsize=(8,6))
# sns.scatterplot(data=tips, x="total_bill", y='tip', alpha=0.6)
# plt.xlabel("Сумма счета")
# plt.ylabel("Чаевые")
# plt.title("Tips зависимость чаевых от суммы счета")
# plt.show()

# # с линией тренда
# sns.lmplot(
#     data=tips, 
#     x='total_bill',
#     y='tip',
#     height=6,
#     aspect=1.3,
#     scatter_kws={'alpha': 0.5},
#     line_kws={"color": "red"}
# )
# plt.title("Чаевые vs сумма счета")
# plt.show()

# Разбивка на категории
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue='time', style="sex", alpha=0.6)
# plt.title("Чаевые vs общая сумма(по времени и по полу)")
# plt.show()


# anscombe = sns.load_dataset("anscombe")
# g = sns.lmplot(data=anscombe, x="x", y="y",
#                col="dataset", col_wrap=2,
#                height=3.5, aspect=1.2,
#                scatter_kws={'alpha': 0.7}
# )
# g.figure.suptitle("Квартет Аскомба", y=1.02)
# plt.show()


#СНАЧАЛА СТРОЙ ГРАФИК, ПОТОМ СЧИТАЙ СТАТИСТИКУ. НИКОГДА НАОБОРОТ

# ===========Категория + число ========
# отличается ли чаевые курящих и не курящих
# в каие дни сколько общая сумма

# 1 Группировка и описательная статистика
# print(tips.groupby("smoker")["tip"].agg(["mean", "median", "std", "count"]))

# print(tips.groupby("day")["total_bill"].mean())

# Визуализация
# plt.figure(figsize=(8,5))
# sns.boxplot(data=tips, x="day", y="total_bill", palette="Set2")
# plt.title("Распределение суммы")
# plt.show()


# ============ Категория + Категория ===============
# выживаемость vs класс
ct = pd.crosstab(titanic["survived"], titanic["pclass"])
print(ct)

# В процентай по столбцу
ct_prs = pd.crosstab(titanic["survived"], titanic["pclass"], normalize="columns") * 100
print(ct_prs.round(1))


# Тест Xi^2
# Xi^2 = сумма((O - E)**2/ E)
# O - данные с которыми работаем
# E = N(summ_row)(summ_columb)/N

from scipy.stats import chi2_contingency

ct = pd.crosstab(titanic["survived"], titanic["pclass"])
chi2, p_value, dof, expected = chi2_contingency(ct)
print(chi2)
print(f"{p_value:.6f}")
print(dof)

# p_value < 0.5 - то первая переменная зависит от второй переменной
# p_value >= 0.5 - то переменная не зависит друг от друга


# Статистическкие тесты (для сравнения групп)

# если на самом деле различий нет то 
# p_value < 0.5 -> различие значимо(обоим переменным)
# p_value>=0.5 -> не уверенность

# выбор теста
# 2 группы - данные нормальные - t-test
# 2 группы - данные не нормальные - Mann-whitney U
# 3 группы + - данные нормальные - ANOVA
# 3 группы + -  данные не нормальные - Kruskal_Wallis


# T_test

smoker = tips[tips['smoker']== "Yes"]["tip"]
non_smoker = tips[tips['smoker']== "No"]["tip"]

print("smoker",smoker)
print("non_smoker", non_smoker)

# Шаг 1 : Проверка нормальности данных
from scipy import stats
_, p_s = stats.shapiro(smoker)
_, p_ns = stats.shapiro(non_smoker)
print(f"Нормальность курящих  {p_s:.4f}")
print(f"Нормальность не курящих {p_ns:.4f}" )
# p > 0.05 - данные считаются нормальными
# p< 0.05 - данные считаются ненормальные

# шаг 2 
u_stat, p_value = stats.mannwhitneyu(
    smoker, non_smoker, alternative="two-sided"
)

print(f"Статистика. {u_stat:.2f}")
print(f"{p_value:.4f}")


t_stat, p_t = stats.ttest_ind(smoker, non_smoker)

print(f"T статистика: {t_stat:.4f}")
print(f"T p_value: {p_t:.4f}")

# Визуализация
# Boxplot - унивирсальный (подходит всегда)
# Violin - Важное распределение 
# Swarm - когда данные < 200
# Bar plot - для презентаций


#Violin
# plt.figure(figsize=(8,5))
# sns.violinplot(
#     data=tips, x="day", y="total_bill",
#     palette="muted"
# ) 

# plt.title("Распределение суммы счета по дням")
# plt.show()


# SWARM plot
# plt.figure(figsize=(8,5))
# sns.swarmplot(
#     data=tips, x="smoker", y="tip"
# )
# plt.title("Чаевые")
# plt.show()


# Практика 

# 1. Scatter plot: total_bill (X) vs tip (Y). 
# 2. Корреляция Пирсона и Спирмена. 
# 3. Линия тренда (sns.lmplot). 
# 4. Heatmap корреляций всех числовых столбцов. 
# Вопрос: Насколько сильна связь? Логична ли она?


# Шпаргалка

# Определить тип переменных
# Строи график
# описательные статистики(среднее, медитана, корреляция)
# проверка условий - нормальность\выбросы\ размер выборки
# провести тесты - ttest, Xi^2 ..
# Оценить размер эфекта - корреляции
# вывод


# Корреляция не равно причине