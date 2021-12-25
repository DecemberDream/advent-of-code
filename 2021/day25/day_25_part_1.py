import numpy as np


def move(region, direction):
    to_move = region == direction
    look_ahead = np.roll(region, -1, 1 if direction == 1 else 0)
    
    to_move[look_ahead != 0] = False
    region[to_move] = 0
    
    move_forward = np.roll(to_move, 1, 1 if direction == 1 else 0)
    region[move_forward] = direction

    return len(region[to_move])


region = np.array([list(line.replace(">", "1").replace("v", "2").replace(".", "0").strip())
          for line in open("../../input/day_25_data.txt").readlines()], dtype=np.uint8)

steps = 1

while move(region, 1) + move(region, 2) > 0:
    steps += 1
    
print(steps)