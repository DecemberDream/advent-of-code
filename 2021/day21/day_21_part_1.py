def get_dice_sum(x_old, dice_min=1, dice_max=101):
    dice_sum = 0
    
    for x in range(x_old + 1, x_old + 4):
        dice_sum += (((x - dice_min) % (dice_max - dice_min)) + (dice_max - dice_min)) % (dice_max - dice_min) + dice_min
    
    return dice_sum, x_old + 3


data = open("../../input/day_21_data.txt").readlines()

p1_idx = int(data[0].strip()[-1])
p2_idx = int(data[1].strip()[-1])

p1_total = 0
p2_total = 0

throw_counter = 0
dice_side = 0

while p1_total < 1000 and p2_total < 1000:
    dice_val = 0
    
    # for player 1
    dice_val, dice_side = get_dice_sum(dice_side)
    throw_counter += 3
    p1_idx = ((p1_idx + dice_val) % 10 + 10) % 10
    
    if p1_idx == 0:
        p1_idx = 10
        
    p1_total += p1_idx
    
    if p1_total > 999:
        break
    
    # for player 2
    dice_val, dice_side = get_dice_sum(dice_side)
    throw_counter += 3
    p2_idx = ((p2_idx + dice_val) % 10 + 10) % 10
    
    if p2_idx == 0:
        p2_idx = 10
        
    p2_total += p2_idx
    
    if p2_total > 999:
        break
    
print(p1_total, p2_total, throw_counter)
print(f"{p2_total} * {throw_counter} = ", p2_total * throw_counter)