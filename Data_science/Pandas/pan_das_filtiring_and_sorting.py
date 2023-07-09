import pandas as pd
import numpy as np


forum_users = {
    'User ID': np.array([1, 2, 3, 4, 5]),
    'Username': ['bogdan_s', 'jane_smith', 'alex123', 'bob56', 'mark_wilson'],
    'Age': [18, 35, 25, 38, None],
    'Joined Date': pd.to_datetime(['2032-01-01', '2032-02-15', '2032-04-25', '2032-06-21', '2032-09-15']),
    'Total Posts': [150, 230, 80, 420, 310],
    'Reputation': [500, 720, 200, 940, 500]
}

df = pd.DataFrame(forum_users)

            ### Filtering ###

print(df[['Username', 'Age']])
print('')

print(df.loc[3])  # Поиск по метке определённого ряда в Data Frame получаем Serie
print('')

print(df.loc[2:3])  # Поиск по метке определённого ряда в Data Frame получаем Data Frame
print('')

print(df.loc[2:3, ['Username', 'Joined Date', 'Reputation']])
print('')

print(df.iloc[3])
print('')

print(df.iloc[2:4])  # Поиск по идексу последний не включительно в данном случаии 4
print('')

print(df.iloc[2:4, 1:4])  # Поиск по идексу указываем диапозон 2:4 это для рядов а 1:4 это для столбцов
print('')

print(df.iloc[:, 1:4])
print('')

print(df[df['Age'] >= 25])  # Фильтрация в Data Frame
print('')

print(df[df['Total Posts'] >= 300])
print('')

print(df[df['Reputation'] == 500])
print('')

print(df[(df['Total Posts'] >= 300) & (df['Age'] >= 25)])  # &-это и
print('')

print(df[(df['Total Posts'] >= 400) | (df['Age'] <= 25)])  # |-это или
print('')

print(df['Reputation'].isin([200, 500]))
print('')

print(df[df['Reputation'].isin([200, 500])])  # Проверяет если есть определённое значение в определённом списке значений
print('')

print(df[df['Total Posts'].isin(range(200, 350))])
print('')

data_range1 = pd.date_range(start='2032-03-01', end='2032-08-01')
print(data_range1)
print('')

print(df[df['Joined Date'].isin(data_range1)])
print('')


            ### Sorting ###

print(df.sort_values(by='Age'))
print('')

print(df.sort_values(by='Joined Date', ascending=False))
print('')

print(df.sort_values(by='Total Posts'))
print('')

print(df[['User ID', 'Total Posts', 'Reputation']])
print('')

# Sort by values in the row with index 2
print(df[['User ID', 'Total Posts', 'Reputation']].sort_values(by=2, axis=1, ascending=False))
print('')







