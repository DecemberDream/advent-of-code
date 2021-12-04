import numpy as np


def check_rows_and_cols(a, finished=None):
    # z, row, col
    for z_index in range(len(a)):
        if z_index in finished:
            continue
        for row in range(5):
            for col in range(5):
                check_rows = np.prod(a[z_index, :, col])
                check_cols = np.prod(a[z_index, row, :])
                
                if check_rows:
                    return z_index, col
                if check_cols:
                    return z_index, row
                
    return -1, -1
    


data = open("../../input/day_4_data.txt")

numbers = []
board_starting_line = 2
board = []

lines = data.readlines()
lines = np.array(lines)

for row, line in enumerate(lines):  
    if row == 0:
        numbers = np.array([int(c) for c in line.split(",")])
    
    elif board_starting_line == row:
        board_block = lines[row:row+5]

        for i in range(5):
            board.append([int(c) for c in board_block[i].rstrip("\n").split()])

        board_starting_line += 6

data.close()

board = np.array(board)
board = board.reshape(board.shape[0] // board.shape[1], 5, 5)
mask = np.zeros_like(board, dtype=bool)

won = False
last_number = None
winning_board = None
finished_boards = set()

for number in numbers:
    if won:
        break
    
    indices = np.argwhere(board == number)
    
    for index in indices:
        mask[index[0], index[1], index[2]] = True
        z_index, row_col = check_rows_and_cols(mask, finished_boards)
        
        if z_index >= 0 and row_col >= 0:
            last_number = number
            winning_board = z_index
            finished_boards.add(winning_board)

            if len(finished_boards) == board.shape[0]:
                won = True
                break


anti_mask = np.ones_like(mask).astype(bool) ^ mask

sum_of_unmarked= np.sum(board[winning_board, :, :] * anti_mask[winning_board, :, :])
print(sum_of_unmarked * last_number)