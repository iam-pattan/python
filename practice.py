import numpy as np
import pandas as pd

df_col = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
df_row = np.random.randint(low=0, high=100, size=(12))
df_row = df_row.reshape((3,4))
print(df_col)
print(df_row, type(df_row))
df = pd.DataFrame(data=df_row, columns=df_col)
janet_col = df['Tahani'] + df['Jason']
df['Janet'] = janet_col

print(df)