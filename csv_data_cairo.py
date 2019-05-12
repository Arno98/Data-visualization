import csv
import matplotlib.pyplot as plt
from datetime import datetime

datafile = 'Temperature_of_Cairo_Two.csv'
with open(datafile) as d_f:
	d_f_read = csv.reader(d_f)
	next_row = next(d_f_read)
	
	hights, averages, dates = [], [], []
	for row in d_f_read:
		try:
			int_hights = int(row[1])
			int_averages = int(row[2])
			current_dates = datetime.strptime(row[0], "%d-%m")
		except ValueError:
			None
		else:
			hights.append(int_hights)
			averages.append(int_averages)
			dates.append(current_dates)
		
fig = plt.figure(dpi=120, figsize=(8, 6))
plt.plot(dates, hights, c='red', linewidth=1)
plt.plot(dates, averages, c='green', linewidth=1)
plt.fill_between(dates, hights, averages, facecolor='green', alpha=0.2)
fig.autofmt_xdate()
plt.show()
