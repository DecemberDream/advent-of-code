def move(d: dict, n: int, f: int, t: int) -> dict:
    for i in range(n):
        e = list(d[f].pop(n-(i+1)))
        d[t] = e + d[t]

    return d


filename = "./../../2022_input/day_5_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()

total_cols = -1
stacks = dict()

for line in data:
    split_line = line.split(" ")

    if split_line[0] != "move":
        for i, char in enumerate(line):
            if char.isalpha():
                total_cols = len(line) // 4
                col_num = int(i / len(line) * total_cols) + 1

                if col_num not in stacks:
                    stacks[col_num] = []

                stacks[col_num] += char
    else:
        quantity, from_col, to_col = int(split_line[1]), int(split_line[3]), int(split_line[5])
        stacks = move(stacks, quantity, from_col, to_col)

for i in range(1, total_cols + 1):
    print(stacks[i][0], end="")