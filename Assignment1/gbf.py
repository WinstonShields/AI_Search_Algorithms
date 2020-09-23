import functions
from collections import deque

# Initialize a very long number for a maximum value.
MAX = 1000000000000000000

def greedy_best_first(pegboard):
    print("Greedy Best-First Search:\n")

    # Initialize queue for states.
    q = deque()
    # Append initial state of pegboard to the queue.
    q.append(pegboard)
    # Initialize set of visited nodes.
    visited = set()
    # Initialize the solved flag to false.
    solved = False
    # Initialize a list for the path that succeeds.
    solution_path = []

    # While the queue is not empty...
    while q:
        # Pop a pegboard state.
        node = q.popleft()
        # Create a list of the possible states of the current pegboard
        # state.
        possible_states = functions.successor(node)

        print(node.board)
        print(node.actions + '\n')

        if node.goal(node):
            # If the goal is reached, one peg left on the board, set the
            # state to complete.
            node.complete = True

        if node.complete:
            # If the node is complete, append the node to the solution path and break
            # the loop.
            solution_path.append(node)
            solved = True
            print("\n\n\nPath to Solution Found!")
            break

        # Initialize the minimum distance to a very high value.
        minimum_distance = MAX

        # Initialize the next state to be selected to none.
        next_state = None

        for state in possible_states:
            # For each state in the possible states, check if a node has been
            # visited yet or if the board arrangement has already been added to
            # to the queue.
            if not functions.visited_state(visited, state):
                manhattan_distance_sum = functions.heuristic(state)
                # Add the state to the set of visited nodes.
                visited.add(state)
               
                if manhattan_distance_sum < minimum_distance:
                    # If the possible state's Manhattan Distance sum is less than the
                    # current minimum distance, set the minimum distance as the possible
                    # state's Manhattan Distance.
                    minimum_distance = manhattan_distance_sum
                    # Set the next state as the current possible state.
                    next_state = state

        if next_state is not None:
            # Append the possible state with the lowest Manhattan Distance sum to the queue.
            q.append(next_state)


    for state in solution_path:
        # For each state in the solution path, set the node's previous
        # state as the previous state variable.
        previous_state = state.previous

        if previous_state is not None:
            # If the previous state is not none, append it to the solution
            # path.
            solution_path.append(previous_state)

    for state in reversed(solution_path):
        # For each state in the solution path, print it in reverse order.
        print(state.board)
        print(state.actions + '\n')

    if solved:
        print("\nSolution found!")
    else:
        print("\nSolution not found.")
