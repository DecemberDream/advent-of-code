from collections import Counter


filename = "./../../2022_input/day_6_data.txt"
n = 14

with open(filename, "r", encoding="utf-8") as file:
    data = file.readline()

for i in range(len(data) - (n-1)):
    if len(Counter(data[i:i+n])) == n:
        print(i+n)
        break