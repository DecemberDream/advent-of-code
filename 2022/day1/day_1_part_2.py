filename = "./../../2022_input/day_1_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.read()

a = data.split("\n\n")
calories_list = []

for elf in a:
    calories_list.append(sum([int(x) for x in elf.split("\n")]))

print(sum(sorted(calories_list)[len(calories_list) - 3:]))
