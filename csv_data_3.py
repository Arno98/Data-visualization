import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as file_weather:
	read_file = csv.reader(file_weather)
	next_row = next(read_file)
	
	hights, lows, dates = [], [], []
	for row in read_file:
		try:
			current_time = datetime.strptime(row[0], '%Y-%m-%d')
			int_value_1 = int(row[1])
			int_value_2 = int(row[3])
		except ValueError:
			print("This data " + "'" + str(current_time) + "'" + " was missed.")
		else:
			hights.append(int_value_1)
			lows.append(int_value_2)
			dates.append(current_time)

fig = plt.figure(dpi=120, figsize=(8, 4))		
plt.plot(dates, hights, c='red', linewidth=1)
plt.plot(dates, lows, c='blue', linewidth=1)
plt.fill_between(dates, hights, lows, facecolor='green', alpha=0.3)

plt.title("Daily hight and low temperature in Death Valley - (2014)", fontsize=20)
plt.xlabel("", fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temeperature(F)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
