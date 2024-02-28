# Multiplication Game

This is a simple text-based game where the player chooses a number and then multiplies it by either 2 or 3. The game continues until a player reaches a total score of 1000 or more. Players take turns multiplying the number and adding it to their score. The player with the highest score at the end wins.

![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/94c61d1b-bba8-4967-879f-9948e6b52d45)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/2d7211d1-f52b-4a82-978f-67b0a8b9d5f9)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/562538ad-82e5-4019-9bc1-061ca4270f33)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/29361dc0-f307-49e0-9998-444843e17ef0)

## How to Play

1. Ensure you have Pygame installed. If not, you can install it using pip:
```pip install pygame```
2. Navigate to the new_game folder.
3. Run the script main.py using Python 3:
```python3 main.py```
Follow the prompts to input a number between 5 and 15.
4. Choose whether to multiply your number by 2 or 3.
5. Repeat steps 4 and 5 until a player reaches a score of 1000 or more.
6. The game will display the final scores and declare the winner.

## Classes

GameWindow - Handles all of the logic and rendering in the game

## Dependencies

- Python 3.x
- `pygame` module

## Example

```
# Inside the if __name__ == "__main__": block
if __name__ == "__main__":

    game = GameWindow()

    while game.running:
        game = GameWindow()
        result = game.welcome_screen()
        
        if result == "human":
            print("I am a human")
        else:
            print("I am a computer")

        result = game.choice_screen()
        print("You chose: ", result)

        # Capture the returned scores
        score1, score2 = game.game_screen(result)

        # Call winner_screen with the captured scores
        game.winner_screen(score1, score2)
```

## Contributions
Artis Čevers
