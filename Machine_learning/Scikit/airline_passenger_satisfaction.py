import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

                    ### Loading Data ###

df = pd.read_csv('airline_passenger_satisfaction.csv')
pd.set_option('display.max_columns', None)  # Показывает все колонки
print(df.head())
print('')
df.drop(columns='ID', inplace=True)  # Удаляет колонку ID из Data Frame
print(df.head(3))
print('')

print(df.shape)
print('')

print(df.describe().round(2))
print('')

print(df.dtypes)
print('')

                    ### Data Cleaning ###
print(df.info())
print('')

print(df.isnull().sum())  # Есть 3 варианта либо удаляем колонку, либо заполняем нулями, либо средним значением
print('')

print(df['Arrival Delay'].mean())  # Находим среднее значения
print('')

df['Arrival Delay'].fillna(df['Arrival Delay'].mean(), inplace=True)  # Заполняем пустые значения
print(df.isnull().sum())
print('')

                    ### Charts ###

plt.pie(df['Satisfaction'].value_counts(), labels=['Neutral of Dissatisfied', 'Satisfied'], autopct='%1.1f%%')
#plt.show()

# Не работает
# cols = ['Gender', 'Customer Type', 'Type of Travel', 'Class', 'Satisfaction']
# plt.figure(figsize=(15, 15))  # Размер диаграммы
# for i, col in enumerate(cols):
#     plt.subplots(3, 2, i + 1)
#     sns.countplot(x=col, data=df)
# plt.show()

df.hist(bins=20, figsize=(20, 20), color='green')
#plt.show()

                    ### Column Data Encoding

object = df.select_dtypes('object').columns
print(object)
print('')

print(df['Gender'].unique())
print('')
print(df['Customer Type'].unique())
print('')
print(df['Type of Travel'].unique())
print('')
print(df['Class'].unique())
print('')

# OPTION 1 Автоматическая кодировка
label_encoder = LabelEncoder()
columns = df.select_dtypes(include='object').drop(columns='Satisfaction').columns
print(columns)
for column in columns:
    df[column] = label_encoder.fit_transform(df[column])
print(df.head(3))

#  OPTION 2 Кодировка в ручную
# df.replace({
#     'Gender': {
#         'Male': 1,
#         'Female': 2
#     },
#     'Customer Type': {
#         'First-time': 1,
#         'Returning': 2
#     },
#     'Type of Travel': {
#         'Business': 1,
#         'Personal': 2
#     },
#     'Class': {
#         'Business': 1,
#         'Economy': 2,
#         'Economy Plus': 3
#     }
# }, inplace=True)
# print(df.head(3))

                    ### Additional Charts ###

plt.figure(figsize=(16, 8))
sns.heatmap(df.drop(columns='Satisfaction').corr(), annot=True, fmt='.2f', cmap='Greens')
plt.show()

sns.catplot(data=df, x='Age', height=4, aspect=6, kind='count', hue='Satisfaction', order=range(7, 73))
plt.show()

sns.catplot(data=df, x='On-board Service', height=4, aspect=4, kind='count', hue='Satisfaction')
plt.show()