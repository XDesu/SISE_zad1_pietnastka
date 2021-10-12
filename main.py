from os import read
from classes.puzzle import Puzzle
from puzzle_reader import PuzzleReader

def main():
    reader = PuzzleReader('./puzzles/4x4_02_00002.txt')
    puzzle = reader.getPuzzle()
    puzzle.print()
    print()
    puzzle.move('D')
    puzzle.print()

if __name__ == "__main__":
    main()