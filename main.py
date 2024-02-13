import pygame
from pygame.locals import *

class Colours:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BLUE = (0, 0, 255)

class Constants:
    
    SQUARE_SIZE = 100
    SCREEN_SIZE = (700, 700)

class BoardSetup:
    
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen

    def draw_squares(self):
        self.game_screen.fill(Colours.BLACK)
        for row in range(8):
            for col in range(row % 2, 8, 2):
                x = col * Constants.SQUARE_SIZE
                y = row * Constants.SQUARE_SIZE
                square_rect = pygame.Rect(x, y, Constants.SQUARE_SIZE, Constants.SQUARE_SIZE)
                pygame.draw.rect(self.game_screen, Colours.WHITE, square_rect)

    @staticmethod
    def get_row_from_mouse(position):
        x_cord, y_cord = position
        row_index = x_cord // Constants.SQUARE_SIZE
        col_index = y_cord // Constants.SQUARE_SIZE
        return row_index, col_index
    

    class GameBoard():

        def __init__(self):
            # Initialize instance variables to track the game state
            self.game_board = []  # List containing the game board
            self.red_pieces_remaining = 12  # Number of remaining red pieces
            self.white_pieces_remaining = 12  # Number of remaining white pieces
            self.num_red_kings = 0  # Number of red kings
            self.num_white_kings = 0  # Number of white kings
            self.create_board()

        def calculate_score(self, king_weight=0.5):  
            #  Aprēķina rezultātu, pamatojoties uz atšķirību starp katras krāsas gabalu skaitu un karaļa figūru skaitu
            return self.white_pieces_remaining - self.red_pieces_remaining + (self.num_white_kings * king_weight - self.num_red_kings * king_weight)


# Initialize pygame
pygame.init()
game_screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

# Create a board instance
board = BoardSetup(game_screen)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    board.draw_squares()
    pygame.display.flip()

# Quit pygame
pygame.quit()
