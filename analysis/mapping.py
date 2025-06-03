import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import json
import geopandas as gpd


#Path for GeoDataFrame
world = gpd.read_file("./ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

#Open and read file into data variable
path = "./ips-countries.json"
with open(path,"r") as file:
	data_dict = json.load(file)

df = pd.DataFrame()

for index, country in enumerate(data_dict):
	#Initialize dataframe columns
	df.loc[index,'Country'] = country
	df.loc[index, 'Occurences'] = 0
	for ip in data_dict[country]:
		#Populate number of occurences in Occurences column
		df.loc[index,'Occurences'] += 1


#Merge world: GeoDataFrame and df: DataFrame
merged = world.merge(df, how='left',left_on='SUBUNIT',right_on='Country')

#Plot data
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.plot(column='Occurences', linewidth=1, ax=ax, legend=True, cmap='coolwarm', missing_kwds={
    "color": "lightgrey",
    "label": "No data"
})
ax.set_title("Number of IP addresses by country", fontsize=15)
ax.axis('off')

plt.savefig("map.png", dpi=300)

plt.show()