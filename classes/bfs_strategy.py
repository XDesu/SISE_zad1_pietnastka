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

    def generate_files(self, sol_file, add_file):
        self.generate_solve_file(sol_file)
        self.generate_additional_file(add_file)

    def generate_solve_file(self, file_name: str):
        f = open("solutions/" + file_name, "w")

        if len(self.solved_puzzle.get_combination()) == 0:
            f.write("-1")
            f.close()
            return

        f.write(
            f"{str(len(self.solved_puzzle.get_combination()))}\n{self.solved_puzzle.get_combination()}")

        f.close()

    def generate_additional_file(self, file_name: str):
        f = open("statistics/" + file_name, "w")

        length = len(self.solved_puzzle.get_combination()) if len(
            self.solved_puzzle.get_combination()) > 0 else -1
        f.write(f"{str(length)}\n")
        f.write(str(self.visited_states) + "\n")
        f.write(str(self.processed_states) + "\n")
        f.write("0\n")  # głębokość rekursji
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
        new_puzzle = self.puzzle.deep_copy()

        # create a queue
        queue = []

        # add the initial state to the queue
        queue.append(new_puzzle)

        # create a list of visited states
        visited = []

        # while the queue is not empty
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
                new_state: Puzzle = deepcopy(current_state)
                new_state.move(move)
                queue.append(new_state)

        return
