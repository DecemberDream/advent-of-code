import numpy as np
from scipy import signal


data = np.genfromtxt("../../input/day_11_data.txt", delimiter=1, dtype=np.uint8)

step = 1
flashing = np.zeros_like(data)

while True:
    data += 1
    flashed_in_step = np.zeros_like(data)    
    
    while data[data > 9].any():
        flashing = np.where(data > 9, True, False)
        adjacent = signal.convolve2d(flashing, np.ones((3,3)), mode="same").astype(np.uint8)
        data += adjacent
        data[np.where(flashing)] = 0
        flashed_in_step += flashing

    data[np.where(flashed_in_step)] = 0

    if np.sum(flashed_in_step) == len(data.flatten()):
        break
    
    step += 1
    
print(step)