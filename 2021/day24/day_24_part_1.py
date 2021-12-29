from itertools import product


def works(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0

    for i in range(14):
        increment, mod_req = steps[i], required[i]

        if increment == None:
            res[i] = ((z % 26) - mod_req)
            z //= 26
            
            if not 1 <= res[i] <= 9:
                return False

        else:
            z = z * 26 + digits[digits_idx] + increment
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res


steps = [0, 12, 14, 0, None, 15, 11, None, 1, None, None, None, None, None]
required = [None, None, None, None, 2, None, None, 15, None, 9, 9, 7, 4, 6]

input_space = product(range(9, 0, -1), repeat=7)

for digits in input_space:
    res = works(digits)
    
    if res:
        print("".join([str(i) for i in res]))
        break