import numpy as np
from scipy.ndimage import measurements

data = open("../../input/day_9_data.txt")
lines = data.readlines()

data_array = []

for line in lines:
    data_array.append(np.array([int(c) for c in line.rstrip("\n")], dtype=np.uint8))

data.close()

height_map = np.array(data_array)

basins = np.where(height_map == 9, False, True)

labels, num_of_labels = measurements.label(basins)
areas = measurements.sum(basins, labels, index=np.arange(np.max(labels) + 1))
areas = np.sort(areas)

print(np.prod(areas[-3:]))
