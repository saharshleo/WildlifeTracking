import pandas as pd
import reverse_geocoder as rg
from google.colab import files
import io

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

def reverseGeocode(coordinates): 
	result = rg.search(coordinates) 
	return result

def compute_address(df):
	# Initializing 
	city_list, country_list, admin1_list, admin2_list, count = [], [], [], [], 0

	for (idx, row) in df.iterrows():

		# print(row.loc['location_lat'])
		# print(pd.isna(row.loc['location_lat']) or pd.isna(row.loc['location_long']))

		if not (pd.isna(row.loc['location_lat']) or pd.isna(row.loc['location_long'])):
			value = reverseGeocode((row.loc['location_lat'], row.loc['location_long']))
			city, country, admin1, admin2 = value[0]['name'], value[0]['cc'], value[0]['admin1'], value[0]['admin2']
			print(count)
			count += 1
			city_list.append(city)
			country_list.append(country)
	 		if count == 10000:
				df['city'] = city_list
				df['country_code'] = country_list

				df.dropna(subset = ['location_lat', 'location_long'], inplace = True)

				df.to_csv('new_file_5.csv')
				files.download('new_file_5.csv')
				city_list = []
				country_list = []
		else:
			print(count)
			count += 1
			city_list.append(None)
			country_list.append(None)
	 		if count == 10000:
				df['city'] = city_list
				df['country_code'] = country_list

				df.dropna(subset = ['location_lat', 'location_long'], inplace = True)

				df.to_csv('new_file_5.csv')
				files.download('new_file_5.csv')
				city_list = []
				country_list = []
	
	return city_list, country_list


uploaded = files.upload()
df = pd.read_csv(io.BytesIO(uploaded['Data_Collected_5.csv']))

df['location_lat'] = pd.to_numeric(df['location_lat'], errors='ignore')
df['location_long'] = pd.to_numeric(df['location_long'], errors='ignore')

computed_city, computed_country = compute_address(df)
df['city'] = computed_city
df['country_code'] = computed_country

df.dropna(subset = ['location_lat', 'location_long'], inplace = True)

df.to_csv('new_file_5.csv')
files.download('new_file_5.csv')

