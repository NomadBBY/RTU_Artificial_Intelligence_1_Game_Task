import pygame
from CONSTANTS import BOARD_SIZE, SQUARE_SIZE

def get_cords_from_mouse():
    pass

# Definē funkciju, lai iegūtu kvadrāta rindu un kolonnu, pamatojoties uz spēlētāja peles pozīciju
def get_row_col_from_mouse(pos):
    pass
    # # Peles pozīcijas x un y koordinātas
    # x, y = pos
    # row_index = y // SQUARE
    # col_index = x // SQUARE
    # return row_index, col_index

def draw_valid_moves(self, moves):
    pass
#         # Parāda ceļu ko spelētājs var izvēlēties
#         for move in moves:
#             row, col = move
#             # Aprēķina apļa centra koordinātas, pamatojoties uz rindu un kolonnu
#             # no derīgā gājiena un katra laukuma lielums uz galda
#             pygame.draw.circle(self.game_window, BLUE, (col * SQUARE + SQUARE // 2, row * SQUARE + SQUARE // 2), 15)

def ask_for_fox_coordinates(fox):
    print("Click on the new position for the fox:")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= SQUARE_SIZE  # Assuming SQUARE_SIZE is the size of each square on the board
                y //= SQUARE_SIZE  # Assuming SQUARE_SIZE is the size of each square on the board
                if (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE) and (abs(x - fox[0]) == abs(y - fox[1])):
                    return (x, y)  # Return valid coordinates
                else:
                    print("Invalid position. Please click on a diagonal square relative to the current fox position.")

def ask_for_hound_cordinates():
    pass