data = open("../../input/day_8_data.txt")
lines = data.readlines()

pattern = []
output = []

for line in lines:
    split_line = line.split("|")
    pattern.append(["".join(sorted(c)) for c in split_line[0].split()])
    output.append(["".join(sorted(c)) for c in split_line[1].split()])

data.close()

result = 0

for i in range(len(pattern)):
    digits = {}
    
    while len(digits) < 10:
        for digit in pattern[i]:
            # trivial cases
            if len(digit) == 2 and 1 not in digits:
                digits[1] = digit
                continue
            if len(digit) == 3 and 7 not in digits:
                digits[7] = digit
                continue
            if len(digit) == 4 and 4 not in digits:
                digits[4] = digit
                continue
            if len(digit) == 7 and 8 not in digits:
                digits[8] = digit
                continue
            
            # either 2 or 5 or 3
            if len(digit) == 5:
                if 7 in digits and all([i in list(digit) for i in list(digits.get(7))]):
                    digits[3] = digit
                elif 9 in digits and all([i in list(digits.get(9)) for i in list(digit)]):
                    digits[5] = digit
                elif 9 in digits:
                    digits[2] = digit
            
            # either 0 or 6 or 9
            if len(digit) == 6:
                if 3 in digits and all([i in list(digit) for i in list(digits.get(3))]):
                    digits[9] = digit
                elif 5 in digits and sum([i in list(digits.get(5)) for i in list(digit)]) == 5:
                    digits[6] = digit
                elif 5 in digits and sum([i in list(digits.get(5)) for i in list(digit)]) == 4:
                    digits[0] = digit

    out_num_1 = []
    
    for out_pos in range(4):
        out_num_1.append([k for k, v in digits.items() if v == output[i][out_pos]][0])
        
    result += int("".join([str(c) for c in out_num_1]))

print(result)
