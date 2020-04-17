import pandas as pd

df1 = pd.read_csv('new_file_dta1.csv')
df2 = pd.read_csv('new_file_dta2.csv')

frames = [df1, df2]

result = pd.concat(frames, ignore_index = True)
print(result)
print(result.columns)

result.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
print(result.columns)
print(result)