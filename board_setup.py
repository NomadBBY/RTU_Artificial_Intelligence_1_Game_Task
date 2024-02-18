import pygame
from pygame.locals import *
from constants import SQUARE_SIZE, FONT_SIZE

def draw_squares(game_screen):
    """
    Draws the game board grid.
    """
    # Fill the screen with black color
    game_screen.fill((0, 0, 0))
    
    # Loop through rows and columns to draw squares
    for row in range(8):
        for col in range(row % 2, 8, 2):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            square_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            # Draw a rectangle representing a square on the grid
            pygame.draw.rect(game_screen, (255, 117, 24), square_rect)

def draw_pieces(game_screen, hound_positions, fox_position):
    """
    Draws all game pieces on the board.
    """
    # Draw hound pieces
    for position in hound_positions:
        x, y = position[1] * SQUARE_SIZE, position[0] * SQUARE_SIZE
        # Draw a circle representing a hound
        pygame.draw.circle(game_screen, (128, 128, 128), (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2), SQUARE_SIZE // 3)

    # Draw fox piece
    x, y = fox_position[1] * SQUARE_SIZE, fox_position[0] * SQUARE_SIZE
    # Draw a circle representing the fox
    pygame.draw.circle(game_screen, (255, 117, 24), (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
