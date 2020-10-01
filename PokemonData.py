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

# Подсчитать какой тип покемонов преобладает в каждом поколении
# Результат  представьте гистограммой с группировкой.
list_Pokemon_Gen = data['Generation'].unique()
list_Pokemon_Type = data['Type 1'].unique()
for gen in list_Pokemon_Gen:
    dic_Pokemon_Type = {type: count for type in list_Pokemon_Type for count in
                        range(data.query("(`Type 1` == @type | `Type 2` == @type) & Generation == @gen").shape[0] + 1)}
    var = pd.DataFrame({'Количество покемонов': dic_Pokemon_Type.values()}, index=list_Pokemon_Type).plot.bar(rot=0,
                                                                                                              title="Поколение " + str(
                                                                                                                  gen))
# plt.show()

# Основываясь на информации из датасета, выяснить, соотношения легендарных и обычнх покемонов
# Результат представить в круговой диаграмме
legendary = data.query('Legendary == True').shape[0]
df = pd.DataFrame({'pokemons': [legendary, data.shape[0] - legendary]},
                  index=['Legendary', 'NotLegendary'])
plot = df.plot.pie(y='pokemons')
# plt.show()


# Определить самого сильного и самого слабого покемона в каждом поколении, если их несколько, то вывести всех
for gen in list_Pokemon_Gen:
    max_total = data.query('Generation == @gen')['Total'].max()
    min_total = data.query('Generation == @gen')['Total'].min()
    Pokemon_strong = data.query('Total == @max_total & Generation == @gen')['Name'].values
    Pokemon_weak = data.query('Total == @min_total & Generation == @gen')['Name'].values
    print("GENERATION ", gen)
    print("Cамый сильный покемон: ", ', '.join(Pokemon_strong), " c суммой характеристик -", max_total)
    print("Cамый cлабый покемон: ", ', '.join(Pokemon_weak), " c суммой характеристик -", min_total)

# Какой процент покемонов имееют два типа
type_nan = pd.isnull(data).sum()['Type 2'] * 100 / data["Type 2"].shape[0]
print("Покемоны имеют два типа ", type_nan, "%")
print("Покемоны имеют один тип ", 100 - type_nan, "%")

# Подсчитать среднее значение HP водных покемонов каждого поколения и за все время в целом.
# Результат  представьте гистограммой с группировкой.
data_pokemon_water = data.query('`Type 1` == "Water" | `Type 2` == "Water"')
print(data_pokemon_water)  # Проверка
gen_pokemon_hp = []
mean_HP_Pokemon_Water = data_pokemon_water['HP'].mean()
for gen in list_Pokemon_Gen:
    gen_pokemon_hp.append(data_pokemon_water.query('Generation == @gen')['HP'].mean())
print(pd.DataFrame({'generation': gen_pokemon_hp, 'all': mean_HP_Pokemon_Water}))  # Проверка
ax = pd.DataFrame({'generation': gen_pokemon_hp, 'all': mean_HP_Pokemon_Water}, index=list_Pokemon_Gen).plot.bar(rot=0)
plt.show()
