from pegboard import Pegboard
import numpy as np
import random
import bfs
import dfs
import gbf
import a_star


def choose_dimensions(pegboard):

    print("Select rows and columns (m x n):\n\n"
          "1. 4x4 \n"
          "2. 5x5 \n"
          "3. 6x6 \n"
          "4. 7x7 \n"
          "5. 8x8 \n"
          "6. 9x9 \n"
          "7. 10x10 \n")

    dimensions = 0

    while True:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            dimensions = 4
            break
        elif choice == 2:
            dimensions = 5
            break
        elif choice == 3:
            dimensions = 6
            break
        elif choice == 4:
            dimensions = 7
            break
        elif choice == 5:
            dimensions = 8
            break
        elif choice == 6:
            dimensions = 9
            break
        elif choice == 7:
            dimensions = 10
            break
        else:
            print("Invalid option")

    return dimensions


def choose_search_algorithm(pegboard):
    while True:

        print("Choose Search Algorithm \n\n"
              "1. Breadth-First Search\n"
              "2. Depth-First Search\n"
              "3. Greedy Best-First Search\n"
              "4. A* Search\n")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            bfs.breadth_first_search(pegboard)
            break
        elif choice == 2:
            dfs.depth_first_search_start(pegboard)
            break
        elif choice == 3:
            gbf.greedy_best_first(pegboard)
            break
        elif choice == 4:
            a_star.a_star_search(pegboard)
            break
        else:
            print("Invalid option")


def main():
    pegboard = Pegboard()
    dimensions = choose_dimensions(pegboard)
    print('\n')
    pegboard.create_board(dimensions)
    print('\n')
    choose_search_algorithm(pegboard)


if __name__ == "__main__":
    main()
