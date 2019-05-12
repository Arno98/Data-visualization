import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(numbers, squares, linewidth=5)

plt.title("Squares first's 5 number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
