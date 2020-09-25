import numpy as np
import random


class Pegboard:
    # Initialize pegboard class and all attributes with constructor.
    def __init__(self):
        self._board = []
        self._rows = 0
        self._columns = 0
        self._actions = ""
        self._complete = False
        self._previous = None
        self._heuristic_value = 0
        self._cost = 0

    # Getter for 2D board array.
    @property
    def board(self):
        return self._board

    # Setter for 2D board array.
    @board.setter
    def board(self, value):
        self._board = value

    # Setter for number of rows.
    @property
    def rows(self):
        return self._rows

    # Getter for number of rows.
    @rows.setter
    def rows(self, value):
        self._rows = value

    # Getter for number of columns.
    @property
    def columns(self):
        return self._columns

    # Setter for number of columns.
    @columns.setter
    def columns(self, value):
        self._columns = value

    # Getter for completion of board.
    @property
    def complete(self):
        return self._complete

    # Setter for completion of board.
    @complete.setter
    def complete(self, value):
        self._complete = value

    # Getter for state actions.
    @property
    def actions(self):
        return self._actions

    # Setter for state actions.
    @actions.setter
    def actions(self, value):
        self._actions = value

    # Getter for previous board arrangement.
    @property
    def previous(self):
        return self._previous

    # Setter for previous board arrangement.
    @previous.setter
    def previous(self, value):
        self._previous = value

    # Getter for heuristic value.
    @property
    def heuristic_value(self):
        return self._heuristic_value

    # Setter for heuristic value.
    @heuristic_value.setter
    def heuristic_value(self, value):
        self._heuristic_value = value

    # Getter for cost.
    @property
    def cost(self):
        return self._cost

    # Setter for cost.
    @cost.setter
    def cost(self, value):
        self._cost = value

    # Create and set up the board.
    def create_board(self, dimensions):
        # Initialize 2D array with selected dimensions, set all elements to one.
        self.board = np.ones([dimensions, dimensions], dtype=int)

        # Set rows and columns to the selected value.
        self.rows = dimensions
        self.columns = dimensions

        # Get list of indexes from the board array, where the element is 1.
        indexes = self.occupied_spots()

        # Randomly select an index, [m n], from the list of indexes.
        index = random.choice(indexes)

        # Set indexes of index, [m] and [n], into empty row and empty column variable
        empty_row = index[0]
        empty_col = index[1]

        # Set empty row and empty column index to zero.
        self.remove_peg(empty_row, empty_col)

        print(f"{self.board}\n")
        print(f"{self.rows} x {self.columns} Pegboard Created")

    # Getter for list of empty spots.
    def empty_spots(self):
        return np.argwhere(self.board == 0)

    # Getter for list of occupied spots.
    def occupied_spots(self):
        return np.argwhere(self.board == 1)

    # Function for when peg jumps over another peg in the upwards direction.
    # Return a value of true if it successfully moves.
    def move_peg_up(self, row, column):
        to_row = row - 2
        to_column = column
        remove = row - 1
        if self.in_bounds(to_row, column) and self.in_bounds(row, column):
            if self.occupied(row, column) and self.occupied(remove, to_column) and not self.occupied(to_row, to_column):
                self.remove_peg(row, to_column)
                self.remove_peg(remove, to_column)
                self.place_peg(to_row, to_column)

                # Set actions of state.
                str_actions = self.actions_to_string(row, column, to_row, to_column,
                                                     remove, to_column, 'up')
                self.actions = str_actions

                return True

    # Function for when peg jumps over another peg in the downwards direction.
    # Return a value of true if it successfully moves.
    def move_peg_down(self, row, column):
        to_row = row + 2
        to_column = column
        jumped_over = row + 1
        if self.in_bounds(to_row, column) and self.in_bounds(row, column):
            if self.occupied(row, column) and self.occupied(jumped_over, to_column) and not self.occupied(to_row, to_column):
                self.remove_peg(row, to_column)
                self.remove_peg(jumped_over, to_column)
                self.place_peg(to_row, to_column)

                # Set actions of state.
                str_actions = self.actions_to_string(row, column, to_row, to_column,
                                                     jumped_over, to_column, 'down')
                self.actions = str_actions
                return True

    # Function for when peg jumps over another peg in the left direction.
    # Return a value of true if it successfully moves.
    def move_peg_left(self, row, column):
        to_row = row
        to_column = column - 2
        jumped_over = column - 1
        if self.in_bounds(row, to_column) and self.in_bounds(row, column):
            if self.occupied(row, column) and self.occupied(to_row, jumped_over) and not self.occupied(to_row, to_column):
                self.remove_peg(to_row, column)
                self.remove_peg(to_row, jumped_over)
                self.place_peg(to_row, to_column)

                # Set actions of state.
                str_actions = self.actions_to_string(row, column, to_row, to_column,
                                                     to_row, jumped_over, 'left')
                self.actions = str_actions
                return True

    # Function for when peg jumps over another peg in the right direction.
    # Return a value of true if it successfully moves.
    def move_peg_right(self, row, column):
        to_row = row
        to_column = column + 2
        jumped_over = column + 1
        if self.in_bounds(row, to_column) and self.in_bounds(row, column):
            if self.occupied(row, column) and self.occupied(to_row, jumped_over) and not self.occupied(to_row, to_column):
                self.remove_peg(to_row, column)
                self.remove_peg(to_row, jumped_over)
                self.place_peg(to_row, to_column)

                # Set actions of state.
                str_actions = self.actions_to_string(row, column, to_row, to_column,
                                                     to_row, jumped_over, 'right')
                self.actions = str_actions
                return True

    # Check if the index is within the bounds of the pegboard.
    def in_bounds(self, row, column):
        if row >= 0 and row <= self.columns - 1 and column >= 0 and column <= self.columns - 1:
            return True

    # Check if the index of the pegboard has a peg or not.
    def occupied(self, row, column):
        if self.board[row][column] == 1:
            return True

    # Set position on pegboard to empty.
    def remove_peg(self, row, column):
        self.board[row][column] = 0

    # Set position on pegboard to occupied.
    def place_peg(self, row, column):
        self.board[row][column] = 1

    # Create a string for the state actions.
    def actions_to_string(self, start_row, start_col, to_row, to_col, row_jumped, col_jumped, direction):
        return(f"Moved {direction}: {[start_row, start_col]} to {[to_row, to_col]}" +
               f", Jumped over {[row_jumped, col_jumped]}")

    # If the pegboard reaches only one peg, set the completion status to true.
    def goal(self, pegboard):
        if np.count_nonzero(pegboard.board == 1) == 1:
            pegboard.complete = True
