import numpy as np
import random as rd

chess_board = np.arange(1, 65).reshape(8, 8)

def put_queen(position_of_queen):
    add_to_banned_pieces(position_of_queen)

def add_to_banned_pieces(position_of_queen):
    position_y = np.where(chess_board == position_of_queen)[1][0]
    for left_cross in range(position_of_queen - (position_y * 9), position_of_queen + 1 + ((7-position_y)*9), 9):
        if 65 > left_cross > 0:
            banned_pieces.add(left_cross)
    for right_cross in range(position_of_queen - ((7-position_y) * 7), position_of_queen + 1 + (position_y*7), 7):
        if 65 > right_cross > 0:
            banned_pieces.add(right_cross)

    for horizontal in chess_board:
        if position_of_queen in horizontal:
            for piece_in_horizontal in horizontal:
                banned_pieces.add(piece_in_horizontal)
            
            for piece_in_vertical in range(len(chess_board)):
                banned_pieces.add(chess_board[piece_in_vertical, position_y])

def convert_to_chess_coordinate(array1, array2):
    finale_state = []
    verticals = "habcdefg"
    for horizontal, vertical in zip(array1, array2):
        finale_state.append(f"{verticals[(vertical % 8)]}{8 - horizontal}")
    
    print("It have been tried {} times.".format(num_of_attempt + 1))
    print(chess_board)
    print(positions_of_queens)
    
    return finale_state

crosses = set()
positions_of_queens = []
horizontals = []
banned_pieces = set()

num_of_attempt = 0
num_of_queens_to_put = 8

choice_range = list(range(1, 65))

while num_of_queens_to_put > 0:
    random_pos = rd.choice(choice_range)
    if len(banned_pieces) != 64:
        if random_pos not in banned_pieces:
            horizontals.append(np.where(chess_board == random_pos)[0][0])
            put_queen(random_pos)
            positions_of_queens.append(random_pos)
            
            num_of_queens_to_put -= 1
            choice_range.remove(random_pos)
            print("Queen placed successfully!")
    else:    
        print("Returning to start...")
        print("Successfully attempts : {}".format(8 - num_of_queens_to_put))
        positions_of_queens.clear()
        banned_pieces.clear()
        horizontals.clear()
        num_of_queens_to_put = 8
        num_of_attempt += 1
        choice_range = list(range(1, 65))


print(convert_to_chess_coordinate(horizontals, positions_of_queens))
