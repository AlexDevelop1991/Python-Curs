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
print('')

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
# plt.show()

sns.catplot(data=df, x='Age', height=4, aspect=6, kind='count', hue='Satisfaction', order=range(7, 73))
# plt.show()

sns.catplot(data=df, x='On-board Service', height=4, aspect=4, kind='count', hue='Satisfaction')
# plt.show()

                    ### Filtering Data ### (Полезна на этапе предварительного анализа)

print(df[['Gender', 'Age', 'Type of Travel']].head())
print('')
print(df.loc[2:5, ['Gender', 'Age', 'Flight Distance']])  # loc работает только с метками строк и колонок(столбцов)
print('')
print(df.loc[df['Age'] > 50, ['Gender', 'Age', 'Flight Distance']].head())
print('')
print(df.loc[df['Gender'] == 1, ['Gender', 'Age', 'Flight Distance']].head())
print('')
print(df.iloc[10:15, 1:7].head())  # iloc работает с индексами строк и колонок(столбцов)
print('')
print(df.columns)
print('')
print(df.index)
print('')

                    ### Models ###

# X = df.drop(columns='Satisfaction')
# y = df['Satisfaction']

### Desicion Tree
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# model = DecisionTreeClassifier()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# print(X.shape)
# print('')
# print(X_train.shape)
# print('')
# print(X_test.shape)
# print('')
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)
# print('')
# model_score = accuracy_score(y_test, predictions)
# print(model_score)
# print('')

### Random Forest

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# model = RandomForestClassifier()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)
# print('')
# model_score = accuracy_score(y_test, predictions)
# print(model_score)
# print('')

### KNeighborsClassifier (почему то выдаёт ошибку)

# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# model = KNeighborsClassifier(n_neighbors=10)  # n_neighbors это указываем количество соседей
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)
# print('')
# model_score = accuracy_score(y_test, predictions)
# print(model_score)
# print('')

### Logistic Regression

# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# model = LogisticRegression(max_iter=10000)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)
# print('')
# model_score = accuracy_score(y_test, predictions)
# print(model_score)
# print('')

                    ### Predictions without Voting columns

X = df[['Gender', 'Age', 'Customer Type', 'Type of Travel', 'Class',
        'Flight Distance', 'Departure Delay', 'Arrival Delay']]
print(X.head())
print('')
y = df['Satisfaction']

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

model = RandomForestClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
print('')
model_score = accuracy_score(y_test, predictions)
print(model_score)
print('')

# Тестирование модели на основании вручную созданных данных
print(X.iloc[:0].to_dict())
print('')
test_inputs = {
    'Gender': [1, 0],
    'Age': [35, 25],
    'Customer Type': [0, 1],
    'Type of Travel': [0, 0],
    'Class': [1, 1],
    'Flight Distance': [1200, 600],
    'Departure Delay': [0, 0],
    'Arrival Delay': [0, 0]
}
test_df = pd.DataFrame(test_inputs)
print(test_df)
print('')
print(model.predict(test_df))
print('')

                    ### Saving Prediction Model ###

import joblib
joblib.dump(model, 'airline_passenger_satisfaction.joblib')
test_inputs = {
    'Gender': [1, 0],
    'Age': [35, 25],
    'Customer Type': [0, 1],
    'Type of Travel': [0, 0],
    'Class': [1, 1],
    'Flight Distance': [1200, 600],
    'Departure Delay': [0, 0],
    'Arrival Delay': [0, 0]
}
test_df = pd.DataFrame(test_inputs)
print(test_df)
print('')
trained_model = joblib.load('airline_passenger_satisfaction.joblib')
print(trained_model.predict(test_df))
