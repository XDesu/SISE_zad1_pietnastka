from classes.puzzle import Puzzle
from time import perf_counter_ns as perf
from copy import deepcopy


class DFS():

    MAX_DEPTH = 4

    def __init__(self, puzzle: Puzzle, method: str):
        self.puzzle: Puzzle = puzzle
        self.method: str = method
        self.solved_puzzle: Puzzle = None
        self.time_taken: float = 0.0
        self.processed_states: int = 0
        self.visited_states: int = 0
        self.max_depth: int = 0
        self.visited = []

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
        f.write(str(self.max_depth) + "\n")
        f.write(str(self.time_taken))

        f.close()

    def solve(self):
        start = perf()
        self._solve(self.puzzle.deep_copy())
        self.time_taken = round((perf() - start) / 1000000, 3)  # ns to ms

    def _solve(self, puzzle: 'Puzzle', depth: int = 0):
        # jeżeli rozwiązane, to kończ
        if self.solved_puzzle is not None:
            return

        # jeżeli wszedłem, to odwiedziłem
        # jeżeli jest w odwiedzonych, to nie przetwarzam
        # jeżeli nie ma w odwiedzonych, to zapisuję i przetwarzam
        self.visited_states += 1
        if puzzle in self.visited:
            return
        self.visited.append(puzzle.deep_copy())
        self.processed_states += 1

        if depth > self.max_depth:
            self.max_depth = depth

        if puzzle.is_solved():
            self.solved_puzzle = puzzle.deep_copy()
            return

        if depth > DFS.MAX_DEPTH:
            return

        moves = puzzle.check_possible_moves()
        to_move = ""
        for move in self.method:
            if move in moves:
                to_move += move

        # for each move
        for move in to_move:
            new_state = puzzle.deep_copy()
            new_state.move(move)
            self._solve(new_state, depth + 1)

            # jeżeli rozwiązane, to kończ
            if self.solved_puzzle is not None:
                return

        return
