# Multiplication Game

This is a simple text-based game where the player chooses a number and then multiplies it by either 2 or 3. The game continues until a player reaches a total score of 1000 or more. Players take turns multiplying the number and adding it to their score. The player with the highest score at the end wins.

![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/94c61d1b-bba8-4967-879f-9948e6b52d45)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/2d7211d1-f52b-4a82-978f-67b0a8b9d5f9)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/562538ad-82e5-4019-9bc1-061ca4270f33)
![image](https://github.com/NomadBBY/RTU_Artificial_Intelligence_1_Game_Task/assets/89861525/29361dc0-f307-49e0-9998-444843e17ef0)

## How to Play

1. Ensure you have Pygame installed. If not, you can install it using pip:
```pip install pygame```



## Classes

### Player

- Represents a player in the game.
- Contains attributes for the human player and the computer player.

### AiAlgorithm

- Placeholder for AI algorithm class (currently not implemented).

### Game

- Represents the game environment.
- Manages the flow of the game, including user input and score calculation.

## How to Run

Ensure you have Python installed on your machine. Run the script `multiplication_game.py` using your preferred Python interpreter.

## Dependencies

- Python 3.x
- `os` module
- `time` module

## Example

```python
from os import system
import time

# Main part of the code
if __name__ == "__main__":
    new_game = Game()  # Creating an instance of the Game class
    new_game.start_game()  # Starting the game
```

## Contributions
Artis Čevers
