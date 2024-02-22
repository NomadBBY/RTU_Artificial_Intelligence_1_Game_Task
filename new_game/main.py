from os import system  # Importing system function from the os module
import time  # Importing time module


class Player:

    def __init__(self):
        self.human = 'human'  # Initializing human attribute with 'human'
        self.computer = 'computer'  # Initializing computer attribute with 'computer'

    def score(self):
        """
        Returns the scores of both computer and human players.
        """
        return self.computer, self.human


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
        self.player = Player()  # Creating an instance of the Player class
        self.score = {self.player.human: 0, self.player.computer: 0}  # Initializing score dictionary
        self.total = 0  # Initializing total score variable

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
        self.score[player] += 1  # Incrementing the player's score by 1
        self.total += choice  # Adding the choice to the total score
        return self.total  # Returning the updated total score

    def start_game(self):
        """
        Starts the game.
        """
        turn = self.player.human  # Start with human's turn
        total_score = 0  # Initializing total_score variable

        choice = self.user_choice()  # Getting user choice
        system("cls")  # Clearing the screen
        print("Number chosen by human:", choice)  # Printing the chosen number
        print()

        while self.game_state and total_score < 1000:

            if turn == 'human':
                print('Human\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))  # Asking for user input
                system("cls")  # Clearing the screen
                if multiply == 2:
                    choice *= 2  # Multiplying the choice by 2
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 2:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Human get's 1 point")  # Printing message
                        self.update_score(self.player.human, 1)  # Updating human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'computer'  # Switching to computer's turn
                    else:
                        print("Human loses 1 point")  # Printing message
                        self.update_score(self.player.human, -1)  # Updating human's score by -1
                        print("Human's current score:", self.score[self.player.human], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'computer'  # Switching to computer's turn

                elif multiply == 3:
                    choice *= 3  # Multiplying the choice by 3
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 3:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Human get's 1 point")  # Printing message
                        self.update_score(self.player.human, 1)  # Updating human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'computer'  # Switching to computer's turn
                    else:
                        print("Player loses 1 point")  # Printing message
                        self.update_score(self.player.human, -1)  # Updating human's score by -1
                        print("Human's current score:", self.score[self.player.human], '\n')  # Printing human's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'computer'  # Switching to computer's turn

                else:
                    print("Invalid choice. Please try again.")  # Printing message
                    continue  # Restart the loop if the choice is invalid

            elif turn == 'computer':
                print('Computer\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))  # Asking for user input
                system("cls")  # Clearing the screen
                if multiply == 2:
                    choice *= 2  # Multiplying the choice by 2
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 2:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Computer get's 1 point")  # Printing message
                        self.update_score(self.player.computer, 1)  # Updating computer's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'human'  # Switching to human's turn
                    else:
                        print("Computer loses 1 point")  # Printing message
                        self.update_score(self.player.human, -1)  # Updating human's score by -1
                        print("Computer's current score:", self.score[self.player.computer], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'human'  # Switching to human's turn

                elif multiply == 3:
                    choice *= 3  # Multiplying the choice by 3
                    total_score += choice  # Updating the total score
                    print("Total score after multiply by 3:", total_score, '\n')  # Printing total score
                    if choice % 2 == 0:
                        print("Computer get's 1 point")  # Printing message
                        self.update_score(self.player.computer, 1)  # Updating computer's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'human'  # Switching to human's turn
                    else:
                        print("Computer loses 1 point")  # Printing message
                        self.update_score(self.player.computer, -1)  # Updating computer's score by -1
                        print("Computer's current score:", self.score[self.player.computer], '\n')  # Printing computer's current score
                        time.sleep(5)  # Pausing execution for 5 seconds
                        system('cls')  # Clearing the screen
                        turn = 'human'  # Switching to human's turn

                else:
                    print("Invalid choice. Please try again.")  # Printing message
                    continue  # Restart the loop if the choice is invalid

        print("Human score: ", self.score[self.player.human])
        print("Computer score: ", self.score[self.player.computer])            
        time.sleep(5)
        system('cls')
            
        if self.score[self.player.human] < self.score[self.player.computer]:
            print("Human wins with a score of:", self.score[self.player.human])  # Printing message if human wins
        elif self.score[self.player.human] > self.score[self.player.computer]:
            print("Computer wins with a score of:", self.score[self.player.computer])  # Printing message if computer wins
        else:
            print("It's a tie!")  # Printing message if it's a tie
        
        print("Goodbye!")

# Main part of the code
if __name__ == "__main__":
    new_game = Game()  # Creating an instance of the Game class
    new_game.start_game()  # Starting the game
