from pegboard import Pegboard
import copy
import numpy as np


def successor(pegboard, best_first):
    # Get list of empty spots on pegboard.
    empty_spots = pegboard.empty_spots()

    # Initialize list of possible states.
    possible_states = []

    # For each empty spot on the board...
    for spot in empty_spots:
        # Create a new pegboard object and copy the attributes from
        # the last state onto the the new object. Set the last state
        # of the pegboard as the previous state for the new pegboard.
        state1 = Pegboard()
        state1 = copy.deepcopy(pegboard)
        state1.previous = pegboard

        if state1.move_peg_up(spot[0] + 2, spot[1]):
            # If possible, append the state where the peg moves up
            # to the empty spot.
            possible_states.append(state1)

            if best_first:
                # If this is a best first algorithm, get the heuristic value
                # of the state.
                state1.heuristic_value = heuristic(state1)

        state2 = Pegboard()
        state2 = copy.deepcopy(pegboard)
        state2.previous = pegboard

        if state2.move_peg_down(spot[0] - 2, spot[1]):
            # If possible, append the state where the peg moves down
            # to the empty spot.
            possible_states.append(state2)

            if best_first:
                # If this is a best first algorithm, get the heuristic value
                # of the state.
                state2.heuristic_value = heuristic(state2)

        state3 = Pegboard()
        state3 = copy.deepcopy(pegboard)
        state3.previous = pegboard

        if state3.move_peg_left(spot[0], spot[1] + 2):
            # If possible, append the state where the peg moves left
            # to the empty spot.
            possible_states.append(state3)

            if best_first:
                # If this is a best first algorithm, get the heuristic value
                # of the state.
                state3.heuristic_value = heuristic(state3)

        state4 = Pegboard()
        state4 = copy.deepcopy(pegboard)
        state4.previous = pegboard

        if state4.move_peg_right(spot[0], spot[1] - 2):
            # If possible, append the state where the peg moves right
            # to the empty spot.
            possible_states.append(state4)

            if best_first:
                # If this is a best first algorithm, get the heuristic value
                # of the state.
                state4.heuristic_value = heuristic(state4)

    # Return all possible states as a list.
    return possible_states


def heuristic(state):
    # Set the goal position at the center of the board state.
    goal = [int(state.rows/2), int(state.columns/2)]

    # Initialize the sum of the Manhattan Distance's.
    manhattan_distance_sum = 0

    for peg in state.occupied_spots():
        # Row Distance = |Node Row - Goal Row|
        dx = abs(peg[0] - goal[0])
        # Column Distance = |Node Column - Goal Column|
        dy = abs(peg[1] - goal[1])
        # Manhattan Distance = Row Distance + Column Distance
        manhattan_distance = dx + dy
        # Add all of the Manhattan Distance's together.
        manhattan_distance_sum = manhattan_distance_sum + manhattan_distance

    # Return the Manhattan Distance sum.
    return manhattan_distance_sum


def visited_state(set, state):
    # Check if pegboard arrangement (arrangement of all pieces on the board) is
    # already in the queue.
    if any(np.array_equal(node.board, state.board) for node in set):
        return True
