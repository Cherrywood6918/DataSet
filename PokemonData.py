import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv('Pokemon.csv')
print(data)

# Узнайте информацию о размере датасета и типах хранящихся в нем данных.

data_type = data.dtypes
print("Тип данных:\n", data_type)
data_size = data.size
print("Размер ДатаСета: ", data_size)
data_row = data.shape[0]
data_columns = data.shape[1]
print("Количество строк: ", data_row, " Количетсво столбцов: ", data_columns)

# Построить круговую диаграмму, отражающую процентное соотношение
# покемонов первого поколения, проведя распределение по их типам.
data_Pokemon_Gen_1 = data.query('Generation == 1')
print(data_Pokemon_Gen_1)

# Основываясь на информации из датасета, выяснить, кого больше в процентном  соотношении:
# Легендарных покемонов или .
