filename = "./../../2022_input/day_3_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()

data = [s.strip() for s in data]
intersections_lower = []
intersections_upper = []

for rucksack in data:
    set_1 = set(rucksack[:len(rucksack) // 2])
    set_2 = set(rucksack[len(rucksack) // 2:])
    element = set_1.intersection(set_2).pop()
    intersections_upper.append(element) if 64 < ord(element) < 91 else intersections_lower.append(element)
    
print(sum([ord(x) - 38 for x in intersections_upper]) + sum([ord(x) - 96 for x in intersections_lower]))
