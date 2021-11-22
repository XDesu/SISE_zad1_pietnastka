from classes.puzzle import Puzzle
from copy import deepcopy
from time import perf_counter_ns as perf


class BFS():

    def __init__(self, puzzle: Puzzle, method: str):
        self.puzzle: Puzzle = puzzle
        self.method: str = method
        self.solved_puzzle: Puzzle = None
        self.time_taken: float = 0.0
        self.processed_states: int = 0
        self.visited_states: int = 0
        self.max_depth: int = 0

    def __str__(self):
        to_return = f"{self.solved_puzzle}\n"
        to_return += f"solution: {self.solved_puzzle.get_combination()}({len(self.solved_puzzle.get_combination())})\n"
        to_return += f"method: {self.method}\n"
        to_return += f"time: {self.time_taken} ms\n"
        to_return += f"visited: {self.visited_states}\n"
        to_return += f"processed: {self.processed_states}\n"
        to_return += f"max depth: {self.max_depth}\n"
        return to_return

    def generate_files(self, sol_file, add_file):
        self.generate_solve_file(sol_file)
        self.generate_additional_file(add_file)

    def generate_solve_file(self, file_name: str):
        f = open("solutions/" + file_name, "w")

        if not self.solved_puzzle:
            f.write("-1")
            f.close()
            return

        f.write(
            f"{str(len(self.solved_puzzle.get_combination()))}\n{self.solved_puzzle.get_combination()}")

        f.close()

    def generate_additional_file(self, file_name: str):
        f = open("statistics/" + file_name, "w")

        length = len(self.solved_puzzle.get_combination()
                     ) if self.solved_puzzle else -1
        f.write(f"{str(length)}\n")
        f.write(str(self.visited_states) + "\n")
        f.write(str(self.processed_states) + "\n")
        f.write(str(self.max_depth) + "\n")
        f.write(str(self.time_taken))

        f.close()

    def solve(self):
        start_time = perf()
        self._solve()
        self.time_taken = perf() - start_time
        self.time_taken = round(self.time_taken / 1000000, 3)  # ns to ms

    def _solve(self):

        if self.puzzle.is_solved():
            self.solved_puzzle = self.puzzle.deep_copy()
            return

        new_puzzle = self.puzzle.deep_copy()

        queue = []
        queue.append(new_puzzle)

        visited = []

        while queue:

            # jeżeli wszedłem, to odwiedziłem
            # jeżeli jest w odwiedzonych, to nie przetwarzam
            # jeżeli nie ma w odwiedzonych, to zapisuję i przetwarzam
            self.visited_states += 1
            current_state: Puzzle = queue.pop(0)
            if current_state in visited:
                continue
            visited.append(current_state.deep_copy())
            self.processed_states += 1

            if len(current_state.get_combination()) > self.max_depth:
                self.max_depth = len(current_state.get_combination())

            if current_state.is_solved():
                self.solved_puzzle = current_state
                return

            # wygeneruj dostępne ruchy w odpowiedniej kolejności
            moves = current_state.check_possible_moves()
            to_move = ""
            for move in self.method:
                if move in moves:
                    to_move += move

            for move in to_move:
                new_state = current_state.deep_copy()
                new_state.move(move)
                queue.append(new_state)

        return
