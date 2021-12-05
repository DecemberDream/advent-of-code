import numpy as np


def covered_points(start, end, all_points):
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])
    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])
    
    if min_x == max_x:
        r = range(min_y, max_y + 1)
        for i in range(len(r)):
            all_points.append([min_x, r[i]])
    if min_y == max_y:
        r = range(min_x, max_x + 1)
        for i in range(len(r)):
            all_points.append([r[i], min_y])
    
    return all_points


data = open("../../input/day_5_data.txt")
lines = data.readlines()

x1_y1 = []
x2_y2 = []

for line in lines:
    split_line = line.split()
    x1_y1.append([int(c) for c in split_line[0].split(",")])
    x2_y2.append([int(c) for c in split_line[2].split(",")])

data.close()

x1_y1 = np.array(x1_y1)
x2_y2 = np.array(x2_y2)

mask = np.squeeze(np.array([x1_y1 == x2_y2]))

for i in range(len(x1_y1)):
    if mask[i, 0] or mask[i, 1]:
        mask[i, :] = True

x1_y1_filtered = x1_y1[mask[:,0]]
x2_y2_filtered = x2_y2[mask[:,1]]

all_points = []

for i in range(len(x1_y1_filtered)):
    all_points = covered_points(x1_y1_filtered[i, :], x2_y2_filtered[i, :], all_points)

all_points = np.array(all_points)

unq, count = np.unique(all_points, axis=0, return_counts=True)

print(len(unq[count > 1]))