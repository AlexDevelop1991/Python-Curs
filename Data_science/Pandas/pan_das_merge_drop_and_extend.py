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

df['Active'] = [True, False, False, True, True]
print(df)