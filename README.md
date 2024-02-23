# Multiplication Game

This is a simple text-based game where the player chooses a number and then multiplies it by either 2 or 3. The game continues until a player reaches a total score of 1000 or more. Players take turns multiplying the number and adding it to their score. The player with the highest score at the end wins.

## How to Play

1. Run the script `multiplication_game.py`.
2. Follow the prompts to input a number between 5 and 15.
3. Choose whether to multiply your number by 2 or 3.
4. Repeat steps 2 and 3 until a player reaches a score of 1000 or more.
5. The game will display the final scores and declare the winner.

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

Created by Artis Čevers