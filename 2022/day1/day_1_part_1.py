filename = "./../../2022_input/day_1_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.read()

a = data.split("\n\n")
max = 0

for elf in a:
    if sum([int(x) for x in elf.split("\n")]) > max:
        max = sum([int(x) for x in elf.split("\n")])

print(max)