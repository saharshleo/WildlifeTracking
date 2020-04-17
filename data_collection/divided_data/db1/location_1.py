# import csv
import pandas as pd
import reverse_geocoder as rg 

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
			print(count)
			count += 1
			city_list.append(city)
			country_list.append(country)

		else:
			print(count)
			count += 1
			city_list.append(None)
			country_list.append(None)
	
	return city_list, country_list


# #################################################################################################
df = pd.read_csv('Data_Collected_1-1.csv')
print("read file")
print("**********************************")

# Converting to NaN
df['location_lat'] = pd.to_numeric(df['location_lat'], errors='ignore')
df['location_long'] = pd.to_numeric(df['location_long'], errors='ignore')
# print(df)

computed_city, computed_country = compute_address(df)
df['city'] = computed_city
df['country_code'] = computed_country

# Dropping Nan
df.dropna(subset = ['location_lat', 'location_long'], inplace = True)
	
df.to_csv('new_file_1-1.csv')
