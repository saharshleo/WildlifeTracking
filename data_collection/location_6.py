# import csv
import pandas as pd
import reverse_geocoder as rg
import numpy as np 
import pprint as pp

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

def reverseGeocode(coordinates): 
	result = rg.search(coordinates) 
	return result

def compute_address(df):
	# Initializing 
	city_list, country_list, count = [], [], 0

	for (idx, row) in df.iterrows():

		# print(row.loc['location_lat'])
		# print(pd.isna(row.loc['location_lat']) or pd.isna(row.loc['location_long']))

		if not (pd.isna(row.loc['location_lat']) or pd.isna(row.loc['location_long'])):
			value = reverseGeocode((row.loc['location_lat'], row.loc['location_long']))
			city, country = value[0]['name'], value[0]['cc']
			# print(count)
			# count += 1
			city_list.append(city)
			country_list.append(country)

		else:
			# print(count)
			# count += 1
			city_list.append(None)
			country_list.append(None)
	
	return city_list, country_list


# #################################################################################################
read_data = read_csv('Data_Collected_6.csv')
print("read file")
df = pd.DataFrame(read_data)
list_df = np.array_split(df, 10)
# pp.pprint(list_df)

pp.pprint(len(list_df))
print("**********************************")

# final = []
done = 0
for df in list_df:
	# Converting to NaN
	df['location_lat'] = pd.to_numeric(df['location_lat'], errors='ignore')
	df['location_long'] = pd.to_numeric(df['location_long'], errors='ignore')
	# print(df)

	computed_city, computed_country = compute_address(df)
	df['city'] = computed_city
	df['country_code'] = computed_country

	# Dropping Nan
	df.dropna(subset = ['location_lat', 'location_long'], inplace = True)
	# print(df)
	# final.append(df)
	if done == 0:
		df.to_csv('new_file_6.csv', mode = 'a')
		done += 1
		continue
	df.to_csv('new_file_6.csv', mode = 'a', header = False)
	print(done)
	done += 1
