import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(20000)
	rw.walk()
	
	plt.figure(figsize=(12, 6))
	
	points_numbers = list(range(rw.number_points))
	
	plt.scatter(rw.x_value, rw.y_value, c=points_numbers, cmap=plt.cm.Blues, edgecolor='none', s=8)
	plt.scatter(0, 0, c='green', edgecolor='none', s=50)
	plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolor='none', s=50)
	
	plt.title("Random Walk", fontsize=25)
	plt.xlabel("X Value", fontsize=15)
	plt.ylabel("Y Value", fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize=15)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()
	
	next_random_walk = input("Do you want generate next random walk?(enter 'y' or 'n') ")
	if next_random_walk == 'y':
		continue
	elif next_random_walk == 'n':
		break
