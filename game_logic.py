import pygame
from pygame.locals import *
from board_setup import draw_squares, draw_pieces

def initialize_game(game_screen, player, hounds, fox, current_player):
    """
    Initializes and starts the game loop.
    """
    pygame.init()  # Initialize Pygame here
    print("Welcome to Fox and Hounds!")
    while True:  # Main game loop
        for event in pygame.event.get():  # Check for events
            if event.type == QUIT:  # If the user quits the game
                pygame.quit()  # Quit Pygame
                return  # Exit the function and stop the game loop

        # Draw the game board and pieces
        draw_squares(game_screen)  # Draw the game board grid
        draw_pieces(game_screen, hounds, fox)  # Draw all game pieces on the board
        pygame.display.flip()  # Update the display to show the changes

