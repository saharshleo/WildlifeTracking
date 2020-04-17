import pandas as pd

df = pd.read_csv("animal_data/animal_data_7.csv")

print("read")
df.drop(['Unnamed: 0.1.1', 'Unnamed: 0.1'], axis = 1, inplace = True)
# print(df)
df.dropna(subset = ['location_lat', 'location_long'], inplace = True)


dict_of_companies = {k: v for k, v in df.groupby('individual_id')}
# print(dict_of_companies)

count = 1

for key, temp_df in dict_of_companies.items():
	temp_df.to_csv("individual_data/animal_7/" + str(temp_df.iloc[0]['common_name']) + '_' + str(count) + ".csv")
	count += 1
	# print(temp_df.iloc[0]['common_name'])
