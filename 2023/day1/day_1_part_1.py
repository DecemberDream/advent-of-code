import re


filename = "./../../2023_input/day_1_data.txt"

with open(filename, encoding="utf-8") as f:
    text = f.read().split("\n")

res = 0

for line in text:
    digits = re.findall(r"\d", line)
    res += int(digits[0] + digits[-1])

print(res)
