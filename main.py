import sys
import re
import os
from classes.bfs_strategy import BFS
from classes.dfs_strategy import DFS
from test import test
from classes.a_star_strategy import A_star

from puzzle_reader import PuzzleReader

# porównywać faktyczne ustawienie zamiast listy kroków
# i zaimplementować to, szczególnie w DFS
# dobrze by było przez klase Puzzle

# coś się pierdoli z kopiowaniem, albo chuj wie co


def main(strategy, param, puzzle_file, sol_file, stats_file):

    # create directories if they don't exist
    if not os.path.exists("solutions"):
        os.makedirs("solutions")
    if not os.path.exists("statistics"):
        os.makedirs("statistics")

    reader = PuzzleReader('./puzzles/4x4_07_00001.txt')
    puzzle = reader.getPuzzle()

    astr = A_star(puzzle, "manh")
    astr.solve()
    print(astr.solved_puzzle)

    # dfs = DFS(puzzle, "RDLU")
    # dfs.solve()
    # dfs.generate_files("test.txt", "test.txt")

    # print(dfs.solved_puzzle)

    # print(str(dfs.time_taken) + "ms")
    # print(str(dfs.visited_states) + " vis")
    # print(str(dfs.processed_states) + " proc")
    # print(str(dfs.solved_puzzle.get_combination()) + " comb")

    # bfs = BFS(puzzle, "RDLU")
    # bfs.solve()
    # bfs.generate_files("test.txt", "test.txt")

    # print(str(bfs.time_taken) + "ms")
    # print(str(bfs.visited_states) + "vis")
    # print(str(bfs.processed_states) + "proc")

    # print(f"method: {bfs.method}\nprocessed: {bfs.processed_states}\nvisited: {bfs.visited_states}\ntime_taken: {bfs.time_taken}ns\n")
    # print(bfs.solved_puzzle.get_combination())

    # print("oryginał:")
    # print(bfs.puzzle)
    # print("rozwiązanie:")
    # print(bfs.solved_puzzle)

    # print(puzzle)

    # print(BFS(puzzle, "RULD"))

    # for val in puzzle.get_combination():
    #     puzzle.move(val)

    # print(puzzle)

    # print(puzzle.check_possible_moves())


main(1, 1, 1, 1, 1)

# if __name__ == "__main__":
#     args = sys.argv
#     strategy = args[1]
#     param = args[2]
#     puzzle_file = args[3]
#     sol_file = args[4]
#     stats_file = args[5]

#     if strategy not in ['bfs', 'dfs', 'astr']:
#         raise Exception(f'Nieznana strategia: "{strategy}"')

#     if strategy == "astr" and param not in ['hamm', 'manh']:
#         raise Exception(
#             f'Nieznana metoda: "{param}" dla strategii "{strategy}"')
#     elif not re.match(r'^(?=.*R)(?=.*U)(?=.*L)(?=.*D).*$', param) or len(param) != 4:
#         raise Exception(
#             f'Nieznana metoda: "{param}" dla strategii "{strategy}"')

#     main(strategy, param, puzzle_file, sol_file, stats_file)
#     exit(0)
