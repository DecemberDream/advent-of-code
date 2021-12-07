import numpy as np


data = np.array([int(c) for c in open("../../input/day_7_data.txt").read().split(",")], dtype=np.int32)
fuel = np.abs(data - np.median(data))
print(np.sum(fuel))