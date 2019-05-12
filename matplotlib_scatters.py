import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
squares_of_numbers = [1, 4, 9, 16, 25]
plt.scatter(numbers, squares_of_numbers, s=20)

plt.title("Square Scatters", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.show()
