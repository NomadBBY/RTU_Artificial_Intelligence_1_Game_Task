import pygame

class GameWindow:
    
    def __init__(self, width=600, height=350):
        self.game = pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))

    def welcome_screen(self):

        button1_rect = pygame.Rect(120, 200, 120, 35)  # Adjusted button 1 position
        button2_rect = pygame.Rect(360, 200, 120, 35)  # Adjusted button 2 position

        button_font = pygame.font.Font(None, 24) #Font for the buttons
        title_font = pygame.font.Font(None, 50) #Font for the title text
        text_font = pygame.font.Font(None, 36) #Font for the under text

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if button 1 is clicked
                        if button1_rect.collidepoint(event.pos):
                            print("Button 1 clicked!")
                            return 'human'
                        # Check if button 2 is clicked
                        elif button2_rect.collidepoint(event.pos):
                            print("Button 2 clicked!")
                            return 'computer'

            self.window.fill((225, 217, 196))  # Fill window with color

            # Render text "Multiplication game"
            text1 = title_font.render("Multiplication game", True, (0, 0, 0))
            text1_rect = text1.get_rect(center=(self.width // 2, 75))
            self.window.blit(text1, text1_rect)

            # Render text "Izvēleties kurš sāk"
            text2 = text_font.render("Izvēleties kurš sāk", True, (0, 0, 0))
            text2_rect = text2.get_rect(center=(self.width // 2, 125))
            self.window.blit(text2, text2_rect)

            # Draw buttons
            pygame.draw.rect(self.window, (217, 217, 217), button1_rect)
            pygame.draw.rect(self.window, (217, 217, 217), button2_rect)

            # Render button text
            button1_text = button_font.render("Cilvēks", True, (0, 0, 0))
            button2_text = button_font.render("Dators", True, (0, 0, 0))

            # Center text on buttons
            button1_text_rect = button1_text.get_rect(center=button1_rect.center)
            button2_text_rect = button2_text.get_rect(center=button2_rect.center)

            # Draw text on buttons
            self.window.blit(button1_text, button1_text_rect)
            self.window.blit(button2_text, button2_text_rect)

            pygame.display.flip()  # Update the display

        pygame.quit()

# Example usage:
if __name__ == "__main__":
    game = GameWindow()
    result = game.welcome_screen()
    
    
    if result == "human":
        print("I am a human")
    else:
        print("I am a computer")
