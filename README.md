# Bouncy Ball Game

This project is a simple Bouncy Ball game implemented using the Pygame library. The player controls a ball that can jump and move left or right, while avoiding obstacles and collecting points. The game keeps track of the player's score and saves it to a file upon collision or exiting the game.

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Gameplay](#gameplay)
- [Project Structure](#project-structure)
- [Running the Game](#running-the-game)
- [File Structure](#file-structure)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bouncy-ball-game.git
    cd bouncy-ball-game
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Requirements

- Python 3.8
- Pygame

You can install the required packages using `pip`:
```bash
pip install pygame
```

## Gameplay

- Use the arrow keys to move the ball left and right.
- Press the spacebar to make the ball jump.
- Avoid hitting the red obstacles.
- Collect points by passing through the blue blocks.
- The game keeps track of your score and saves it to `Bouncy_ball_score.txt`.

## Project Structure

- `main.py`: The main script containing the game logic.
- `mock-background1.png`: Background image used in the game.
- `Bouncy_ball_score.txt`: File where scores are saved.

## Running the Game

To run the game, execute the `main.py` script:
```bash
python main.py
```

## File Structure

```
bouncy-ball-game/
│
├── Bouncy_ball_score.txt     # File to store scores
├── main.py                   # Main script with the game logic
├── mock-background1.png      # Background image for the game
```
