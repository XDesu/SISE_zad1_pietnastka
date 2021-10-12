from puzzle_reader import PuzzleReader

def main():
    reader = PuzzleReader('./puzzles/4x4_07_00196.txt')
    puzzle = reader.getPuzzle()
    puzzle.print()
    print()
    puzzle.move('D')
    puzzle.print()

if __name__ == "__main__":
    main()