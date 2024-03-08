import pygame
import random
import os

BACKGROUND_COLOR = 225, 217, 196
BUTTON_COLOR = 100, 100, 100

class Algorithm:
    '''
    Implementation of the MiniMax algorithm for the game
    '''

    def __init__(self) -> None:
        pass

    def minimax(self, number1, number2, score1, score2, turn, depth, maximizing_player):
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            # Evaluate the current state
            # The computer (maximizing player) wants a higher score than the human
            if number1 >= 1000:
                return score2 - score1, None  # Human wins (computer loses, lower score)
            elif number2 >= 1000:
                return score1 - score2, None  # Computer wins (higher score)
            else:
                # Compare the scores and return a value based on who has the higher score
                return score2 - score1, None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_possible_moves(number1, turn):
                new_number1 = self.make_move(number1, move)
                new_score1 = self.update_score(score1, new_number1)
                evaluation = self.minimax(new_number1, number2, new_score1, score2, 'computer', depth - 1, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_possible_moves(number2, turn):
                new_number2 = self.make_move(number2, move)
                new_score2 = self.update_score(score2, new_number2)
                evaluation = self.minimax(number1, new_number2, score1, new_score2, 'human', depth - 1, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
            return min_eval, best_move

    def get_possible_moves(self, number, turn):
        if turn == 'computer':
            possible_moves = []
            for i in range(2, 11):  # Consider multipliers from 2 to 10
                if (number * i) % 2 == 1:  # Include only moves that result in odd numbers
                    possible_moves.append(i)
            return possible_moves
        else:
            # For the human player, the possible moves can vary based on the number
            possible_moves = []
            for i in range(2, min(number, 6) + 1):  # Limit possible moves to 6
                possible_moves.append(i)
            return possible_moves

    def make_move(self, number, move):
        return number * move

    def update_score(self, score, number):
        if number % 2 == 0:
            return score - 1  # Subtract 1 point for even number
        else:
            return score + 1  # Add 1 point for odd number

class GameWindow:

    def __init__(self, width=600, height=350):
        pygame.font.init()  # Initialize the font module
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = True
        pygame.display.set_caption('Multiplication game')

    def reset_game(self):
        # Reset the running variable
        self.running = True
        pygame.init()  # Initialize Pygame again

    def welcome_screen(self):

        button1_rect = pygame.Rect(120, 200, 120, 35)  # Adjusted button 1 position
        button2_rect = pygame.Rect(360, 200, 120, 35)  # Adjusted button 2 position

        button_font = pygame.font.Font(None, 24) #Font for the buttons
        title_font = pygame.font.Font(None, 50) #Font for the title text
        text_font = pygame.font.Font(None, 36) #Font for the under text
                        
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

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if button 1 is clicked
                        if button1_rect.collidepoint(event.pos):
                            #print("Button 1 clicked!")
                            return 'human'
                        # Check if button 2 is clicked
                        elif button2_rect.collidepoint(event.pos):
                            #print("Button 2 clicked!")
                            return 'computer'

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

        while self.running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running = False
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                       # Check if any button is clicked
                       for i, rect in enumerate(button_rects):
                           if rect.collidepoint(event.pos):
                               return button_values[i]

        pygame.quit()

    def game_screen(self, number, initial_player):

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
        number1 = number  # Initial number for window 1
        number1_text = number_font.render(str(number1), True, (0, 0, 0))
        number1_text_rect = number1_text.get_rect(center=window1_rect.center)
        self.window.blit(number1_text, number1_text_rect)

        # Render the window under buttons with number 1
        window2_rect = pygame.Rect(360, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window2_rect)
        number2 = number  # Initial number for window 2
        number2_text = number_font.render(str(number2), True, (0, 0, 0))
        number2_text_rect = number2_text.get_rect(center=window2_rect.center)
        self.window.blit(number2_text, number2_text_rect)

        pygame.display.update()

        def render_player_one():
            # Update the numbers displayed in the windows
            number1_text = number_font.render(str(number1), True, (0, 0, 0))
            self.window.fill((200, 200, 200), rect=window1_rect)  # Clear previous number for window 1
            self.window.blit(number1_text, number1_text_rect)
            pygame.display.update()

        def render_player_two():
            # Update the numbers displayed in the windows
            number2_text = number_font.render(str(number2), True, (0, 0, 0))
            self.window.fill((200, 200, 200), rect=window2_rect)  # Clear previous number for window 2
            self.window.blit(number2_text, number2_text_rect)
            pygame.display.update()

        # Initialize scores
        self.turn = initial_player
        self.score1 = 0
        self.score2 = 0

        # Create an instance of the MiniMax algorithm
        algo = Algorithm()

        # Main loop to handle events
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break  # Exit the loop if running is set to False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn == 'human':
                        # Human's turn
                        # Check if the first two buttons are clicked
                        for i, rect in enumerate(button_rects[:2]):
                            if rect.collidepoint(event.pos):
                                print(f"Button {i + 1} clicked!")
                                if i == 0:
                                    number1 *= 2  # Double the number for window 1
                                elif i == 1:
                                    number1 *= 3  # Triple the number for window 1

                                # Update the score based on the parity of the number
                                if number1 % 2 == 0:
                                    print("Number is even!")
                                    self.score1 += 1
                                else:
                                    print("Number is odd!")
                                    self.score1 -= 1

                                # Update the numbers displayed in the windows
                                render_player_one()

                                # Switch to computer's turn
                                self.turn = 'computer'
                                break

                if self.turn == 'computer':
                    print("Computer is thinking...")
                    pygame.display.update()
                    pygame.time.delay(1000)  # Add a delay of 1000 milliseconds (1 second)

                    # Get the best move for the computer using MiniMax algorithm
                    best_eval, best_move = algo.minimax(number1, number2, self.score1, self.score2, 'computer', 3, False)

                    if best_move is not None:
                        # Make the best move
                        number2 *= best_move

                        # Update the score based on the parity of the number
                        if number2 % 2 == 0:
                            print("Number is even!")
                            self.score2 += 1
                        else:
                            print("Number is odd!")
                            self.score2 -= 1

                        # Update the numbers displayed in the windows
                        render_player_two()

                    # Switch to human's turn
                    self.turn = 'human'

                # Check if either score is >= 1000
                if number1 >= 1000 or number2 >= 1000:
                    print("Goodbye")
                    # Reset the game
                    self.running = False
                    return self.score1, self.score2

    def winner_screen(self, human_score, pc_score):
        """
        Display a winner screen with human and PC scores and a continue button.

        Args:
            human_score (int): The score of the human player.
            pc_score (int): The score of the PC player.
        """
        # Define the text based on the comparison of scores
        if score1 < score2:
            text = "Spēlētājs uzvarēja!"  # Player 1 wins
        elif score1 > score2:
            text = "Dators uzvarēja!"  # Player 2 wins
        else:
            text = "Neizšķirts!"  # One player wins

        # Define headline position
        text_x = 300
        text_y = 85

        # Define text positions
        text1_x = 150
        text1_y = 160

        text2_x = 450
        text2_y = 160

        # Define window positions
        window1_x = 100
        window1_y = 200

        window2_x = 420
        window2_y = 200

        # Define button position and size
        button_x = 200
        button_y = 280
        button_width = 200
        button_height = 50

        self.window.fill(BACKGROUND_COLOR)
        headline_text = pygame.font.Font(None, 45)
        text_surface = headline_text.render(text, True, (0, 0, 0))

        text_font = pygame.font.Font(None, 35)
        # Set the text position
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        self.window.blit(text_surface, text_rect)

        # Render "Human Result" text
        text_surface = text_font.render("Human Result", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(text1_x, text1_y))
        self.window.blit(text_surface, text_rect)

        # Render "PC Result" text
        text_surface = text_font.render("PC Result", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(text2_x, text2_y))
        self.window.blit(text_surface, text_rect)

        # Render windows with scores
        number_font = pygame.font.Font(None, 24)

        # Render window 1 with human score
        window1_rect = pygame.Rect(window1_x, window1_y, 90, 35)
        pygame.draw.rect(self.window, (255, 255, 255), window1_rect)  # Draw white rectangle as background
        human_score_surface = number_font.render(str(human_score), True, (0, 0, 0))
        number_rect = human_score_surface.get_rect(center=window1_rect.center)
        self.window.blit(human_score_surface, number_rect.topleft)

        # Render window 2 with PC score
        window2_rect = pygame.Rect(window2_x, window2_y, 90, 35)
        pygame.draw.rect(self.window, (255, 255, 255), window2_rect)  # Draw white rectangle as background
        pc_score_surface = number_font.render(str(pc_score), True, (0, 0, 0))
        number_rect = pc_score_surface.get_rect(center=window2_rect.center)
        self.window.blit(pc_score_surface, number_rect.topleft)

        # Render button
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(self.window, (BUTTON_COLOR), button_rect)  # Green button
        button_text = text_font.render("Turpināt?", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)

        pygame.display.flip()  # Update the display

        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        # Restart the game
                        self.reset_game()
                        waiting = False

        pygame.quit()


# Inside the __name__ == "__main__" block
        
if __name__ == "__main__":
    game = GameWindow()

    while game.running:
        game = GameWindow()
        initial_player = game.welcome_screen()  # Get the initial player's turn
        result = game.choice_screen()
        print("You chose: ", result)
        os.system('cls')
        score1, score2 = game.game_screen(result, initial_player)  # Pass the initial player's turn to game_screen
        game.winner_screen(score1, score2)