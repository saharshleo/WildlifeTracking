import pandas as pd

df1 = pd.read_csv('Data_Collected_1.csv')
df2 = pd.read_csv('Data_Collected_2.csv')
df3 = pd.read_csv('Data_Collected_3.csv')
df4 = pd.read_csv('Data_Collected_4.csv')
df5 = pd.read_csv('Data_Collected_5.csv')
df6 = pd.read_csv('Data_Collected_6.csv')
df7 = pd.read_csv('Data_Collected_7.csv')

df1 = df1.head(5000)
df2 = df2.head(5000)
df3 = df3.head(5000)
df4 = df4.head(5000)
df5 = df5.head(5000)
df6 = df6.head(5000)
df7 = df7.head(5000)

frames = [df1, df2, df3, df4, df5, df6, df7]

result = pd.concat(frames, ignore_index = True)
print(result)
print(result.columns)

result.drop(['Unnamed: 0'], axis = 1, inplace = True)
print(result.columns)
print(result)

result.to_csv("all_files_head.csv")