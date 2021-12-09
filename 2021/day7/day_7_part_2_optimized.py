import numpy as np


data = np.array([int(c) for c in open("../../input/day_7_data.txt").read().split(",")], dtype=np.int32)

m = np.mean(data)
n = len(data)
k = len(data[data < m])

if m - int(m) > (2 * k - 1) / (2 * n):
    fuel = np.abs(data - np.ceil(np.mean(data))) * (np.abs(data - np.ceil(np.mean(data))) + 1) // 2
else:
    fuel = np.abs(data - np.floor(np.mean(data))) * (np.abs(data - np.floor(np.mean(data))) + 1) // 2
    
print(np.sum(fuel))