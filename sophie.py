#print("Hello world")
def save_game(board):
    with open('tic_tac_toe.json','w') as file:
        json.dump(board,file)
    print("Game successfuly ")

def load_game():
    try:
        with open('tic_tac_toe.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None