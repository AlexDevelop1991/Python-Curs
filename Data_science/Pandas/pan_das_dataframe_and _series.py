import pandas as pd
import numpy as np

            ### DATA FRAME ###


forum_users = {
    'User ID': np.array([1, 2, 3, 4, 5]),
    'Username': ['bogdan_s', 'jane_smith', 'alex123', 'bob56', 'mark_wilson'],
    'Age': [18, 35, 25, 38, None],
    'Joined Date': pd.to_datetime(['2032-01-01', '2032-02-15', '2032-04-25', '2032-06-21', '2032-09-15']),
    'Total Post': [150, 230, 80, 420, 310],
    'Reputation': [500, 720, 200, 940, 500]
}

df = pd.DataFrame(forum_users)
print(df)
print('')
print(df.shape)  # Длина то есть сколько строк и столбцов(колонок)
print('')
print(type(df))  # Тип
print('')
print(df.columns)  # Названия столбцов
print('')
print(df.columns.tolist())  # Названия столбцов в виде списка
print('')
print(df.index.tolist())  # Получаем список меток
print('')
print(df.dtypes)  # Получаем типы данных для каждой из столбцов(колонок)
print('')
print(df.values)  # Выводит в виде массива данные
print('')
print(df.values[1, 1])  # Получаем данные из массива по индексу
print('')
print(df.head(3))  # Получаем данные из Data Frame первые 3 ряда по default это первые 5 рядов
print('')
print(df.tail(2))  # Получаем данные из Data Frame последнии 2 ряда по default это последнии 5 рядов
print('')
print(df.describe().round(2))  # Получаем статистические данные о определенном Data Frame , round округляет значение
print('')
print(df.select_dtypes(include='object'))  # Возвращает Data Frame c определённым типом данных
print('')
print(df.select_dtypes(include='int'))
print('')
print(df.isna())  # Позваляет определить те значения которые отсутсвуют
print('')
print(df.isna().sum())
print('')


                    ### SERIES ###

user_name_series = df['Username']
print(user_name_series)
print('')
print(type(user_name_series))
print('')
print(user_name_series.values)
print('')
print(user_name_series.index)
print('')
print(user_name_series.value_counts())  # Value_counts считает одиннаковое количество элементов в определённой колонки в исходном Data Frame
print('')
print(df['Reputation'].value_counts())
print('')
print(df['Reputation'].value_counts(ascending=True))
print('')
print(df['Reputation'].unique())  # Получем только уникальные значения в определенной колонки(одномерный массив)
print('')
print(user_name_series.sort_values())  # Сортировка значений в определённой колонки по default по возрастанию
print('')
print((user_name_series.sort_values(ascending=False)))

