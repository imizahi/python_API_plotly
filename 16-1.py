import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'

with open(filename_1) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, prcps_1 = [], []
	for row in reader:
		current_day = datetime.strptime(row[2], '%Y-%m-%d')
		prcp = float(row[3])
		dates.append(current_day)
		prcps_1.append(prcp)

with open(filename_2) as f_2:
	reader_2 = csv.reader(f_2)
	header_row_2 = next(reader_2)
	dates,prcps_2 = [], []
	for row in reader_2:
		current_day_2 = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			prcp_2 = float(row[3])
		except ValueError:
			print('s')
			#dates.remove(current_day_2)
			#prcps_1.append(0)
		else:
			dates.append(current_day_2)
			prcps_2.append(prcp_2)
prcps_1.append(0)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps_1, c='red', alpha=0.5)
ax.plot(dates, prcps_2, c='blue', alpha=0.5)
#plt.fill_between(dates, prcps_1, lows, facecolor='blue', alpha=0.1)

plt.title("PRCP", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('prcp s', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()