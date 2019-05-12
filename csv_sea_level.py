import csv
import matplotlib.pyplot as plt
from datetime import datetime

csv_file = 'epa-sea-level_csv.csv'
with open(csv_file) as sea_level_file:
	csv_file_reader = csv.reader(sea_level_file)
	next_row = next(csv_file_reader)
	
	dates, lowerr, upperr = [], [], []
	for row in csv_file_reader:
		dates.append(row[0])
		lowerr.append(int(float(row[2])))
		upperr.append(int(float(row[3])))
			
figure = plt.figure(dpi=100, figsize=(8, 4))
plt.plot(dates, lowerr, c='blue', linewidth=1)
plt.plot(dates, upperr, c='red', linewidth=1)
plt.fill_between(dates, lowerr, upperr, facecolor='green', alpha=0.2)

plt.title("Sea level from 1880 to 2014", fontsize=20)
plt.xlabel("", fontsize=15)
figure.autofmt_xdate()
plt.ylabel("Sea level(mm)", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=5)

plt.show()
		
