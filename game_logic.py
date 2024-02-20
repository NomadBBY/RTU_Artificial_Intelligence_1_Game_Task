import pygame
from constants import BOARD_SIZE, SQUARE_SIZE

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