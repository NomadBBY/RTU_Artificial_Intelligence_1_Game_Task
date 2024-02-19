import pygame
from pygame.locals import *
from board_setup import *
from constants import *
from game_logic import *
from choose_player import * 

class YourGameClassName:
    def __init__(self):
        self.game_screen = None
        self.fox = (7, 4)

    def ask_for_fox_coordinates(self):

        print("Click on the new position for the fox:")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x //= SQUARE_SIZE  # Assuming SQUARE_SIZE is the size of each square on the board
                    y //= SQUARE_SIZE  # Assuming SQUARE_SIZE is the size of each square on the board
                    if (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE) and (abs(x - self.fox[0]) == abs(y - self.fox[1])):
                        self.fox = (x, y)
                        return  # Exit the loop when valid coordinates are obtained
                    else:
                        print("Invalid position. Please click on a diagonal square relative to the current fox position.")

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

        initialize_game(self.game_screen, player, [], self.fox, current_player)  # Pass an empty list for hounds

        self.ask_for_fox_coordinates()

        # Start the game loop
        # initialize_game(self.game_screen, player, [], self.fox, current_player)  # Pass an empty list for hounds

        # Quit pygame when the game loop ends
        pygame.quit()

if __name__ == "__main__":
    game_instance = YourGameClassName()
    game_instance.main()
