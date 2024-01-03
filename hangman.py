import random

def choose_word():
    word_list = ["python", "hangman", "programming", "computer", "keyboard"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |      
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """
    ]
    
    return stages[attempts]

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts before the player loses

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)
        print(draw_hangman(6 - attempts))

        if "_" not in current_display:
            print("Congratulations! You've won. The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Sorry, that letter is not in the word.")
            attempts -= 1

    if attempts == 0:
        print("You're out of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
