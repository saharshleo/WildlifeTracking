import pandas as pd

df = pd.read_csv('animal_data_1.csv')
print("read file")
print("**********************************")

wiki_list = []
# df.replace(to_replace="Unknown", value="straw-coloured fruit bat", inplace=True)

for (idx, row) in df.iterrows():
	if row.loc['taxon_canonical_name'] == 'Anser albifrons':
		print('Anser albifrons')
		wiki_list.append('https://en.wikipedia.org/wiki/Greater_white-fronted_goose')

	elif row.loc['taxon_canonical_name'] == 'Cygnus columbianus':
		print('Cygnus columbianus')
		wiki_list.append('https://en.wikipedia.org/wiki/Tundra_swan')

	elif row.loc['taxon_canonical_name'] == 'Aythya fuligula':
		print('Aythya fuligula')
		wiki_list.append('https://en.wikipedia.org/wiki/Tufted_duck')

	elif row.loc['taxon_canonical_name'] == 'Anas platyrhynchos':
		print('Anas platyrhynchos')
		wiki_list.append('https://en.wikipedia.org/wiki/Mallard')

	elif row.loc['taxon_canonical_name'] == 'Canis lupus':
		print('Canis lupus')
		wiki_list.append('https://en.wikipedia.org/wiki/Wolf')

	elif row.loc['taxon_canonical_name'] == 'Felis catus':
		print('Felis catus')
		wiki_list.append('https://en.wikipedia.org/wiki/Cat')

	elif row.loc['taxon_canonical_name'] == 'Limosa limosa':
		print('Limosa limosa')
		wiki_list.append('https://en.wikipedia.org/wiki/Black-tailed_godwit')

	# elif row.loc['taxon_canonical_name'] == '':
	# 	print('')
	# 	wiki_list.append('')	

	else:
		print('Unknown')
		wiki_list.append('Unknown')

df['wiki_url'] = wiki_list
df.to_csv('animal_data_1.csv')