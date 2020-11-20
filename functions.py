from pegboard import Pegboard
import copy
import numpy as np


def successor(pegboard, get_heuristic, get_cost):
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

            if get_heuristic:
                # Get heuristic value if heuristic is enabled.
                state1.heuristic_value = heuristic(state1)

            if get_cost:
                # Get cost value of the previous state to the next state.
                state1.cost_g = state1.cost_g + 1
                # Get the estimated cost of the cheapest solution.
                state1.calculate_cost_f()

        state2 = Pegboard()
        state2 = copy.deepcopy(pegboard)
        state2.previous = pegboard

        if state2.move_peg_down(spot[0] - 2, spot[1]):
            # If possible, append the state where the peg moves down
            # to the empty spot.
            possible_states.append(state2)

            if get_heuristic:
                # Get heuristic value if heuristic is enabled.
                state2.heuristic_value = heuristic(state2)

            if get_cost:
                # Get cost value of the previous state to the next state.
                state2.cost_g = state2.cost_g + 1
                # Get the estimated cost of the cheapest solution.
                state2.calculate_cost_f()

        state3 = Pegboard()
        state3 = copy.deepcopy(pegboard)
        state3.previous = pegboard

        if state3.move_peg_left(spot[0], spot[1] + 2):
            # If possible, append the state where the peg moves left
            # to the empty spot.
            possible_states.append(state3)

            if get_heuristic:
                # Get heuristic value if heuristic is enabled.
                state3.heuristic_value = heuristic(state3)

            if get_cost:
                # Get cost value of the previous state to the next state.
                state3.cost_g = state3.cost_g + 1
                # Get the estimated cost of the cheapest solution.
                state3.calculate_cost_f()

        state4 = Pegboard()
        state4 = copy.deepcopy(pegboard)
        state4.previous = pegboard

        if state4.move_peg_right(spot[0], spot[1] - 2):
            # If possible, append the state where the peg moves right
            # to the empty spot.
            possible_states.append(state4)

            if get_heuristic:
                # Get heuristic value if heuristic is enabled.
                state4.heuristic_value = heuristic(state4)

            if get_cost:
                # Get cost value of the previous state to the next state.
                state4.cost_g = state4.cost_g + 1
                # Get the estimated cost of the cheapest solution.
                state4.calculate_cost_f()

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
