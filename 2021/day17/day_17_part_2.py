import numpy as np


def step(x, y, x_vel, y_vel):
    x += x_vel
    y += y_vel
    
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
        
    y_vel -= 1
    
    return x, y, x_vel, y_vel


def perform_steps(x_vel, y_vel, target, x_start=0, y_start=0, steps=20):
    x_coords = [x_start]
    y_coords = [y_start]
    
    while check_if_possible(x_coords[-1], y_coords[-1], x_vel, y_vel, target):
        x_pos, y_pos, x_vel, y_vel = step(x_coords[-1], y_coords[-1], x_vel, y_vel)
        x_coords.append(x_pos)
        y_coords.append(y_pos)
    
    return np.array(x_coords), np.array(y_coords)


def check_if_possible(x_start, y_start, x_vel, y_vel, target):
    x0, xn, y0, yn = target
    
    if (x_vel >= 0 and xn < x_start) or (x_vel <= 0 and x0 > x_start):
        return False
    elif (y_vel < 0 and y0 > y_start):
        return False
    else:
        return True


def in_target(x_vel, y_vel, target):
    x, y = perform_steps(x_vel, y_vel, target)
    x0, xn, y0, yn = target
    
    return np.any((y >= y0) & (y <= yn) & (x >= x0) & (x <= xn))


data = open("../../input/day_17_data.txt").read().split(": ")[1:][0].split(", ")
x_range = data[0].split("=")[1].split("..")
y_range = data[1].split("=")[1].split("..")

x_range = [int(x) for x in x_range]
y_range = [int(y) for y in y_range]

target = (x_range[0], x_range[1], y_range[0], y_range[1])

x_start = 0
y_start = 0

viable = []

for x_vel in range(x_range[1] + 1):
    for y_vel in range(y_range[0]-1, 100):
        if in_target(x_vel, y_vel, target):
            viable.append((x_vel, y_vel))

print("number of viable initial velocities:", len(viable))