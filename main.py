import pygame
from pygame.locals import *
from board_setup import *
from constants import *
from game_logic import *
from choose_player import * 

def main():
    # Initialize pygame
    pygame.init()

    # Set up the welcome screen
    welcome_screen = pygame.display.set_mode(WELCOME_SCREEN)

    # Ask the user to choose a player and get the chosen player
    player = choose_player(welcome_screen)

    # Set up the game screen
    game_screen = pygame.display.set_mode(SCREEN_SIZE)

    # Initialize the positions of hounds and fox
    hounds = [(0, 1), (0, 3), (0, 5), (0, 7)]
    fox = (7, 4)

    # Set the current player to the chosen player
    current_player = player

    # Print the current player for debugging
    print(current_player)

    # Start the game loop
    initialize_game(game_screen, player, hounds, fox, current_player)

    # Quit pygame when the game loop ends
    pygame.quit()

if __name__ == "__main__":
    main()
