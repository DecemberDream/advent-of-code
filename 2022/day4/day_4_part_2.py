def is_partially_contained(a: list, b: list) -> bool:
    return int((a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1])
    or (b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]))


filename = "./../../2022_input/day_4_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.read().split()

counter = 0

for pair in data:
    sec1 = [int(x) for x in pair.split(",")[0].split("-")]
    sec2 = [int(x) for x in pair.split(",")[1].split("-")]
    counter += is_partially_contained(sec1, sec2)

print(counter)