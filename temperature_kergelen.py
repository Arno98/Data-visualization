import csv
import matplotlib.pyplot as plt

t_file = 'temperature_kergelen.csv'
with open(t_file) as ker_file:
	ker_read = csv.reader(ker_file)
	next_row_read = next(ker_read)
	
	monthes, abs_max, mid_max, mid, mid_min, abs_min = [], [], [], [], [], []	
	for row in ker_read:
		monthes.append(int(float(row[0])))
		abs_max.append(int(float(row[1])))
		mid_max.append(int(float(row[2])))
		mid.append(int(float(row[3])))
		mid_min.append(int(float(row[4])))
		abs_min.append(int(float(row[5])))
		
fig = plt.figure(dpi=120, figsize=(8, 4))
plt.plot(monthes, abs_max, c='red', linewidth=1)
plt.plot(monthes, mid_max, c='yellow', linewidth=1)
plt.plot(monthes, mid, c='green', linewidth=1)
plt.plot(monthes, mid_min, c='cyan', linewidth=1)
plt.plot(monthes, abs_min, c='blue', linewidth=1)
plt.fill_between(monthes, abs_max, abs_min, facecolor='green', alpha=0.1)

plt.title("Temperature island Kerguelen", fontsize=20)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(C)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
