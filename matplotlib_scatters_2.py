import matplotlib.pyplot as plt

thousands_scatters = list(range(1, 1001))
squares_of_thousands_scatters = [s**2 for s in thousands_scatters]

plt.scatter(thousands_scatters, squares_of_thousands_scatters, c=squares_of_thousands_scatters, cmap=plt.cm.Blues, edgecolor='none', s=30)
plt.title("Squares 1000 Scatters", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.axis([0, 1100, 0, 1100000])

plt.show()
