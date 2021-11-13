from classes.puzzle import Puzzle
from time import perf_counter_ns as perf


# manhattan to odległość od prawidłowego rozwiązania
# uznaliśmy, że odległość w przypadku piętnastki to
# średnia z wszystkich odległości każdej komórki od prawidłowego rozwiązania
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


class A_star():

    def __init__(self, puzzle: Puzzle, method: str) -> None:
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
        func = manhattan_distance if self.method == "manh" else self.hamming
        start = perf()
        self._solve(func)
        self.time_taken = (perf() - start) / 1000000  # ns to ms

    def _solve(self, distance_func):
        open_list: list['Node'] = []
        closed_list: list['Node'] = []
        open_list.append(Node(self.puzzle.deep_copy(), None, 0))

        while len(open_list) > 0:
            current_node = open_list[0]
            for node in open_list:
                if node.distance < current_node.distance:
                    current_node = node

            open_list.remove(current_node)

            succesors: list['Node'] = []
            moves = current_node.puzzle.check_possible_moves()
            for move in moves:
                new_puzzle = current_node.puzzle.deep_copy()
                new_puzzle.move(move)
                new_node = Node(new_puzzle, current_node, 0)
                succesors.append(new_node)

            for succesor in succesors:
                skip = False
                if succesor.puzzle.is_solved():
                    self.solved_puzzle = succesor.puzzle.deep_copy()
                    return

                succesor.simple_distance = current_node.simple_distance + 1
                succesor.heuristic_distance = distance_func(
                    succesor.puzzle)  # to do ogarnięcia (manhattan chyba działa)
                succesor.distance = succesor.simple_distance + succesor.heuristic_distance

                for node in open_list:
                    if node.puzzle == succesor.puzzle:
                        if node.distance < succesor.distance:
                            skip = True
                            break

                for node in closed_list:
                    if node.puzzle == succesor.puzzle:
                        if node.distance < succesor.distance:
                            skip = True
                            break
                        else:
                            open_list.append(node)
                if skip:
                    continue

            closed_list.append(current_node)


class Node():
    def __init__(self, puzzle: Puzzle, parent: 'Node', distance: int):
        self.puzzle: Puzzle = puzzle
        self.parent: Node = parent
        self.distance: int = distance
        self.simple_distance: int = 0
        self.heuristic_distance: int = 0

    # def __lt__(self, other):
    #     return self.distance < other.distance

    # def __eq__(self, other):
    #     return self.distance == other.distance

    # def __hash__(self):
    #     return hash(self.puzzle)

    # def __str__(self):
    #     return f"{self.puzzle} - {self.distance}"
