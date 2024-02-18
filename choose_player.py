import pygame
from pygame.locals import *
from constants import WHITE, BLACK, ORANGE

def choose_player(game_screen):
    """
    Method to ask the user who should start first using buttons.
    """
    # Define the position and size of the buttons
    player_one_button = pygame.Rect(75, 175, 150, 50) # X, Y, Width, Height
    player_two_button = pygame.Rect(375, 175, 150, 50) 

    # Position for the text above the buttons
    text_chose_player_x = game_screen.get_width() // 2
    text_chose_player_y = 110

    # Position for the game name text
    game_name_x = game_screen.get_width() // 2
    game_name_y = 45

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if player_one_button.collidepoint(event.pos):
                    return "Human"
                elif player_two_button.collidepoint(event.pos):
                    return "Computer"
            elif event.type == QUIT:
                return None

        # Fill the screen with black color
        game_screen.fill((BLACK))

        # Draw buttons
        pygame.draw.rect(game_screen, (WHITE), player_one_button)
        pygame.draw.rect(game_screen, (WHITE), player_two_button)

        # Render text above the buttons
        text_font = pygame.font.Font(None, 60)
        text_surface = text_font.render("Fox and Hounds", True, (ORANGE))
        text_rect = text_surface.get_rect(center=(game_name_x, game_name_y))
        game_screen.blit(text_surface, text_rect)

        # Render text above the buttons
        text_font = pygame.font.Font(None, 30)
        text_surface = text_font.render("Choose Player", True, (ORANGE))
        text_rect = text_surface.get_rect(center=(text_chose_player_x, text_chose_player_y))
        game_screen.blit(text_surface, text_rect)

        # Render text on the buttons
        button_font = pygame.font.Font(None, 30)
        text_surface = button_font.render("Human", True, (ORANGE))
        text_rect = text_surface.get_rect(center=player_one_button.center)
        game_screen.blit(text_surface, text_rect)

        text_surface = button_font.render("Computer", True, (ORANGE))
        text_rect = text_surface.get_rect(center=player_two_button.center)
        game_screen.blit(text_surface, text_rect)

        pygame.display.flip()
