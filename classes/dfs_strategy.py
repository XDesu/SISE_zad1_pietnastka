from classes.puzzle import Puzzle
from time import perf_counter_ns as perf
from copy import deepcopy


class DFS():

    MAX_DEPTH = 20

    def __init__(self, puzzle: Puzzle, method: str):
        self.puzzle: Puzzle = puzzle
        self.method: str = method
        self.solved_puzzle: Puzzle = None
        self.time_taken: float = 0.0
        self.processed_states: int = 0
        self.visited_states: int = 0
        self.max_depth: int = 0
        self.visited = {}

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
        start = perf()
        self._solve(self.puzzle.deep_copy())
        self.time_taken = round((perf() - start) / 1000000, 3)  # ns to ms

    def _solve(self, puzzle: 'Puzzle', depth: int = 0):
        # je??eli rozwi??zane, to ko??cz
        if self.solved_puzzle is not None:
            return

        # je??eli wszed??em, to odwiedzi??em
        # je??eli jest w odwiedzonych, to nie przetwarzam
        # je??eli nie ma w odwiedzonych, to zapisuj?? i przetwarzam
        self.visited_states += 1

        # je??eli sprawdzamy czy odwiedzili??my dany stan, to ??redni czas wykonania
        # jest mniejszy, a wyniki s?? bardziej przewidywalne (jest mniejsza zale??no???? od wybranej kolejno??ci przetwarzania)
        # Niestety wyst??puje te?? taka wada, ??e zwi??ksza si?? prawodopodobie??stwo, ??e nie znajdziemy rozwi??zania
        hash_key = str(hash(puzzle))
        if hash_key in self.visited:
            return
        self.visited[hash_key] = True

        self.processed_states += 1

        if depth > self.max_depth:
            self.max_depth = depth

        if puzzle.is_solved():
            self.solved_puzzle = puzzle.deep_copy()
            return

        if depth >= DFS.MAX_DEPTH:
            return

        moves = puzzle.check_possible_moves()
        to_move = ""
        for move in self.method:
            if move in moves:
                to_move += move

        for move in to_move:
            new_state = puzzle.deep_copy()
            new_state.move(move)
            self._solve(new_state, depth + 1)

            # je??eli rozwi??zane, to ko??cz (tutaj tak na wszelki wypadek (jest ju?? na pocz??tku funkcji))
            if self.solved_puzzle is not None:
                return

        return
