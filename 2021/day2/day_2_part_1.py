data = open("../../input/day_2_data.txt")
lines = data.readlines()

horizontal = 0
depth = 0

for line in lines:
    instruction, value = line.split()

    if instruction == "forward":
        horizontal += int(value)
    elif instruction == "down":
        depth += int(value)
    elif instruction == "up":
        depth -= int(value)
        
print(horizontal * depth)