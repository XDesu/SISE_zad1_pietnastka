from copy import deepcopy
from time import perf_counter_ns as perf

from classes.puzzle import Puzzle


class BFS():

    def __init__(self, puzzle: Puzzle, method: str):
        self.puzzle: Puzzle = puzzle
        self.method: str = method
        self.solved_puzzle: Puzzle = None
        self.time_taken: int = 0
        self.processed_states: int = 0
        self.visited_states: int = 0

    def generate_files(self, sol_file, add_file):
        self.generate_solve_file(sol_file)
        self.generate_additional_file(add_file)

    def generate_solve_file(self, file_name: str):
        f = open("solved/" + file_name, "w")

        if len(self.solved_puzzle.get_combination()) == 0:
            f.write("-1")
            f.close()
            return

        f.write(
            f"{str(len(self.solved_puzzle.get_combination()))}\n{self.solved_puzzle.get_combination()}")

        f.close()

    def generate_additional_file(self, file_name: str):
        f = open("additional/" + file_name, "w")

        length = len(self.solved_puzzle.get_combination()) if len(
            self.solved_puzzle.get_combination()) > 0 else -1
        f.write(f"{str(length)}\n")
        f.write(str(self.visited_states) + "\n")
        f.write(str(self.processed_states) + "\n")
        f.write("0\n")
        f.write(str(self.time_taken))

        f.close()

    def solve(self):
        start_time = perf()
        self._solve()
        self.time_taken = perf() - start_time
        self.time_taken = round(self.time_taken / 1000000, 3)  # ns to ms

    def _solve(self):

        if self.puzzle.is_solved():
            return

        # create a new puzzle object
        new_puzzle = deepcopy(self.puzzle)

        # create a queue
        queue = []

        # add the initial state to the queue
        queue.append(new_puzzle)

        # create a list of visited states
        visited = []

        # while the queue is not empty
        while queue:
            self.visited_states += 1

            # get the first state in the queue
            current_state: Puzzle = queue.pop(0)

            # if the current state is the goal state
            if current_state.is_solved():
                self.solved_puzzle = current_state
                return

            # if the current state has not been visited
            if current_state.get_combination() not in visited:
                self.processed_states += 1

                # add the current state to the visited list
                visited.append(current_state.get_combination())

                # get the possible moves from the current state
                moves = current_state.check_possible_moves()
                to_move = ""
                for move in self.method:
                    if move in moves:
                        to_move += move

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

        return
