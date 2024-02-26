import pygame

BACKGROUND_COLOR = 225, 217, 196
BUTTON_COLOR = 100, 100, 100

class GameWindow:

    def __init__(self, width=600, height=350):
        self.game = pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Multiplication game')

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

            self.window.fill((BACKGROUND_COLOR))  # Fill window with color

            # Render text "Multiplication game"
            text1 = title_font.render("Multiplication game", True, (0, 0, 0))
            text1_rect = text1.get_rect(center=(self.width // 2, 75))
            self.window.blit(text1, text1_rect)

            # Render text "Izvēleties kurš sāk"
            text2 = text_font.render("Izvēleties kurš sāk", True, (0, 0, 0))
            text2_rect = text2.get_rect(center=(self.width // 2, 125))
            self.window.blit(text2, text2_rect)

            # Draw buttons
            pygame.draw.rect(self.window, (BUTTON_COLOR), button1_rect)
            pygame.draw.rect(self.window, (BUTTON_COLOR), button2_rect)

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

    def choice_screen(self):

        title_font = pygame.font.Font(None, 50) #Font for the title text

        # Define button parameters
        button_width = 35
        button_height = 35
        button_margin = 10  # Increased space between buttons
        button_color = BUTTON_COLOR
        button_font = pygame.font.Font(None, 24)

        # Define button values
        button_values = list(range(5, 16))

        # Calculate total width of all buttons
        total_button_width = len(button_values) * button_width + (len(button_values) - 1) * button_margin

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if any button is clicked
                        for i, rect in enumerate(button_rects):
                            if rect.collidepoint(event.pos):
                                return button_values[i]

            # Clear the screen
            self.window.fill((BACKGROUND_COLOR))

            # Render text "Multiplication game"
            text1 = title_font.render("Izvēlies sākuma skaitli", True, (0, 0, 0))
            text1_rect = text1.get_rect(center=(self.width // 2, 80))
            self.window.blit(text1, text1_rect)

            # Calculate starting x-coordinate for the first button to center them
            start_x = (self.width - total_button_width) // 2

            # Render buttons
            button_rects = []  # List to store button rects for collision detection
            
            for i, value in enumerate(button_values):
                button_x = start_x + i * (button_width + button_margin)
                button_y = 180  # Adjusted button y-coordinate to position the buttons lower
                button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                pygame.draw.rect(self.window, button_color, button_rect)
                button_rects.append(button_rect)

                # Render button text
                button_text = button_font.render(str(value), True, (0, 0, 0))
                button_text_rect = button_text.get_rect(center=button_rect.center)
                self.window.blit(button_text, button_text_rect)

            # Update the display
            pygame.display.update()

        pygame.quit()

    def game_screen(self):

        text_font = pygame.font.Font(None, 45)  # Font for the text
        number_font = pygame.font.Font(None, 30)  # Font for the number

        # Define button parameters
        button_width = 60
        button_height = 35
        button_color = BUTTON_COLOR
        button_font = pygame.font.Font(None, 24)

        # Clear the screen
        self.window.fill(BACKGROUND_COLOR)

        # Manual input for text positions
        text1_x = 100
        text1_y = 100

        text2_x = 400
        text2_y = 100

        # Render text "Spēlētājs"
        text1 = text_font.render("Spēlētājs", True, (0, 0, 0))
        text1_rect = text1.get_rect(topleft=(text1_x, text1_y))
        self.window.blit(text1, text1_rect)

        # Render text "Dators"
        text2 = text_font.render("Dators", True, (0, 0, 0))
        text2_rect = text2.get_rect(topleft=(text2_x, text2_y))
        self.window.blit(text2, text2_rect)

        button1_x = 80
        button1_y = 150

        button2_x = 180
        button2_y = 150

        button3_x = 360
        button3_y = 150

        button4_x = 460
        button4_y = 150

        # Render buttons
        button_rects = []  # List to store button rects for collision detection

        button_rect = pygame.Rect(button1_x, button1_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x2", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)

        button_rect = pygame.Rect(button2_x, button2_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x3", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)

        button_rect = pygame.Rect(button3_x, button3_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x2", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)

        button_rect = pygame.Rect(button4_x, button4_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x3", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)

        # Render the window under buttons with number 1
        window1_rect = pygame.Rect(80, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window1_rect)
        number1 = 1  # Initial number for window 1
        number1_text = number_font.render(str(number1), True, (0, 0, 0))
        number1_text_rect = number1_text.get_rect(center=window1_rect.center)
        self.window.blit(number1_text, number1_text_rect)

        # Render the window under buttons with number 1
        window2_rect = pygame.Rect(360, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window2_rect)
        number2 = 1  # Initial number for window 2
        number2_text = number_font.render(str(number2), True, (0, 0, 0))
        number2_text_rect = number2_text.get_rect(center=window2_rect.center)
        self.window.blit(number2_text, number2_text_rect)

        pygame.display.update()

        # Main loop to handle events
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if any button is clicked
                        for i, rect in enumerate(button_rects):
                            if rect.collidepoint(event.pos):
                                if i == 0:
                                    print(f"Button {i + 1} clicked!")
                                    number1 *= 2  # Double the number for window 1
                                elif i == 1:
                                    print(f"Button {i + 1} clicked!")
                                    number1 *= 3  # Triple the number for window 1
                                elif i == 2:
                                    print(f"Button {i + 1} clicked!")
                                    number2 *= 2  # Double the number for window 2
                                elif i == 3:
                                    print(f"Button {i + 1} clicked!")
                                    number2 *= 3  # Triple the number for window 2

                                # Update the numbers displayed in the windows
                                number1_text = number_font.render(str(number1), True, (0, 0, 0))
                                number2_text = number_font.render(str(number2), True, (0, 0, 0))

                                self.window.fill((200, 200, 200), rect=window1_rect)  # Clear previous number for window 1
                                self.window.blit(number1_text, number1_text_rect)

                                self.window.fill((200, 200, 200), rect=window2_rect)  # Clear previous number for window 2
                                self.window.blit(number2_text, number2_text_rect)
                                
                                pygame.display.update()
                                # Check if either number is >= 1000
                                if number1 >= 1000 or number2 >= 1000:
                                    print("Goodbye")
                                    running = False
                                    break  # Exit the loop

        pygame.quit()


# Exmmple usage:
if __name__ == "__main__":
    game = GameWindow()

    # result = game.welcome_screen()
    
    
    # if result == "human":
    #     print("I am a human")
    # else:
    #     print("I am a computer")

    # # Call choice_screen method to display the choice screen
    # result = game.choice_screen()
    # print("You chose: ", result)

    game.game_screen()