import pygame
from pygame.locals import *

# Define colors and constants
class Colours:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BLUE = (0, 0, 255)

class Constants:

    SQUARE_SIZE = 100
    SCREEN_SIZE = (600, 600)

# Function to draw squares
def draw_squares(game_screen, colors, square_size):

    game_screen.fill(colors.BLACK)
    for row in range(8):
        for col in range(row % 2, 8, 2):
            x = col * square_size
            y = row * square_size
            square_rect = pygame.Rect(x, y, square_size, square_size)
            pygame.draw.rect(game_screen, colors.RED, square_rect)





# Initialize pygame
pygame.init()
game_screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    draw_squares(game_screen, Colours, Constants.SQUARE_SIZE)
    pygame.display.flip()

# Quit pygame
pygame.quit()
