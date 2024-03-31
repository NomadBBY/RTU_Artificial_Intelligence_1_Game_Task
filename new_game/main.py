import pygame
import os

BACKGROUND_COLOR = 225, 217, 196
BUTTON_COLOR = 100, 100, 100

class Algorithm:
    '''
    Implementation of the MiniMax algorithm for the number manipulation game.
    Each turn, a player can multiply the current number by 2 or 3.
    Points are scored based on the resulting number's parity.
    The game ends when a number >= 1000 is reached.
    '''

    def __init__(self, start_number):
        self.current_number = start_number
        self.score = 0  # Assuming a single player score tracking for simplicity

    def is_game_over(self):
        # Check if the current game state is a terminal state.
        return self.current_number >= 1000

    def evaluate_heuristic(self):
        # Heuristic evaluation of the current game state.
        if self.current_number >= 1000:
            return float('inf') if self.score < 0 else float('-inf')
        return self.score

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.is_game_over():
            return self.evaluate_heuristic()
    
        if maximizing_player:
            max_eval = float('-inf')
            original_number = self.current_number
            original_score = self.score
            for multiplier in [2, 3]:
                self.current_number = multiplier
                self.score += -1 if self.current_number % 2 == 0 else 1  # Decrement score for even numbers, increment for odd numbers
                eval = self.minimax(depth - 1, False)
                max_eval = max(max_eval, eval)
                self.current_number = original_number
                self.score = original_score
            return max_eval
        
        else:
            min_eval = float('inf')
            original_number = self.current_number
            original_score = self.score
            for multiplier in [2, 3]:
                self.current_number= multiplier
                self.score += -1 if self.current_number % 2 == 0 else 1  # Decrement score for even numbers, increment for odd numbers
                eval = self.minimax(depth - 1, True)
                min_eval = min(min_eval, eval)
                self.current_number = original_number
                self.score = original_score
            return min_eval

    def alphabeta(self, depth, alpha, beta, maximizing_player):
        # Similar implementation to minimax, with alpha-beta pruning added.
        if depth == 0 or self.is_game_over():
            return self.evaluate_heuristic()

        if maximizing_player:
            max_eval = float('-inf')
            for multiplier in [2, 3]:
                original_number = self.current_number
                self.current_number *= multiplier
                self.score += 1 if self.current_number % 2 == 0 else -1
                eval = self.alphabeta(depth - 1, alpha, beta, False)
                self.current_number = original_number
                self.score -= 1 if self.current_number % 2 == 0 else -1
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for multiplier in [2, 3]:
                original_number = self.current_number
                self.current_number *= multiplier
                self.score += 1 if self.current_number % 2 == 0 else -1
                eval = self.alphabeta(depth - 1, alpha, beta, True)
                self.current_number = original_number
                self.score -= 1 if self.current_number % 2 == 0 else -1
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    # Removed get_possible_moves and make_move as they are not directly relevant for the described game logic.

    # No need for update_score method since score updates are directly handled within minimax/alphabeta methods.

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
                    best_move = None
                    best_eval = float('-inf')

                    # Iterate over possible multipliers (2 and 3)
                    for multiplier in [2, 3]:
                        # Make a hypothetical move for the computer
                        new_number = number2 * multiplier

                        # Update the score based on the parity of the number
                        new_score = self.score2 + 1 if new_number % 2 == 0 else self.score2 - 1

                        # Evaluate the move using the minimax algorithm with a higher depth
                        eval_score = Algorithm(new_number).minimax(10, False)  # Increased depth to 10

                        # Check if this move yields a better evaluation score
                        if eval_score > best_eval:
                            best_eval = eval_score
                            best_move = multiplier

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

                    # Check if either score is >= 1000
                    if number1 >= 1000 or number2 >= 1000:
                        print("Goodbye")
                        # Reset the game
                        self.running = False
                        return self.score1, self.score2

                    # Switch to human's turn
                    self.turn = 'human'

                # Check if either score is >= 1000
                if number1 >= 1000 or number2 >= 1000:
                    print("Goodbye")
                    # Reset the game
                    self.running = False
                    return self.score1, self.score2

    pygame.quit()

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
