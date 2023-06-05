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

    while True:
        print_hangman(attempts_left)

        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        print(masked_word)
