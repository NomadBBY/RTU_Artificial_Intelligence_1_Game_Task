import pygame

BACKGROUND_COLOR = 225, 217, 196  # Define the background color of the game window
BUTTON_COLOR = 100, 100, 100  # Define the color of the buttons

class Algorithm:
    
    def __init__(self):
        pass

    def make_move(self, number, move):
        """This method takes a number and a move, and returns the result of multiplying them."""
        return number * move

    def update_score(self, score, number, score1, score2):
        """
        This method updates the score based on the current score and the number.
        If the number is even, it adds 1 point to the score; otherwise, it subtracts 1 point.
        """
        if number % 2 == 0:
            return score + 1  # Add 1 point for even number
        else:
            return score - 1  # Subtract 1 point for odd number

        #Labojums
        # Additional logic
        if score1 - score2 >= 1:
            return 0
        elif score1 - score2 == 0:
            return 1
        else:
            return score

    def get_possible_moves(self, number, turn):
        """
        This method returns a list of possible moves based on the current number and turn.
        By default, it returns [2, 3] for the computer's turn and a range from 2 to the minimum of the number and 6 for the human's turn.
        """
        if turn == 'computer':
            return [2, 3]
        else:
            return list(range(2, min(number, 6) + 1))

class MinimaxAlgorithm(Algorithm):
    
    def minimax(self, number1, number2, score1, score2, turn, depth, maximizing_player):
        """
        This method implements the Minimax algorithm to determine the best move for the computer player.
        It recursively explores all possible moves up to a certain depth and returns the best evaluation and move.
        """
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
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

