from os import system
import time

class Player:

    def __init__(self):
        self.human = 'human'
        self.computer = 'computer'

    def score(self):
        return self.computer, self.human

class Game:
    
    def __init__(self):
        self.game_state = True
        self.player = Player()
        self.score = {self.player.human: 0, self.player.computer: 0}
        self.total = 0

    def user_choice(self):
        while self.game_state:
            choice = int(input("Please enter a number between 5 and 15: "))
            if 5 <= choice <= 15:
                return choice
            else:
                print("Try again")

    def update_score(self, player, choice):
        self.score[player] += 1
        self.total += choice
        return self.total

    def start_game(self):
        turn = self.player.human  # Start with human's turn
        total_score = 0

        choice = self.user_choice()
        system("cls")
        print("Number chosen by human:", choice)
        print()

        while self.game_state and total_score < 1000:

            if turn == 'human':
                print('Human\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))
                system("cls")
                if multiply == 2:
                    choice *= 2
                    total_score += choice
                    print("Total score after multiply by 2:", total_score, '\n')
                    if choice % 2 == 0:
                        print("Human get's 1 point")
                        self.update_score(self.player.human, 1)  # Update human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'computer'
                    else:
                        print("Human loses 1 point")
                        self.update_score(self.player.human, -1)  # Update human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'computer'

                elif multiply == 3:
                    choice *= 3
                    total_score += choice
                    print("Total score after multiply by 3:", total_score, '\n')
                    if choice % 2 == 0:
                        print("Human get's 1 point")
                        self.update_score(self.player.human, 1)  # Update human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'computer'    
                    else:
                        print("Player loses 1 point")
                        self.update_score(self.player.human, -1)  # Update human's score by 1
                        print("Human's current score:", self.score[self.player.human], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'computer'

                else:
                    print("Invalid choice. Please try again.")
                    continue  # Restart the loop if the choice is invalid
            
            elif turn == 'computer':
                print('Computer\'s turn\n')

                multiply = int(input("Would you like to multiply with 2 or 3? : "))
                system("cls")
                if multiply == 2:
                    choice *= 2
                    total_score += choice
                    print("Total score after multiply by 2:", total_score, '\n')
                    if choice % 2 == 0:
                        print("Computer get's 1 point")
                        self.update_score(self.player.computer, 1)  # Update human's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'human'
                    else:
                        print("Computer loses 1 point")
                        self.update_score(self.player.human, -1)  # Update human's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'human'

                elif multiply == 3:
                    choice *= 3
                    total_score += choice
                    print("Total score after multiply by 3:", total_score, '\n')
                    if choice % 2 == 0:
                        print("Computer get's 1 point")
                        self.update_score(self.player.computer, 1)  # Update human's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'human'    
                    else:
                        print("Computer loses 1 point")
                        self.update_score(self.player.computer, -1)  # Update human's score by 1
                        print("Computer's current score:", self.score[self.player.computer], '\n')
                        time.sleep(5)
                        system('cls')
                        turn = 'human'

                else:
                    print("Invalid choice. Please try again.")
                    continue  # Restart the loop if the choice is invalid
        
        if self.score[self.player.human] > self.score[self.player.computer]:
            print("Human wins with a score of:", self.score[self.player.human], "Goodbye!")
        elif self.score[self.player.human] < self.score[self.player.computer]:
            print("Computer wins with a score of:", self.score[self.player.computer], "Goodbye!")
        else:
            print("It's a tie!", "Goodbye!")

        
# Main part of the code
if __name__ == "__main__":
    new_game = Game()
    new_game.start_game()
