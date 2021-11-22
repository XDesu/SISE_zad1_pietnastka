from classes.puzzle import Puzzle
from time import perf_counter_ns as perf

# stany odwiedzone to stany odwiedzone z open_list
# stany przetworzone to stany których ścieżka została choć raz zapisana
# głębokość to maksymalna długość ścieżki (uwzględnia tylko stany przetworzone)


# manhattan to odległość od prawidłowego rozwiązania
# uznaliśmy, że odległość w przypadku piętnastki to
# suma z wszystkich odległości każdej komórki od prawidłowego rozwiązania
def manhattan_distance(puzzle: Puzzle) -> int:
    distance = 0
    current_value = 0

    for i in range(puzzle.height):
        for j in range(puzzle.width):
            tmp = puzzle.array[i][j]
            current_value += 1
            should_x = (tmp - 1) // puzzle.height
            should_y = (tmp - 1) % puzzle.width
            if tmp == 0:
                should_x = puzzle.height - 1
                should_y = puzzle.width - 1
            distance += abs(i - should_x) + abs(j - should_y)

    return distance


def hamming_distance(puzzle: Puzzle) -> int:
    distance = 0
    current_value = 0

    for i in range(puzzle.height):
        for j in range(puzzle.width):
            tmp = puzzle.array[i][j]
            current_value += 1
            if tmp == 0 and i == puzzle.height - 1 and j == puzzle.width - 1:
                continue
            if tmp != current_value:
                distance += 1

    return distance


class A_star():

    def __init__(self, puzzle: Puzzle, method: str) -> None:
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
        func = manhattan_distance if self.method == "manh" else hamming_distance
        start = perf()
        self._solve(func)
        self.time_taken = (perf() - start) / 1000000  # ns to ms

    def _solve(self, distance_func):
        state_scores = {}
        open_list: list[Node] = []
        open_list.append(Node(self.puzzle.deep_copy(), None))

        while len(open_list) > 0:
            self.processed_states += 1

            # wybieramy element z najmniejszą aproksymacją odległości
            current_node = open_list[0]
            for node in open_list:
                if node.aprox_dist_from_start < current_node.aprox_dist_from_start:
                    current_node = node
            open_list.remove(current_node)

            # sprawdzamy czy jest to rozwiązanie
            if current_node.puzzle.is_solved():
                self.solved_puzzle = current_node.puzzle.deep_copy()
                return

            moves = current_node.puzzle.check_possible_moves()
            for move in moves:
                # utworzenie nowego stanu
                new_puzzle = current_node.puzzle.deep_copy()
                new_puzzle.move(move)
                self.visited_states += 1

                distance_from_start = current_node.dist_from_start + 1
                aprox_distance = distance_from_start + \
                    distance_func(new_puzzle)

                # jeżeli pierwszy raz w tym stanie
                # lub jeżeli znaleziona ścieżka jest lepsza
                # to zapisujemy nową ścieżkę
                if (str(hash(new_puzzle)) not in state_scores) or (distance_from_start < state_scores[str(hash(new_puzzle))]):

                    self.visited_states += 1
                    if len(new_puzzle.get_combination()) > self.max_depth:
                        self.max_depth = len(new_puzzle.get_combination())

                    state_scores[str(hash(new_puzzle))] = distance_from_start
                    new_node = Node(new_puzzle, current_node)
                    new_node.dist_from_start = distance_from_start
                    new_node.aprox_dist_from_start = aprox_distance
                    open_list.append(new_node)
                    self.processed_states += 1


class Node():
    def __init__(self, puzzle: Puzzle, parent: 'Node'):
        self.puzzle: Puzzle = puzzle
        self.parent: Node = parent
        self.dist_from_start: int = 0
        self.aprox_dist_from_start: int = 0
