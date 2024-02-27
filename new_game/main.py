from os import system  # Importing system function from the os module
import time  # Importing time module
import pygame

BACKGROUND_COLOR = 225, 217, 196
BUTTON_COLOR = 100, 100, 100

class GameWindow:

    def __init__(self, width=600, height=350):
        self.game = pygame.init()
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
                                pygame.quit()
                                return 'human'
                            # Check if button 2 is clicked
                            elif button2_rect.collidepoint(event.pos):
                                #print("Button 2 clicked!")
                                pygame.quit()
                                return 'computer'
        
class Player:
    def __init__(self, choice):

        self.choice = choice  # Initialize the player's choice

    def score(self):
        """
        Returns the player's choice.
        """
        return self.choice

class AiAlgorithm:
    """
    Placeholder for AI algorithm class.
    """
    pass


class Game:
    """
    Class representing the game.
    """

    def __init__(self):
        """
        Initializes the game with default settings.
        """
        self.game_state = True  # Initializing game_state attribute as True
        game_window = GameWindow()  # Create an instance of the GameWindow
        choice = game_window.welcome_screen()  # Obtain player's choice from welcome screen
        self.player = Player(choice)  # Creating an instance of the Player class with obtained choice
        print(self.player.choice)

        # Initialize score dictionary based on player's choice
        if choice == 'human':
            self.score = {self.player.choice: 0, 'computer': 0}
        else:
            self.score = {'human': 0, self.player.choice: 0}

    def user_choice(self):
        """
        Prompts the user to input a number between 5 and 15.
        """
        while self.game_state:
            choice = int(input("Please enter a number between 5 and 15: "))  # Asking for user input
            if 5 <= choice <= 15:
                return choice  # Returning the choice if it's within the specified range
            else:
                print("Try again")  # Prompting the user to try again if the choice is invalid

    def update_score(self, player, choice):
        """
        Updates the score based on the player and their choice.
        """
        if player == 'human':
            self.score[self.player.choice] += choice
        elif player == 'computer':
            self.score['computer'] += choice
        return self.score

    def start_game(self):
        """
        Starts the game.
        """
        turn = self.player.choice  # Start with human's turn
        total_score = 0  # Initializing total_score variable

        choice = self.user_choice()  # Getting user choice
        print("Number chosen by human:", choice)  # Printing the chosen number
        print()

        while self.game_state and total_score < 1000:

            if turn == 'human':
                print('Human\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))  # Asking for user input
                if multiply == 2:
                    choice *= 2  # Multiplying the choice by 2
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 2:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Human gets 1 point")  # Printing message
                        self.update_score(self.player.choice, 1)  # Updating human's score by 1
                        print("Human's current score:", self.score[self.player.choice], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'computer'  # Switching to computer's turn
                    else:
                        print("Human loses 1 point")  # Printing message
                        self.update_score(self.player.choice, -1)  # Updating human's score by -1
                        print("Human's current score:", self.score[self.player.choice], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'computer'  # Switching to computer's turn

                elif multiply == 3:
                    choice *= 3  # Multiplying the choice by 3
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 3:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Human gets 1 point")  # Printing message
                        self.update_score(self.player.choice, 1)  # Updating human's score by 1
                        print("Human's current score:", self.score[self.player.choice], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'computer'  # Switching to computer's turn
                    else:
                        print("Human loses 1 point")  # Printing message
                        self.update_score(self.player.choice, -1)  # Updating human's score by -1
                        print("Human's current score:", self.score[self.player.choice], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'computer'  # Switching to computer's turn

                else:
                    print("Invalid choice. Please try again.")  # Printing message
                    continue  # Restart the loop if the choice is invalid

            elif turn == 'computer':
                print('Computer\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))  # Asking for user input
                if multiply == 2:
                    choice *= 2  # Multiplying the choice by 2
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 2:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Computer gets 1 point")  # Printing message
                        self.update_score('computer', 1)  # Updating computer's score by 1
                        print("Computer's current score:", self.score['computer'], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'human'  # Switching to human's turn
                    else:
                        print("Computer loses 1 point")  # Printing message
                        self.update_score('computer', -1)  # Updating computer's score by -1
                        print("Computer's current score:", self.score['computer'], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'human'  # Switching to human's turn

                elif multiply == 3:
                    choice *= 3  # Multiplying the choice by 3
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 3:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Computer gets 1 point")  # Printing message
                        self.update_score('computer', 1)  # Updating computer's score by 1
                        print("Computer's current score:", self.score['computer'], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'human'  # Switching to human's turn
                    else:
                        print("Computer loses 1 point")  # Printing message
                        self.update_score('computer', -1)  # Updating computer's score by -1
                        print("Computer's current score:", self.score['computer'], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        turn = 'human'  # Switching to human's turn

                else:
                    print("Invalid choice. Please try again.")  # Printing message
                    continue  # Restart the loop if the choice is invalid

        print("Human score: ", self.score[self.player.choice])
        print("Computer score: ", self.score['computer'])            
        time.sleep(5)
            
        if self.score[self.player.choice] < self.score['computer']:
            print("Computer wins with a score of:", self.score['computer'])  # Printing message if computer wins
        elif self.score[self.player.choice] > self.score['computer']:
            print("Human wins with a score of:", self.score[self.player.choice])  # Printing message if human wins
        else:
            print("It's a tie!")  # Printing message if it's a tie
        
        print("Goodbye!")

# Main part of the code
if __name__ == "__main__":

    new_game = Game()
    new_game.start_game()
