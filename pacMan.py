import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 36
WORD_FONT_SIZE = 48
WORD_LIST = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS"]
MAX_WRONG_GUESSES = 6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load hangman images
hangman_images = [pygame.image.load(f"hangman{index}.png") for index in range(MAX_WRONG_GUESSES + 1)]

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hangman Game")

# Fonts
font = pygame.font.Font(None, FONT_SIZE)
word_font = pygame.font.Font(None, WORD_FONT_SIZE)

# Initialize game variables
word_to_guess = random.choice(WORD_LIST)
guessed_letters = set()
wrong_guesses = 0
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in word_to_guess:
                        wrong_guesses += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw hangman image
    screen.blit(hangman_images[wrong_guesses], (50, 50))

    # Draw word with underscores and guessed letters
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_surface = word_font.render(display_word, True, BLACK)
    screen.blit(word_surface, (50, 400))

    # Check if the player has won or lost
    if all(letter in guessed_letters for letter in word_to_guess):
        game_over_text = font.render("You Win!", True, BLACK)
        screen.blit(game_over_text, (300, 200))
        game_over = True
    elif wrong_guesses >= MAX_WRONG_GUESSES:
        game_over_text = font.render("You Lose!", True, BLACK)
        screen.blit(game_over_text, (300, 200))
        game_over = True

    pygame.display.flip()

# Wait for a key press to exit
waiting_for_key = True
while waiting_for_key:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting_for_key = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                waiting_for_key = False
            else:
                game_over = False
                word_to_guess = random.choice(WORD_LIST)
                guessed_letters = set()
                wrong_guesses = 0
    pygame.quit()

