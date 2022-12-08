import numpy as np


def all_less(a):
    for x in a[1:]:
        if x >= a[0]:
            return False

    return True
    # return all(x < a[0] for x in a[1:]) # slower


def is_visible(r, c, data):
    return int(all_less(data[r,c:])
        or all_less(data[r:,c])
        or all_less(data[r,:c+1][::-1])
        or all_less(data[:r+1,c][::-1])
    )


filename = "./../../2022_input/day_8_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = np.array([[int(x) for x in list(line.strip())] for line in file.readlines()])

counter = 0

for row in range(1, data.shape[0]-1):
    for col in range(1, data.shape[1]-1):
        counter += is_visible(row, col, data)

print(counter + 2 * data.shape[0] + 2 * data.shape[0] - 4)