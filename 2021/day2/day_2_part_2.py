data = open("../../input/day_2_data.txt")
lines = data.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    instruction, value = line.split()

    if instruction == "forward":
        horizontal += int(value)
        depth += aim * int(value)
    elif instruction == "down":
        aim += int(value)
    elif instruction == "up":
        aim -= int(value)
        
print(horizontal * depth)