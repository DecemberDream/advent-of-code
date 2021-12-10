data = open("../../input/day_10_data.txt")
lines = data.readlines()

brackets = ["()", "[]", "{}", "<>"]
closing = [")", "]", "}", ">"]

corrupt = []
incomplete = []
result = []

for line in lines:
    while any(x in line for x in brackets):
        for bracket in brackets:
            line = line.replace(bracket, "")

    # check whether the line is corrupted or incomplete
    for closed in closing:
        # not needed for part 2
        if any(x in line for x in closing):
            corrupt.append(line)
            break
        if not all(x in line for x in closing):
            incomplete.append(line)
            break

for incomplete_line in incomplete:
    acc = 0

    for c in incomplete_line[::-1]:
        if c == "(":
            acc = acc * 5 + 1
        elif c == "[":
            acc = acc * 5 + 2
        elif c == "{":
            acc = acc * 5 + 3
        elif c == "<":
            acc = acc * 5 + 4

    result.append(acc)
           
print(sorted(result)[len(result) // 2])