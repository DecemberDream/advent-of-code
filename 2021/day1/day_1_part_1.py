data = open("../../input/day_1_data.txt")
lines = data.readlines()

counter = 0
prev_num = 0

for line in lines:
    num = int(line)
    counter += 1 * (num > prev_num)
    prev_num = num
    
print(counter - 1)