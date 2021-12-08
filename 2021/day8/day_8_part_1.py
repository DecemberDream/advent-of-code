data = open("../../input/day_8_data.txt")
lines = data.readlines()

output = []

for line in lines:
    split_line = line.split("|")
    output.append([c for c in split_line[1].split()])

data.close()

counter = 0

for i in range(len(output)):
    for digit in output[i]:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            counter += 1
        
print(counter)