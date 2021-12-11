import numpy as np
from scipy import signal


data = np.genfromtxt("../../input/day_11_data.txt", delimiter=1, dtype=np.uint8)

num_flashes = 0
flashing = np.zeros_like(data)

for step in range(1, 101):
    data += 1
    flashed_in_step = np.zeros_like(data)   
    
    while data[data > 9].any():
        flashing = np.where(data > 9, True, False)
        adjacent = signal.convolve2d(flashing, np.ones((3,3)), mode="same").astype(np.uint8)
        data += adjacent
        data[np.where(flashing)] = 0
        flashed_in_step += flashing

    num_flashes += np.sum(flashed_in_step)
    data[np.where(flashed_in_step)] = 0
    
print(num_flashes)