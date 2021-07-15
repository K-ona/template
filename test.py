import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
df.columns = ['h', 'w', 'l']

print(df)
print(df['h'])
print(df.loc())
print(df.iloc[[0]])