import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 20]
#
# plt.show()

# plt.scatter(x_values, y_values, s=100, color='green')
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.show()

animals = ['cat', 'dog', 'rabbit', 'elephant', 'tiger', 'lion', 'horse', 'monkey', 'zebra', 'giraffe']
animal_weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# plt.bar(animals, animal_weights)
# plt.title("Animal Weights", fontsize=24)
# plt.xlabel("Animals", fontsize=14)
# plt.ylabel("Weights", fontsize=14)
# plt.show()

import numpy as np

# X_normal = np.random.normal(0, 1, 2000)
# plt.hist(X_normal, color='forestgreen')
# plt.xlabel('X')
# plt.ylabel('Frequency')
# plt.title('Randomly generating 1000 obs from Normal Distribution mu=0, sigma=1')
# plt.show()

from scipy.stats import norm
x_values = np.arange(-4, 4, 0.01)
y_values = norm.pdf(x_values)
counts, bins, ignored = plt.hist(x_values, 30, density=True, color='purple', label='Sampling Distribution')
plt.plot(x_values, norm.pdf(x_values), linewidth=2.5, color='yellow', label='Population Distribution')
# plt.plot(bins, y_values, linewidth=2, color='r')
plt.title('Randomly generating 1000 obs from Normal Distribution mu=0, sigma=1')
plt.ylabel('Probability Density')
plt.legend()
plt.show()