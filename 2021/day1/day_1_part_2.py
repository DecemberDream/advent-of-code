data = open("../../input/day_1_data.txt")
lines = data.readlines()

counter = 0
num_data = []

for line in lines:
    num_data.append(int(line))
    
prev_sum = 0

for i in range(0, len(num_data) - 2):
    sum_of_threes = sum(num_data[i:i+3])

    if sum_of_threes > prev_sum:
        counter += 1
        
    prev_sum = sum_of_threes
    
print(counter - 1)