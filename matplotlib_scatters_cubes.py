import matplotlib.pyplot as plt

numbers = list(range(101))
cubes_of_numbers = [c**3 for c in numbers]

plt.scatter(numbers, cubes_of_numbers, c=cubes_of_numbers, cmap=plt.cm.Blues, edgecolor='none', s=30)

plt.title("Cubes of 5000 number", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Cubes of Value", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.axis([0, 150, 0, 1100000])

plt.show()
