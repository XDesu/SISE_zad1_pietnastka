from classes.puzzle import Puzzle


def test(puzzle: Puzzle, depth) -> None:
    if(depth == 4):
        return

    print("################")
    print(depth)
    print(puzzle)
    print(puzzle.get_combination())
    print("################")

    new_puzzle = puzzle.deep_copy()
    new_puzzle.move("U")
    test(new_puzzle, depth + 1)
