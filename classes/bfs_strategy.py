from copy import deepcopy
import re

from classes.puzzle import Puzzle


def BFS(puzzle, method: str):

    # check method against regex
    if not re.match(r'[U,D,L,R]{4}', method):
        raise ValueError('Invalid method')

    if puzzle.is_solved():
        return puzzle

    # create a new puzzle object
    new_puzzle: Puzzle = deepcopy(puzzle)

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
        if current_state not in visited:

            # add the current state to the visited list
            visited.append(current_state)

            # get the possible moves from the current state
            moves = current_state.check_possible_moves()

            # for each move
            for move in moves:

                # create a new state
                new_state: Puzzle = deepcopy(current_state)

                # make the move
                new_state.move(move)

                # if the new state is not in the visited list
                if new_state not in visited:
                    # add the new state to the queue
                    queue.append(new_state)

    return None

    queue = []
