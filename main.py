import sys
import re
import os
from classes.bfs_strategy import BFS
from classes.dfs_strategy import DFS
from classes.a_star_strategy import A_star
from classes.puzzle_reader import PuzzleReader


def main(strategy, param, puzzle_file, sol_file, stats_file):

    # create directories if they don't exist
    if not os.path.exists("solutions"):
        os.makedirs("solutions")
    if not os.path.exists("statistics"):
        os.makedirs("statistics")

    puzzle_reader = PuzzleReader(f"./puzzles/{puzzle_file}")
    puzzle = puzzle_reader.get_puzzle()

    if strategy == "bfs":
        bfs = BFS(puzzle, param)
        bfs.solve()
        bfs.generate_files(sol_file, stats_file)

    elif strategy == "dfs":
        dfs = DFS(puzzle, param)
        dfs.solve()
        dfs.generate_files(sol_file, stats_file)

    elif strategy == "astr":
        astar = A_star(puzzle, param)
        astar.solve()
        astar.generate_files(sol_file, stats_file)


if __name__ == "__main__":
    args = sys.argv
    strategy = args[1]
    param = args[2]
    puzzle_file = args[3]
    sol_file = args[4]
    stats_file = args[5]

    ok = False

    if strategy not in ['bfs', 'dfs', 'astr']:
        raise Exception(f'Nieznana strategia: "{strategy}"')

    if strategy == "astr" and (param in ['hamm', 'manh']):
        ok = True

    if re.match(r'^(?=.*R)(?=.*U)(?=.*L)(?=.*D).*$', param) and len(param) == 4:
        ok = True

    if ok:
        main(strategy, param, puzzle_file, sol_file, stats_file)
    else:
        raise Exception(
            f'Nieznana metoda: "{param}" dla strategii "{strategy}"')
    exit(0)

# reader = PuzzleReader('./puzzles/4x4_01_00001.txt')
# puzzle = reader.get_puzzle()
# astr_h = A_star(puzzle, "hamm")
# astr_h.solve()
# print(astr_h)
# astr_m = A_star(puzzle, "manh")
# astr_m.solve()
# print(astr_m)
# dfs = DFS(puzzle, "RDUL")
# dfs.solve()
# print(dfs)
# bfs = BFS(puzzle, "RDUL")
# bfs.solve()
# print(bfs)
