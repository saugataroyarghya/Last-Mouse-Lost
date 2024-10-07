# Last Mouse Lost Game

## Project Overview
This is a Python-based implementation of the **Last Mouse Lost** game, designed for two players (human vs. AI or AI vs. AI). The goal is to avoid being the player who removes the last mouse from the board. Various AI strategies have been implemented, offering multiple difficulty levels.

## Features
- **Graphical User Interface (GUI):** Developed using Tkinter, providing a smooth and interactive user experience.
- **AI Opponents:** Six AI strategies (Random, Smart, Fuzzy Logic, Minimax, Genetic Algorithm, and A*) are available for the player to compete against.
- **Multiple Difficulty Levels:** AI strategies range from basic (Random) to more advanced (Minimax, A*), challenging players of varying skill levels.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saugataroyarghya/Last-Mouse-Lost.git
   ```
2. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play
1. Run the Python script:
   ```bash
   python game.py
   ```
2. Use the **Main Menu** to start a new game, select an AI opponent, and choose the difficulty level.
3. In each turn, select a row and the number of mice to remove. Avoid removing the last mouse to win the game.

## AI Strategies
- **Random AI:** Makes random moves without considering the board state.
- **Smart AI:** Attempts to create difficult board configurations for the opponent.
- **Fuzzy Logic AI:** Evaluates moves based on fuzzy logic principles.
- **Minimax AI:** Uses the Minimax algorithm with alpha-beta pruning for optimal moves.
- **Genetic Algorithm AI:** Utilizes evolutionary strategies to optimize move sequences.
- **A\* AI:** Applies the A* search algorithm to find the shortest path to victory.

ow

## Future Improvements
- Add more advanced AI strategies, including reinforcement learning.
- Develop a multiplayer mode for competitive play.
- Improve GUI design for a more polished user experience.

## Contributions
- **[Soummo Bhattacharya](https://github.com/SoummoSsj) (Roll: 1907105):**
  - Developed the Random, Minimax AI, A* AI  and Fuzzy Logic AI players.
  - Worked on GUI design and user interactions.
  
- **[Saugata Roy Arghya](https://github.com/saugataroyarghya) (Roll: 1907116):**
  - Implemented Smart, Fuzzy Logic and Genetic Algorithm strategies.
  - Contributed to the game logic and AI integration with the game interface.

## License
This project is licensed under the MIT License.
```
