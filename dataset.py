import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# ---- Задание 1 ------------
data = pd.read_csv('Aids2.csv')
print(data)

# -------- Задание 2 ----------
print("Типах хранящихся в нем данных:\n", data.dtypes)
print("Размер датасета: ", data.size)
print("Размерность датаФрейма: ", data.shape)

# --------- Задание 3 ----------
male = data.loc[data['sex'] == 'M'].shape[0] * 100 / (data.shape[0])
if male > (100 - male):
    print("Больше мужчин: ", male, "%")
else:
    print("Больше женщин: ", 100 - male, "%")

# ----- Задание 4 ----------
man = data.query('sex == "M" & age < 45 & status == "A"').shape[0] / data.query('sex == "M"').shape[0] * 100
print("Процент мужчин до 45 лет, успешно прошедших курс лечения: ", man, "%")

# ---- 5 Задание ----------
data_people_death = data.query('age > 14 & status == "D"')
age = sorted(data_people_death["age"].unique())
dic_age_deaths = {a: count for a in age for count in range(data_people_death.query('age == @a').shape[0]+1)}
data_age_deaths = pd.DataFrame(dic_age_deaths.items(), columns=['Age', 'Deaths'])

lines_1 = data_age_deaths.plot.line(x='Age', y='Deaths')
lines_2 = px.line(data_age_deaths, x="Age", y="Deaths")
# lines2.show()

# --------- 6 Задание ------------
data_people_younger_30 = data.query('age < 30 & status == "D"')
state = data_people_younger_30["state"].unique()
dic_region_deaths = {s: count for s in state for count in range(data_people_younger_30.query('state == @s').shape[0]+1)}
data_region_deaths = pd.DataFrame(dic_region_deaths.values(), columns=['Deaths'], index=state)
plot = data_region_deaths.plot.pie(y='Deaths')
#plt.show()
plt.pie(dic_region_deaths.values(), labels=state)
#plt.show()

# ---- 7 Задание -----
data_death = data.query('status == "D"')
array = []
mean_age = data_death['age'].mean()
for i in state:
    array.append(data_death.query('state == @i')['age'].mean())
ax = pd.DataFrame({'region': array, 'Australia': mean_age}, index=state).plot.bar(rot=0)
# plt.show()

# ---- 8 Задание -----
old_people = []
youth = []
middle = []
for i in state:
    max_age = data_death.query('state == @i')['age'].max()
    min_age = data_death.query('state == @i')['age'].min()
    old_people.append(data_death.query('state == @i').query('age >= 55').shape[0])
    youth.append(data_death.query('state == @i').query('age <= 30').shape[0])
    middle.append(data_death.query('state == @i').query('age >= 31 & age <= 54').shape[0])
    print(i, ": Максимальный возраст - ", max_age, " Минимальный возраст - ", min_age)
old_people_diagramm = pd.DataFrame({'age': old_people}, index=state).plot.bar(rot=0, title="Старики")
# plt.show()
youth_diagramm = pd.DataFrame({'age': youth}, index=state).plot.bar(rot=0, title="Молодые люди")
# plt.show()
middle_diagramm = pd.DataFrame({'age': middle}, index=state).plot.bar(rot=0, title="Люди среднего возраста")
# plt.show()

# ----- 9 Задание -------
categ = data["T.categ"].unique()
dic_categ = {}
for c in categ:
    dic_categ[c] = [data.query('`T.categ` == @c & state == @s').shape[0] for s in state]
diagramma = pd.DataFrame(dic_categ, index=state).plot.bar(rot=0)
#plt.show()


# ----- Задание 10 -----
data_30_A = data.query('status == "A" & age <= 30').shape[0] / data.query("age <= 30").shape[0] * 100
data_31_54_A = data.query('status == "A" & 31 <= age <= 54').shape[0] / data.query("31 <= age <= 54").shape[0] * 100
data_55_A = data.query('status == "A" & age >= 55').shape[0] / data.query("age >= 55").shape[0] * 100
print("Группа младше 30: процент живых - ",data_30_A,"%, процент мертвых - ", 100-data_30_A,"%")
print("Группа от 31 до 54: процент живых - ",data_31_54_A,"%, процент мертвых - ", 100-data_31_54_A,"%")
print("Группа старше 55: процент живых - ",data_55_A,"%, процент мертвых - ", 100-data_55_A,"%")

print("Таких групп нет")
