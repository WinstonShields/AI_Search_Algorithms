# Pegboard Solution Search Algorithms
This program uses the following search algorithms to solve the pegboard puzzle.
One peg, denoted by a 1, remaining on the board means that the search algorithm
successfully solved the game.

## Dependencies
Python 3

If you do not have the pip installer, you will need to install it.
Type this command in the terminal:
```bash
python get-pip.py
```

In your terminal, use the package manager pip to install numpy.
```bash
pip install numpy
```

## Usage
To run the program, type the following in the terminal:
```bash
py main.py
# Depending on how you installed Python, you might have to
# type it like "python3 main.py", "python main.py", etc.
```
You will then be prompted to select the board dimensions (mxn):
```bash
1. 4x4
2. 5x5
3. 6x6
4. 7x7
5. 8x8
6. 9x9
7. 10x10
8. English-Style
Enter Choice:
```
Enter the number associated with the choice to get the dimensions.
Next, you will be asked to select the search algorithm you would like
to see.
```bash
1. Breadth-First Search
2. Depth-First Search
3. Greedy Best-First Search
4. A* Search

Enter Choice:
```
Enter the number associated with the choice to get the algorithm.

## Results
The program will loop through and display all the nodes that are being
visited, and if a solution is found, the path that lead to the succesful
state will be displayed. If not, you will be told that no solution was
found.
