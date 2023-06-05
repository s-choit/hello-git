import random
import pickle

def save_game(word, guessed_letters, attempts_left):
    game_data = {
        "word": word, 
        "guessed_letters": guessed_letters,
        "attempts_left": attempts_left
    }
    with open("hangman_game.pkl", "wb") as file:
        pickle.dump(game_data, file)
    print("Game saved successfully!")

def load_game():
    try:
        with open("Hangman_game.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def get_word():
    word_list = ["apple", "banana", "cat", "dog", "elephant", "fish", "giraffe", "horse", "iguana", "jellyfish"]
    return random.choice(word_list)

def print_hangman(attempts_left):
    hangman =[
        """
            +---+
                |
                |
                |
               ===
        """,
        """
            +---+
            O   |
                |
                |
               ===
        """,
        """
            +---+
            O   |
            |   |
                |
               ===
        """,
        """
            +---+
            O   |
           /|   |
                |
               ===
        """,
        """
            +---+
            O   |
           /|\\ |
                |
               ===
        """,
        """
            +---+
            O   |
           /|\\ |
           /    |
               ===
        """,
        """
            +---+
            O   |
           /|\\ |
           / \\ |
               ===
        """
    ]
    print(hangman[6 - attempts_left])

def play_game():
    word = get_word()
    guessed_letters = []
    attempts_left = 6
    score = load_score()
    print ("Stats: wins: ", score[0], "losses: ", score[1])

    while True:
        print_hangman(attempts_left)

        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        print(masked_word)

        guess = input("Guess a letter:").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                guessed_letters.append(guess)
                if guess in word:
                    print("Correct guess!")
                else:
                    attempts_left -= 1
                    print("Wrong guess!")
        else:
            print("Invalid input. Please enter a simple letter.")
        
        if attempts_left ==0:
            print_hangman(attempts_left)
            print("You lost! The word was:", word)
            score[1] += 1
            save_score(score)
            break
            
        if all(letter in guessed_letters for letter in word):
            print("Congrats! You won!")
            score[0] += 1
            save_score(score)
            break
        
    print("Final score: wins: ", score[0], "losses: ", score[1])





#saved_game = load_game()
#if saved_game:
#    word = saved_game["word"]
#    guessed_letters = saved_game["guessed_letters"]
#    attempts_left = saved_game["attempts_left"]
#    print(attempts_left)
#    print ("Loaded saved game")
#else:
#    word = get_word()
#    guessed_letters = []
#    attempts_left = 6
#    print("Starting a new game")

def save_score(score):
    with open("hangman_score.pkl", "wb") as file:
        pickle.dump(score, file)
    print("Score saved successfully!")

def load_score():
    try:
        with open("hangman_score.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return [0,0]

def score_win (score):
    score[0]+=1

def score_loss(score):
    score[1]+=1

def update_score(score):
    print(score)

"""
def play_game():
    word = get_word()
    guessed_letters = []
    attempts_left = 6
    score = [0, 0]  # wins and losses
    while True:
        if attempts_left ==0:
            score_loss(score)
            break
        if all(letter in guessed_letters for letter in word):
            update_score(score,1)
            break
        choice = input("Do you want to save and quit? (y/n): ")
        if choice.lower() == "y":
            save_game(word, guessed_letters, attempts_left)
            break
"""

if __name__ == "__main__":
    play_game()
    

 

#        save_game(board)