import functions
from collections import deque
import operator
import time

# Initialize the number of nodes explored.
num_of_nodes_explored = 0


def a_star_start(pegboard):

    print("A* Search:\n")

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
    # Initialize the number of nodes explored.
    num_of_nodes_explored = 0
    # Set start time for time complexity.
    start_time = time.time()

    [solved, num_of_nodes_explored] = a_star_search(pegboard, q, visited, solution_path,
                  solved, start_time)

    if not solved:
        print("\nSolution not found.")

        print(f"Nodes Explored: {num_of_nodes_explored}")
        print(f"Time Complexity: {time.time() - start_time} seconds")


def a_star_search(pegboard, q, visited, solution_path, solved, start_time):
    global num_of_nodes_explored
    # Append to front of queue so that the search will go down one path first.
    q.appendleft(pegboard)
    while q:
        # Pop a pegboard state.
        node = q.popleft()
        # Create a list of the possible states of the current pegboard
        # state with best first algorithm set to true, in order to enable
        # heuristic value logging.
        possible_states = functions.successor(node, True, True)

        # Sort the possible states by estimated cheapest path cost.
        # f(n) = g(n) + h(n)
        possible_states = sorted(possible_states, key=operator.attrgetter(
            'cost_f'), reverse=False)

        print(node.board)
        print(node.actions + '\n')
        print(node.cost_f)

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

            print("----------------------")
            print("\nSolution found!")
            print(f"Nodes Explored: {num_of_nodes_explored}")
            exit(f"Time Complexity: {time.time() - start_time} seconds")

        for state in possible_states:
            if not functions.visited_state(visited, state):
                # For each state in the possible states, check if a node has been
                # visited yet or if the board arrangement has already been added to
                # to the queue.
                visited.add(state)
                # Increment the number of nodes explored.
                num_of_nodes_explored = num_of_nodes_explored + 1
                # Recursively call the A* search function to go down
                # the path of best search first, putting a hold on the functions with
                # a higher cost of completion.
                a_star_search(state, q, visited, solution_path,
                              solved, start_time)

    # Return solved value and number of nodes explored.
    return [solved, num_of_nodes_explored]
