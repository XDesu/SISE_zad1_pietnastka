import sys
from classes.bfs_strategy import BFS

from puzzle_reader import PuzzleReader


def main(strategy, param, puzzle_file, sol_file, stats_file):
    reader = PuzzleReader('./puzzles/4x4_07_00212.txt')
    puzzle = reader.getPuzzle()

    print(puzzle)

    print(BFS(puzzle, "RULD"))

    for val in puzzle.get_combination():
        puzzle.move(val)

    print(puzzle)

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

#     main(strategy, param, puzzle_file, sol_file, stats_file)
