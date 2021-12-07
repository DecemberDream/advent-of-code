import numpy as np


data = np.array([int(c) for c in open("../../input/day_7_data.txt").read().split(",")], dtype=np.int32)
fuel = np.abs(data - int(np.mean(data))) * (np.abs(data - int(np.mean(data))) + 1) // 2
print(np.sum(fuel))