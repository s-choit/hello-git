#Erica, Tiffany, Sophie


#import pickle
#board = [[''for _ in range (3)] for _ in range(3)]
#def print_board(board):
#    for row in board:
#        row_str=""
#        for cell in row:
#            row_str += cell + "I"
#            print(row_str[:-1])
#            print("-"*5)

#def is_board_full(board):
#    for row in board:
#        if " " in row:
#            return False
#    return True
#def is_winner(board, mark):
#    for row in board:
#        if row.count(mark) == 3:
#           return True 
    
#    for col in range(3):
#        if board[0][col] == board[1][col] == board[2][col] == mark:
#            return True
    
#    if board[0][0] == board[1][1] == board[2][2] == mark: 
#        return True
#    if board[0][2] == board[1][1] == board[2][0] == mark:
#        return True
    
#    return False
#def save_game(board):
#    with open("tic_tac_toe.pkl", "wb") as file: 
#        pickle.dump(board, file)

#def save_scores(wins, losses):
#    scores = (wins, losses)
#    with open("score.pkl", "wb") as file:
#        pickle.dump(scores, file)
#def load_game():
#    try:
#        with open("tic_tac_toe.pkl","rb") as file:
#            return pickle.load(file)
#    except FileNotFoundError:
#        return None

import json
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end = " I ")
        print('\n' + "-" *9)

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
        return True
def is_winner (board, mark):
    for row in board:
        if row.count(mark) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board [2][0] == mark:
        return True
    return False

