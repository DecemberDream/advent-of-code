import numpy as np


def count_trees(a):
    counter = 0

    for x in a[1:]:
        if x < a[0]:
            counter += 1
        elif x >= a[0]:
            counter += 1
            break

    return counter


def is_visible(r, c, data):
    return count_trees(data[r,c:]) * count_trees(data[r:,c]) * count_trees(data[r,:c+1][::-1]) * count_trees(data[:r+1,c][::-1])


filename = "./../../2022_input/day_8_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = np.array([[int(x) for x in list(line.strip())] for line in file.readlines()])

score = -1

for row in range(1, data.shape[0]-1):
    for col in range(1, data.shape[1]-1):
        s = is_visible(row, col, data)
        if s > score:
            score = s
        
print(score)