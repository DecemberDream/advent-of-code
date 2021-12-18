import math


def sgn(x):
    return (x > 0) - (x < 0)


def simulate(vx, vy, target, steps=200):
    x = y = 0
    max_y = 0
    x0, xn, y0, yn = target
    
    if (vx >= 0 and xn < x) or (vx <= 0 and x0 > x) or (vy < 0 and y0 > y):
        return -1
    
    for step in range(steps):
        x += vx
        y += vy
        max_y = max(y, max_y)
        
        if x0 <= x <= xn and y0 <= y <= yn:
            return max_y
        
        vx -= sgn(vx)
        vy -= 1
        
    return -1


data = open("../../input/day_17_data.txt").read().split(": ")[1:][0].split(", ")
x_range = data[0].split("=")[1].split("..")
y_range = data[1].split("=")[1].split("..")

x_range = [int(x) for x in x_range]
y_range = [int(y) for y in y_range]

target = (min(x_range), max(x_range), min(y_range), max(y_range))

min_x_vel = int(math.sqrt(target[0]))
max_x_vel = target[1] + 1
min_y_vel = target[2]
max_y_vel = abs(target[2]) + 1

max_y = 0
viable = 0

for vx in range(min_x_vel, max_x_vel):
    for vy in range(min_y_vel, max_y_vel):
        sim = simulate(vx, vy, target)
        max_y = max(max_y, sim)
        viable += sim >= 0
        
print("max y", max_y)
print("number of viable initial velocities", viable)