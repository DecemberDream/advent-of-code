filename = "./../../2022_input/day_3_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()

data = [s.strip() for s in data]
intersections_lower = []
intersections_upper = []

for i in range(0, len(data) - 2, 3):
    group = data[i:i+3]
    set_1 = set(group[0])
    set_2 = set(group[1])
    set_3 = set(group[2])
    element = set_1.intersection(set_2).intersection(set_3).pop()
    intersections_upper.append(element) if 64 < ord(element) < 91 else intersections_lower.append(element)

print(sum([ord(x) - 38 for x in intersections_upper]) + sum([ord(x) - 96 for x in intersections_lower]))
