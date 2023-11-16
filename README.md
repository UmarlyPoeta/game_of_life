## Game of Life

### Project Description

Conway's Game of Life is a one-dimensional simulation game devised by mathematician John Conway. This Python implementation utilizes libraries such as `numpy`, `matplotlib`, and `tkinter` to generate the board, visualize the game, and interact with the user through a graphical user interface (GUI).

### Contents

1. **game_of_life.py**: The main file containing the Game of Life code.
2. **gui_game_of_life.py**: Additional file containing the GUI-related code.
3. **requirements.txt**: A file containing a list of dependencies required to run the program.
4. **test_gui_game_of_life.py**: A test file containing Pytest tests for the GUI-related code.

### Running Instructions

1. Ensure you have a compatible version of Python installed, as specified in the `requirements.txt` file.
2. Install the dependencies by running the command: `pip install -r requirements.txt`.
3. Run the game using the command: `python gui_game_of_life.py`.

### Interacting with the Game

- Upon running the program, a window with a tkinter-based user interface will appear.
- Available options include:
    - "Show Board": Displays the current state of the board in the console.
    - "Do Iterations": Performs number of animation speed iterations of the game and displays the current state of the board in the GUI.
    - "Show Evolution": Displays a chart depicting the evolution of the number of live cells over iterations.
    - "Exit": Closes the program.
    - "Clear Boad": Clears the board
    - "Save Board": Saves a txt with current board
    - "Load Board": Load a txt file with board and displays it
    - "Animation Speed": Changes a number of iterations that "Do iterations" do

### Game Rules

- The board is a two-dimensional grid of cells.
- Each cell can be either "alive" (marked as "0") or "dead" (marked as ".").
- Each cell has 8 neighbors (cells on the sides, top, bottom, and diagonally).
- The state of cells on the board changes according to the following rules:
  - A live cell with fewer than two live neighbors dies from loneliness.
  - A live cell with more than three live neighbors dies from overpopulation.
  - A dead cell with exactly three live neighbors becomes alive.
  - In all other cases, the state of the cell remains unchanged.

### Additional Information

- The project was created using Python version 3.11.6.
- Author: Patryk Kozłowski.

### Testing

To run tests, you can use the following command:

```bash
pytest test_gui_game_of_life.py
```

The project includes Pytest tests for the GUI-related code (`test_gui_game_of_life.py`). These tests ensure the correctness of the implemented functionality and can be expanded as needed.