class AlphaBetaAlgorithm(Algorithm):
    
    def minimax(self, number1, number2, score1, score2, turn, depth, alpha, beta, maximizing_player):
        """
        This method implements the Alpha-Beta Pruning algorithm to determine the best move for the computer player.
        It recursively explores all possible moves up to a certain depth and returns the best evaluation and move.
        """
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            return score2 - score1, None
        
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_possible_moves(number1, turn):
                new_number1 = self.make_move(number1, move)
                new_score1 = self.update_score(score1, new_number1)
                evaluation = self.minimax(new_number1, number2, new_score1, score2, 'computer', depth - 1, alpha, beta, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_possible_moves(number2, turn):
                new_number2 = self.make_move(number2, move)
                new_score2 = self.update_score(score2, new_number2)
                evaluation = self.minimax(number1, new_number2, score1, new_score2, 'human', depth - 1, alpha, beta, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move
        
class GameWindow:

    def __init__(self, width=600, height=350):
        pygame.init()  # Initialize Pygame
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
        """
        This method displays the welcome screen where the player can choose to start the game as a human or a computer.
        It handles mouse clicks on the buttons and returns the choice made by the player.
        """
        button1_rect = pygame.Rect(120, 200, 120, 35)  # Adjusted button 1 position
        button2_rect = pygame.Rect(360, 200, 120, 35)  # Adjusted button 2 position

        button_font = pygame.font.Font(None, 24) # Font for the buttons
        title_font = pygame.font.Font(None, 50) # Font for the title text
        text_font = pygame.font.Font(None, 36) # Font for the under text
                        
        self.window.fill((BACKGROUND_COLOR))  # Fill window with color
        # Render text "Multiplication game"
        text1 = title_font.render("Multiplication game", True, (0, 0, 0))
        text1_rect = text1.get_rect(center=(self.width // 2, 75))
        self.window.blit(text1, text1_rect)
        # Render text "Choose who starts"
        text2 = text_font.render("Choose who starts", True, (0, 0, 0))
        text2_rect = text2.get_rect(center=(self.width // 2, 125))
        self.window.blit(text2, text2_rect)
        # Draw buttons
        pygame.draw.rect(self.window, (BUTTON_COLOR), button1_rect)
        pygame.draw.rect(self.window, (BUTTON_COLOR), button2_rect)
        # Render button text
        button1_text = button_font.render("Human", True, (0, 0, 0))
        button2_text = button_font.render("Computer", True, (0, 0, 0))
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
                            return 'human'
                        # Check if button 2 is clicked
                        elif button2_rect.collidepoint(event.pos):
                            return 'computer'

        pygame.quit()

    def choice_screen(self):
        """
        This method displays the screen where the player can choose the starting number for the game.
        It handles mouse clicks on the buttons and returns the selected number.
        """
        title_font = pygame.font.Font(None, 50) # Font for the title text

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
        # Render text "Choose starting number"
        text1 = title_font.render("Choose starting number", True, (0, 0, 0))
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
    
    def algorithm_choice_screen(self):
        """
        Displays the screen where the player can choose between Minimax and Alpha-Beta algorithms.
        It handles mouse clicks on the buttons and returns the selected algorithm.
        """
        self.window.fill(BACKGROUND_COLOR)  # Fill the background
        title_font = pygame.font.Font(None, 50)  # Font for the title
        button_font = pygame.font.Font(None, 36)  # Font for the button text

        # Create and render the title
        title_surface = title_font.render('Choose Algorithm', True, (0, 0, 0))  # Black color
        title_rect = title_surface.get_rect(center=(self.width // 2, 50))
        self.window.blit(title_surface, title_rect)

        # Create buttons for choosing the algorithm
        minimax_button = pygame.Rect((self.width - 150) // 4, 150, 150, 50)
        alpha_beta_button = pygame.Rect((self.width - 150) * 3 // 4, 150, 150, 50)

        # Draw buttons
        pygame.draw.rect(self.window, BUTTON_COLOR, minimax_button)
        pygame.draw.rect(self.window, BUTTON_COLOR, alpha_beta_button)

        # Render text on buttons
        minimax_text = button_font.render('Minimax', True, (0, 0, 0))  # Black color
        alpha_beta_text = button_font.render('Alpha-Beta', True, (0, 0, 0))  # Black color
        self.window.blit(minimax_text, (minimax_button.x + 20, minimax_button.y + 10))
        self.window.blit(alpha_beta_text, (alpha_beta_button.x + 10, alpha_beta_button.y + 10))

        pygame.display.flip()  # Update the screen

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if minimax_button.collidepoint(event.pos):
                        return "minimax"
                    elif alpha_beta_button.collidepoint(event.pos):
                        return "alpha-beta"

    def game_screen(self, number, initial_player, algo):
        """
        Displays the main game screen where players can interact with the game.
        It handles player's moves and updates the game accordingly.

        Args:
            number (int): The initial number for the game.
            initial_player (str): The starting player, either 'human' or 'computer'.
            algo (Algorithm): The algorithm instance to use for the computer's moves.
        """
        self.turn = initial_player
        self.score1 = 0
        self.score2 = 0
    
        both_numbers = number  # Assigning the initial number to both_numbers
    
        text_font = pygame.font.Font(None, 45)  # Font for the text
        number_font = pygame.font.Font(None, 30)  # Font for the number
        score_font = pygame.font.Font(None, 24)  # Font for the score
    
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
        number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
        number1_text_rect = number1_text.get_rect(center=window1_rect.center)
        self.window.blit(number1_text, number1_text_rect)
    
        # Render the window under buttons with number 1
        window2_rect = pygame.Rect(360, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window2_rect)
        number2_text = number_font.render(str(both_numbers), True, (0, 0, 0))
        number2_text_rect = number2_text.get_rect(center=window2_rect.center)
        self.window.blit(number2_text, number2_text_rect)
    
        pygame.display.update()    

        def render_both_players():

            # Update the numbers displayed in the windows
            number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
            self.window.fill((200, 200, 200), rect=window1_rect)  # Clear previous number for window 1
            self.window.blit(number1_text, number1_text_rect)

            pygame.display.update()
    
        # Initialize scores
        self.turn = initial_player
        self.score1 = 0
        self.score2 = 0
    
        # Main loop to handle events
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.turn == 'human':
                    # Human's turn
                    # Check if the first two buttons are clicked
                    for i, rect in enumerate(button_rects[:2]):
                        if rect.collidepoint(event.pos):
                            print(f"Button {i + 1} clicked!")
                            if i == 0:
                                both_numbers *= 2  # Double the number for window 1
                            elif i == 1:
                                both_numbers *= 3  # Triple the number for window 1
    
                            # Update the score based on the parity of the number
                            if both_numbers % 2 == 0:
                                print("Number is even!")
                                self.score1 += 1
                            else:
                                print("Number is odd!")
                                self.score1 -= 1
    
                            # Update the numbers displayed in the windows
                            render_both_players()
    
                            # Switch to computer's turn
                            self.turn = 'computer'
                            break
                        
                if self.turn == 'computer':
                    print("Computer is thinking...")
                    pygame.display.update()
                    pygame.time.delay(1000)  # Add a delay of 1000 milliseconds (1 second)
    
                    # Get the best move for the computer using MiniMax algorithm
                    if isinstance(algo, MinimaxAlgorithm):
                        best_eval, best_move = algo.minimax(both_numbers, both_numbers, self.score1, self.score2, 'computer', 3, False)
                    elif isinstance(algo, AlphaBetaAlgorithm):
                        best_eval, best_move = algo.minimax(both_numbers, both_numbers, self.score1, self.score2, 'computer', 3, float('-inf'), float('inf'), False)
    
                    if best_move:
                        both_numbers = algo.make_move(both_numbers, best_move)
                        self.score2 = algo.update_score(self.score2, both_numbers)

                    # Update the numbers displayed in the windows
                    render_both_players()

                    # Switch to human's turn
                    self.turn = 'human'
    
                # Check if either score is >= 1000
                if both_numbers >= 1000:
                    print("Goodbye")
                    # Reset the game
                    running = False
                    return self.score1, self.score2
    
            # Clear the screen
            self.window.fill(BACKGROUND_COLOR)
    
            # Render text "Spēlētājs"
            text1 = text_font.render("Spēlētājs", True, (0, 0, 0))
            text1_rect = text1.get_rect(topleft=(text1_x, text1_y))
            self.window.blit(text1, text1_rect)
    
            # Render text "Dators"
            text2 = text_font.render("Dators", True, (0, 0, 0))
            text2_rect = text2.get_rect(topleft=(text2_x, text2_y))
            self.window.blit(text2, text2_rect)
    
            # Render buttons
            button_rect = pygame.Rect(button1_x, button1_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x2", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button2_x, button2_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x3", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button3_x, button3_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x2", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button4_x, button4_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x3", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            # Render the windows    
            window1_rect = pygame.Rect(200, 200, 250, 50)
            pygame.draw.rect(self.window, (200, 200, 200), window1_rect)
            number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
            number1_text_rect = number1_text.get_rect(center=window1_rect.center)
            self.window.blit(number1_text, number1_text_rect)
    
            # Render scores
            score_text = score_font.render(f"Player Score: {self.score1}   Computer Score: {self.score2}", True, (0, 0, 0))
            score_text_rect = score_text.get_rect(center=(self.window.get_width() // 2, 300))
            self.window.blit(score_text, score_text_rect)
    
            pygame.display.update()


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

if __name__ == "__main__":
    # Initialize the game window
    game = GameWindow()

    # Main game loop
    while game.running:

        # Create a new instance of the game window
        game = GameWindow()

        # Display the welcome screen and get the initial player choice
        initial_player = game.welcome_screen()

        # Get the starting number chosen by the player
        start_number = game.choice_screen()

        # Prompt the player to choose the algorithm
        algorithm_choice = game.algorithm_choice_screen()

        # Initialize the algorithm based on the player's choice
        if algorithm_choice == "minimax":
            algo = MinimaxAlgorithm()
        else:
            algo = AlphaBetaAlgorithm()

        # Start the game screen and play the game using the chosen algorithm
        score1, score2 = game.game_screen(start_number, initial_player, algo)

        # Display the winner screen with the result of the game
        game.winner_screen(score1, score2)
