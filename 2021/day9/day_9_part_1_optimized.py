import numpy as np


data = open("../../input/day_9_data.txt")
lines = data.readlines()

data_array = []

for line in lines:
    data_array.append(np.array([int(c) for c in line.rstrip("\n")], dtype=np.uint8))

data.close()

height_map = np.array(data_array)
height_map = np.pad(height_map, pad_width=1, mode="constant", constant_values=9)

rows, cols = height_map.shape
result = 0

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if height_map[row, col] < height_map[row - 1, col] and height_map[row, col] < height_map[row + 1, col] and height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row, col + 1]:
            result += height_map[row, col] + 1

print(result)