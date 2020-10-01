import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv('Aids2.csv')
print(data)

data_type = data.dtypes
print("Типах хранящихся в нем данных:")
print(data_type)

data_size = data.size
print("Размер датасета")
print(data_size)

data_frame = data.shape
print("Размерность датаФрейма")
print(data_frame)

male = data.loc[data['sex'] == 'M'].shape[0]
print("MALE")
print(male)

female = data.loc[data['sex'] == 'F'].shape[0]
print("FEMALE")
print(female)
print("Male: ", male * 100 / (data_frame[0]), "%")
print("Female: ", female * 100 / (data_frame[0]), "%")

man = data.query('sex == "M" & age < 45 & status == "A"').shape[0] / data.query('sex == "M"').shape[0] * 100
print("Процент мужчин до 45 лет, успешно прошедших курс лечения: ", man, "%")

# ---- 5 Задание ----------
data_people_death = data.query('age > 14 & status == "D"')
print(data_people_death)
age = sorted(data_people_death["age"].unique())
print(age)
dic1 = {a: count for a in age for count in range(data_people_death.query('age == @a').shape[0])}
print(dic1)
data_new1 = pd.DataFrame(dic1.items(), columns=['Age', 'Deaths'])
print(data_new1)

lines1 = data_new1.plot.line(x='Age', y='Deaths')
lines2 = px.line(data_new1, x="Age", y="Deaths")
# lines2.show()

# ---- 6 Задание ------------
data_people_younger_30 = data.query('age < 30 & status == "D"')
print(data_people_younger_30)
state = data_people_younger_30["state"].unique()
print(state)
dic2 = {s: count for s in state for count in range(data_people_younger_30.query('state == @s').shape[0])}
print(dic2)
data_new2 = pd.DataFrame(dic2.items(), columns=['State', 'Age']).set_index("State")
print(data_new2)
plot = data_new2.plot.pie(y='Age')
# plt.show()
plt.pie(dic2.values(), labels=state)
# plt.show()

# ---- 7 Задание -----
data_death = data.query('status == "D"')
print(data_death)
array = []
mean_age = data_death['age'].mean()
for i in state:
    array.append(data_death[data_death.state == i]['age'].mean())
print(array)
print(pd.DataFrame({'region': array, 'ausrtalia': mean_age}))
ax = pd.DataFrame({'region': array, 'ausrtalia': mean_age}, index=state).plot.bar(rot=0)
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
print(categ)
for i in state:
    dic3 = {c: count for c in categ for count in range(data.query('`T.categ` == @c & state == @i').shape[0])}
    var = pd.DataFrame({'count': dic3.values()}, index=categ).plot.bar(rot=0, title=i)
    #plt.show()
    print(dic3)

# ----- Задание 10 -----
data_30_D = data.query('status == "D" & age <= 30').shape[0]/data.query("age <= 30").shape[0]*100
data_30_A = data.query('status == "A" & age <= 30').shape[0]/data.query("age <= 30").shape[0]*100
data_31_54_A = data.query('status == "A" & 31 <= age <= 54').shape[0]/data.query("31 <= age <= 54").shape[0]*100
data_55_A = data.query('status == "A" & age >= 55').shape[0]/data.query("age >= 55").shape[0]*100
dic4 = {"младше 30": [data_30_A, 100-data_30_A],
        "от 31 до 54": [data_31_54_A, 100-data_31_54_A],
        "старше 55": [data_55_A, 100-data_55_A]
        }
print(dic4)