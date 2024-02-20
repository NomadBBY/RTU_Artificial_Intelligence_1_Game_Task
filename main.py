# main.py
import pygame
from pygame.locals import *
from board_setup import *
from constants import *
from game_logic import ask_for_fox_coordinates
from choose_player import *

class GameClass:

    def __init__(self):
        self.game_screen = None
        self.fox = (7, 4)

    def initialize_game(self):
        """
        Initializes and starts the game loop.
        """
        print("Welcome to Fox and Hounds!")
        while True:  # Main game loop
            for event in pygame.event.get():  # Check for events
                if event.type == QUIT:  # If the user quits the game
                    pygame.quit()  # Quit Pygame
                    return  # Exit the function and stop the game loop

            # Draw the game board and pieces
            draw_squares(self.game_screen)  # Draw the game board grid
            draw_pieces(self.game_screen, [], self.fox)  # Draw all game pieces on the board
            pygame.display.flip()  # Update the display to show the changes

    def main(self):
        # Initialize pygame
        pygame.init()

        # Set up the welcome screen
        welcome_screen = pygame.display.set_mode(WELCOME_SCREEN)

        # Ask the user to choose a player and get the chosen player
        player = choose_player(welcome_screen)

        # Set up the game screen
        self.game_screen = pygame.display.set_mode(SCREEN_SIZE)

        # Set the current player to the chosen player
        current_player = player

        # Print the current player for debugging
        print(current_player)

        self.initialize_game(player, current_player)

        # Ask for fox coordinates using the method from game_logic.py
        self.fox = ask_for_fox_coordinates(self.fox)

        # Quit pygame when the game loop ends
        pygame.quit()

if __name__ == "__main__":
    game_instance = GameClass()
    game_instance.main()
