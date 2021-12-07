import numpy as np


data = np.array([int(c) for c in open("../../input/day_7_data.txt").read().split(",")], dtype=np.int16)

fuel = np.zeros_like(data, dtype=np.int16)

lowest_sum = np.inf

for i in range(len(data)):
    fuel = np.abs(data - i)
    
    if np.sum(fuel) < lowest_sum:
        lowest_sum = np.sum(fuel)
    
print(lowest_sum)