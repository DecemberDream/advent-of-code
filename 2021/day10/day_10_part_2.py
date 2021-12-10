data = open("../../input/day_10_data.txt")
lines = data.readlines()

brackets = ["()", "[]", "{}", "<>"]
closing = [")", "]", "}", ">"]

corrupt = []
incomplete = []
result_arr = []


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

for incomplete_line in incomplete:
    result = 0

    for c in incomplete_line[::-1]:
        if c == "(":
            result = result * 5 + 1
            #continue
        if c == "[":
            result = result * 5 + 2
            #continue
        if c == "{":
            result = result * 5 + 3
            #continue
        if c == "<":
            result = result * 5 + 4

    result_arr.append(result)
           
print(sorted(result_arr)[len(result_arr) // 2])