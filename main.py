import pygame
from pygame.locals import *

class Colours:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BLUE = (0, 0, 255)
    ORANGE = (255, 117, 24)

class Constants:
    SQUARE_SIZE = 100
    SCREEN_SIZE = (800, 800)

class BoardSetup:
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen
        self.hound_image = pygame.transform.scale(pygame.image.load('hound_image.png'), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))  # Load hound image and resize it to fit the square
        self.fox_image = pygame.transform.scale(pygame.image.load('fox_image.png'), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))  # Load fox image and resize it to fit the square

    def draw_squares(self):
        self.game_screen.fill(Colours.ORANGE)
        for row in range(8):
            for col in range(row % 2, 8, 2):
                x = col * Constants.SQUARE_SIZE
                y = row * Constants.SQUARE_SIZE
                square_rect = pygame.Rect(x, y, Constants.SQUARE_SIZE, Constants.SQUARE_SIZE)
                pygame.draw.rect(self.game_screen, Colours.BLACK, square_rect)

    @staticmethod
    def get_row_from_mouse(position):
        x_cord, y_cord = position
        row_index = x_cord // Constants.SQUARE_SIZE
        col_index = y_cord // Constants.SQUARE_SIZE
        return row_index, col_index

    def draw_piece(self, window, x_pos, y_pos, image):
        radius = Constants.SQUARE_SIZE // 3
        # Calculate the center of the image
        image_center_x = x_pos + image.get_width() // 2
        image_center_y = y_pos + image.get_height() // 2
        # Calculate the center of the circle
        circle_center = (image_center_x, image_center_y - 2.5)
        pygame.draw.circle(window, Colours.BLACK, circle_center, radius + 2)
        # Calculate the top-left position of the image to draw it centered
        image_top_left = (image_center_x - image.get_width() // 2, image_center_y - image.get_height() // 2)
        window.blit(image, image_top_left)


    def draw_pieces(self, hound_positions, fox_position):
        for position in hound_positions:
            x, y = position[1] * Constants.SQUARE_SIZE, position[0] * Constants.SQUARE_SIZE
            self.draw_piece(self.game_screen, x, y, self.hound_image)
        x, y = fox_position[1] * Constants.SQUARE_SIZE, fox_position[0] * Constants.SQUARE_SIZE
        self.draw_piece(self.game_screen, x, y, self.fox_image)

class FoxAndHounds:
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.board = BoardSetup(game_screen)
        self.hounds = [(0, 1), (0, 3), (0, 5), (0, 7)]  # Initial positions of hounds
        self.fox = (7, 4)  # Initial position of the fox
        self.current_player = 'Fox'

    def play(self):
        print("Welcome to Fox and Hounds!")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
            self.board.draw_squares()
            self.board.draw_pieces(self.hounds, self.fox)
            pygame.display.flip()

# Initialize pygame
pygame.init()
game_screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

# Create a Fox and Hounds game instance
game = FoxAndHounds(game_screen)

# Main loop
game.play()

# Quit pygame
pygame.quit()
