import csv
import matplotlib.pyplot as plt
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'data/world_fires_1_day.csv'
lons, lats, versions, mags = [], [], [], []

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	"""for index, column_header in enumerate(header_row):
		print(index,column_header)"""
		#0 lat 1lon 9 version
	for row in reader:
		lon = row[1]
		lat = row[0]
		version = row[11]
		mag = float(row[3])
		lats.append(lat)
		lons.append(lon)
		versions.append(version)
		mags.append(mag)
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat' : lats,
	'text' : versions,
	'marker' : {
		'size' : [5*mag for mag in mags],
		'color' : mags,
		'colorscale' : 'Viridis',
		'reversescale' : True,
		'colorbar' : {'title': 'Magnitude'}

	},
}]
my_layout = Layout(title='fire')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fire.html')


