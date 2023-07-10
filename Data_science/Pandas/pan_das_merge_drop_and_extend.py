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

df['Language'] = 'English'  # Добавляем новую колонку в Data Frame,
print(df)
print('')

# df['Reputation'] = [100, 300, 300, 500, 700]  # Так же можно менять значения в уже существующих колонках
# print(df)
# print('')

df['Active'] = np.array([True, False, False, True, True])  # Так же можно передавать в виде массива Numpy
print(df)
print('')
print('')



total_comments = {
    'Total Comments': [70, 30, 45, 55, 80]
}

df2 = pd.DataFrame(total_comments)
print(df2)
print('')

# By default concat work on the Axis=0!!!
print(pd.concat([df, df2]))  # Выполняем конкатенацию то есть соединяем два Data Frame
print('')

df = pd.concat([df, df2], axis=1)
print(df)
print('')

# Original df doesn't change!
print(df.drop(['Language'], axis=1))  # Удаляем колонку из Data Frame по default axis=0!!!!
print('')

print(df)
print('')

# Original df is changed inplace
df.drop(['Language'], axis=1, inplace=True)  # Удаляет колонку в оригинале Data Frame
print(df)
print('')

df.drop([2, 3], inplace=True)  # Удаляем строки из оригинала Data Frame
print(df)
print('')






