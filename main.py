import sys

from puzzle_reader import PuzzleReader


def main(strategy, param, puzzle_file, sol_file, stats_file):
    reader = PuzzleReader('./puzzles/test3x4.txt')
    puzzle = reader.getPuzzle()
    puzzle.print()
    print()
    puzzle.move('R')
    puzzle.print()


if __name__ == "__main__":
    args = sys.argv
    strategy = args[1]
    param = args[2]
    puzzle_file = args[3]
    sol_file = args[4]
    stats_file = args[5]

    if strategy not in ['bfs', 'dfs', 'astr']:
        raise Exception(f'Nieznana strategia: "{strategy}"')

    main(strategy, param, puzzle_file, sol_file, stats_file)
