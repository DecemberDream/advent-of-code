import numpy as np


data = open("../../input/day_9_data.txt")
lines = data.readlines()

data_array = []

for line in lines:
    data_array.append(np.array([int(c) for c in line.rstrip("\n")], dtype=np.uint8))

data.close()

height_map = np.array(data_array)

rows, cols = height_map.shape
result = 0

for row in range(rows):
    for col in range(cols):
        # checking corners
        if row == 0 and col == 0:
            if height_map[row, col] < height_map[row, col + 1] and height_map[row, col] < height_map[row + 1, col]:
                result += height_map[row, col] + 1
            continue
        if row == 0 and col == cols - 1:
            if height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row + 1, col]:
                result += height_map[row, col] + 1
            continue
        if row == rows - 1 and col == 0:
            if height_map[row, col] < height_map[row, col + 1] and height_map[row, col] < height_map[row - 1, col]:
                result += height_map[row, col] + 1
            continue
        if row == rows - 1 and col == cols - 1:
            if height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row - 1, col]:
                result += height_map[row, col] + 1
            continue
        
        # checking edges
        if row == 0:
            if height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row, col + 1] and height_map[row, col] < height_map[row + 1, col]:
                result += height_map[row, col] + 1
        if row == rows - 1:
            if height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row, col + 1] and height_map[row, col] < height_map[row - 1, col]:
                result += height_map[row, col] + 1
        if col == 0:
            if height_map[row, col] < height_map[row - 1, col] and height_map[row, col] < height_map[row + 1, col] and height_map[row, col] < height_map[row, col + 1]:
                result += height_map[row, col] + 1
        if col == cols - 1:
            if height_map[row, col] < height_map[row - 1, col] and height_map[row, col] < height_map[row + 1, col] and height_map[row, col] < height_map[row, col - 1]:
                result += height_map[row, col] + 1

        # every other point
        if row > 0 and row < rows - 1 and col > 0 and col < cols - 1:
            if height_map[row, col] < height_map[row - 1, col] and height_map[row, col] < height_map[row + 1, col] and height_map[row, col] < height_map[row, col - 1] and height_map[row, col] < height_map[row, col + 1]:
                result += height_map[row, col] + 1

print(result)