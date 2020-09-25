import functions
from collections import deque

def depth_first_search_start(pegboard):
    
    print("Depth-First Search:\n")

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

    depth_first_search(pegboard, q, visited, solution_path, solved)


def depth_first_search(pegboard, q, visited, solution_path, solved):
    # Append to front of queue so that the search will go down one path first.
    q.appendleft(pegboard)
    while q:
        # Pop a pegboard state.
        node = q.popleft()
        # Create a list of the possible states of the current pegboard
        # state.
        possible_states = functions.successor(node, False, False)
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

            exit("\nSolution found!")


        for state in possible_states:
            if not functions.visited_state(visited, state):
                # For each state in the possible states, check if a node has been
                # visited yet or if the board arrangement has already been added to
                # to the queue.
                visited.add(state)
                depth_first_search(state, q, visited, solution_path, solved)

            


        
