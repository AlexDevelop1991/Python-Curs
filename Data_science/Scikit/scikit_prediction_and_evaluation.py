import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import seaborn as sns
import matplotlib.pyplot as plt


                    ### Loading Data ###

df = pd.read_csv('vehicles.csv')
print(df.head(8))
print('')

                    ### Cleaning ###

df.isnull().sum()  # Показывает где отсутсвуют значения
df['Income'].fillna(0.0, inplace=True)  # Заменяем пустые или отсутсвуешие значения в Data Frame
print(df)
print('')

                    ### Encoding ###

print(df['Gender'].unique())
print('')
# OPTION 1 Кодирования в ручную
# df.replace({
#     'Gender': {
#         'male': 0,
#         'female': 1
#     }
# }, inplace=True)
# print(df.head(5))
# OPTION 2  Автоматическое кодирование
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
print(df.head())
print('')

                    ### Model ### (Работают только с цифровыми колонки int, float, Datatime)

X = df.drop(columns='Favorite Transport')  # Удаляем колонку Favorite Transport
print(X.head(5))
print('')
y = df['Favorite Transport']
print(y.head(5))
print('')
model = DecisionTreeClassifier()
model.fit(X, y)

                    ### Prediction ###

test_df = pd.DataFrame({  # Мы просто задаём тестовые данные
    'Age': [12],
    'Gender': [0],
    'Income': [0.0]
})
print(test_df)
print('')
print(model.predict(test_df))  # Модель предсказала что любимый транспорт девочеки 12 лет это велосипед

                    ### Exporting to the DOT file

tree.export_graphviz(model, out_file='decision_tree_model.dot', feature_names=['Age', 'Gender', 'Income'], filled=True, class_names=sorted(y.unique()))

                    ### Evaluation ###

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X.shape)
print('')
print(X_train.shape)  # 80% переданно для тренировки
print('')
print(X_test.shape)  # 20% для тестирования
print('')
model = DecisionTreeClassifier()
model.fit(X_train, y_train)  # Передаем части для обучении модели
predictions = model.predict(X_test)
print(predictions)
print('')
model_accuracy_score = accuracy_score(y_test, predictions)
print(model_accuracy_score)

                    ### Charts ###

sns.countplot(x=df['Gender'], hue=df['Favorite Transport'])
plt.show()

sns.histplot(x=df['Income'], hue=df['Favorite Transport'])
plt.show()



