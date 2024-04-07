# Multiplication Game

This is a simple text-based game where the player chooses a number and then multiplies it by either 2 or 3. The game continues until a player reaches a total score of 1000 or more. Players take turns multiplying the number and adding it to their score. The player with the highest score at the end wins.

![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/797eb738-c0b1-47b3-94bb-3174583ff058)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/f01f667f-c29f-4ec4-b588-d3b784e509d6)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/530dd3ae-0288-415b-91fc-caf9efae8786)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/766d60fb-dafa-4bc2-925d-da2cf661198e)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/8b9fb6b8-0cb6-4606-b7f5-a1bae1cadf79)

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
