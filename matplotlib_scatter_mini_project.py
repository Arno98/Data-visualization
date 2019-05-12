import matplotlib.pyplot as plt

numbers = list(range(1, 101))
squares = [x**2 for x in numbers]

plt.scatter(numbers, squares, c=squares, cmap=plt.cm.Blues, edgecolor='none', s = 10)
plt.scatter(numbers[0], squares[0], c='green', s=30)
plt.scatter(numbers[-1], squares[-1], c='red', s=30)
plt.title("Squares of numbers(from 1 to 100)", fontsize=20)
plt.xlabel("Numbers", fontsize=12)
plt.ylabel("Squares", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
