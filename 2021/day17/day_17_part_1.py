import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def step(x, y, x_vel, y_vel):
    x += x_vel
    y += y_vel
    
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
        
    y_vel -= 1
    
    return x, y, x_vel, y_vel


def perform_steps(x_vel, y_vel, x_start=0, y_start=0, steps=20):
    x_coords = [x_start]
    y_coords = [y_start]
    
    for _ in range(steps):
        x_pos, y_pos, x_vel, y_vel = step(x_coords[-1], y_coords[-1], x_vel, y_vel)
        x_coords.append(x_pos)
        y_coords.append(y_pos)
        
        if x_range[0] <= x_pos <= x_range[1] and y_range[0] <= y_pos <= y_range[1]:
            print("in target area! Vx={0}, Vy={1}".format(x_vel, y_vel))
            break
    
    return np.array(x_coords), np.array(y_coords)


data = open("../../input/day_17_data.txt").read().split(": ")[1:][0].split(", ")
x_range = data[0].split("=")[1].split("..")
y_range = data[1].split("=")[1].split("..")

x_range = [int(x) for x in x_range]
y_range = [int(y) for y in y_range]

x_start = 0
y_start = 0

# found x_vel manually by plotting the points
# after checking many y_vel's (which is really the only value that matters)
# we set the new y_max if it is in the target range and higher than the current y_max
y_max = -np.inf

for y_vel in range(50, 100):
    x, y = perform_steps(17, y_vel, steps=200)

    if np.any((y >= y_range[0]) & (y <= y_range[1])) and np.max(y) > y_max:
        y_max = np.max(y)
    
fig, ax = plt.subplots()
ax.add_patch(Rectangle((x_range[0], y_range[0]), x_range[1]-x_range[0], y_range[1]-y_range[0]))
ax.plot(x, y, "x")
plt.show()

print("max y:", y_max)
