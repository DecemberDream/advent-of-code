import numpy as np


data = open("../../input/day_3_data.txt")
lines = data.readlines()

data_array = []

for line in lines:
    data_array.append(np.array([int(c) for c in line.rstrip("\n")]))

data_array = np.array(data_array)
gamma_rate = np.zeros(len(data_array[0]), bool)
rows = len(data_array)

for i in range(len(data_array[0])):
    ones = np.sum(data_array[:, i])
    
    gamma_rate[i] = 1 if ones / rows > 0.5 else 0
    
epsilon_rate = np.invert(gamma_rate).astype(int)
gamma_rate = gamma_rate.astype(int)

gamma = gamma_rate.dot(1 << np.arange(gamma_rate.shape[-1] - 1, -1, -1))
epsilon = epsilon_rate.dot(1 << np.arange(epsilon_rate.shape[-1] - 1, -1, -1))

print(gamma * epsilon)
