import sys
import re
import os
from classes.bfs_strategy import BFS

from puzzle_reader import PuzzleReader


def main(strategy, param, puzzle_file, sol_file, stats_file):

    # create directories if they don't exist
    if not os.path.exists("solved"):
        os.makedirs("solved")
    if not os.path.exists("additional"):
        os.makedirs("additional")

    reader = PuzzleReader('./puzzles/4x4_07_00137.txt')
    puzzle = reader.getPuzzle()

    bfs = BFS(puzzle, "DULR")
    bfs.solve()
    bfs.generate_files("test.txt", "test.txt")

    print(str(bfs.time_taken) + "ms")

    # print(f"method: {bfs.method}\nprocessed: {bfs.processed_states}\nvisited: {bfs.visited_states}\ntime_taken: {bfs.time_taken}ns\n")
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
