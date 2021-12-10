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
        if any(x in line for x in closing):
            corrupt.append(line)
            break
        if not all(x in line for x in closing):
            incomplete.append(line)
            break

for corr_line in corrupt:
    for c in corr_line:
        if c == ")":
            result.append(3)
            break
        if c == "]":
            result.append(57)
            break
        if c == "}":
            result.append(1197)
            break
        if c == ">":
            result.append(25137)
            break
            
print(sum(result))