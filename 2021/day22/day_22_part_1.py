import numpy as np
from collections import defaultdict


data = open("../../input/day_22_data.txt").readlines()

steps = defaultdict(list)

for i, line in enumerate(data):
    line = line.strip().split(" ")
    x, y, z = line[1:][0].split(",")
    
    steps[i].append(line[0])
    
    for axis in [x, y, z]:
        ranges = axis.split("=")[1]
        start = int(ranges.split("..")[0])
        end = int(ranges.split("..")[1]) + 1
        
        if -50 <= start <= end <= 51:
            steps[i].append(slice(start + 50, end + 50))

steps = {k: v for k, v in steps.items() if len(v) == 4}
        
reactor = np.zeros((100, 100, 100), dtype=bool)

for step in steps.values():
    instruction = step[0]
    x, y, z = step[1:4]
    
    reactor[x, y, z] = 1 if instruction == "on" else 0
        
print(np.sum(reactor))