from copy import deepcopy
import re

from classes.puzzle import Puzzle


def BFS(puzzle: Puzzle, method: str):

    if puzzle.is_solved():
        return puzzle

    # create a new puzzle object
    new_puzzle = deepcopy(puzzle)

    # create a queue
    queue = []

    # add the initial state to the queue
    queue.append(new_puzzle)

    # create a list of visited states
    visited = []

    # while the queue is not empty
    while queue:

        # get the first state in the queue
        current_state: Puzzle = queue.pop(0)

        # if the current state is the goal state
        if current_state.is_solved():
            return current_state

        # if the current state has not been visited
        if current_state.get_combination() not in visited:

            # add the current state to the visited list
            visited.append(current_state.get_combination())

            # get the possible moves from the current state
            moves = current_state.check_possible_moves()
            to_move = ""
            for move in method:
                if move in moves:
                    to_move += move

            print(to_move)

            # for each move
            for move in to_move:

                # create a new state
                new_state: Puzzle = deepcopy(current_state)

                # make the move
                new_state.move(move)

                # if the new state is not in the visited list
                if new_state.get_combination() not in visited:
                    # add the new state to the queue
                    queue.append(new_state)

    return None
