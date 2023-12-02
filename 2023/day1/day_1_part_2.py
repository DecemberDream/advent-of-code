digits = [str(i) for i in range(1, 10)]
digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

filename = "./../../2023_input/day_1_data.txt"

with open(filename, encoding="utf-8") as f:
    text = f.read().split("\n")

res = 0

for line in text:
    left_idx = len(line) + 1
    right_idx = -1
    left_digit = None
    right_digit = None

    for digit in digits:
        idx_l = line.find(digit)
        idx_r = line.rfind(digit)

        if idx_l < 0 or idx_r < 0:
            continue

        if idx_l < left_idx:
            left_idx = idx_l
            left_digit = digit
        if idx_r > right_idx:
            right_idx = idx_r
            right_digit = digit

    for digit in digit_words:
        idx_l = line.find(digit)
        idx_r = line.rfind(digit)

        if idx_l < 0 or idx_r < 0:
            continue

        if idx_l < left_idx:
            left_idx = idx_l
            left_digit = digit
        if idx_r > right_idx:
            right_idx = idx_r
            right_digit = digit

    left_digit = left_digit if len(left_digit) == 1 else str(digit_words.index(left_digit))
    right_digit = right_digit if len(right_digit) == 1 else str(digit_words.index(right_digit))

    res += int(left_digit + right_digit)

print(res)
