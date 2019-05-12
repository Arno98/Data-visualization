import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
cubes_of_numbers = [c**3 for c in numbers]

plt.plot(numbers, cubes_of_numbers, linewidth=3)

plt.title("Cubes of first 5 number", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Cubes of Value", fontsize=15)
plt.tick_params(axis='both', labelsize=15)

plt.show()
