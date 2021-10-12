
class Puzzle:

    def __init__(self, width: int, height: int, array, id) -> None:
        self.width = width
        self.height = height
        self.array = array
        self.id = id
        pass

    def print(self) -> None:
        """prints puzzle ¯\_(ツ)_/¯"""
        for i in range(len(self.array)):
            print(self.array[i])

    def move(self, way: str) -> None:
        """
        moves the puzzle to the given direction:
        ``R``ight, ``L``eft, ``U``p, ``D``own
        """

        match way:
            case 'R':
                self._moveR()
            case 'L':
                self._moveL()
            case 'U':
                self._moveU()
            case 'D':
                self._moveD()
            case _:
                raise Exception(
                    f'Incorrect way "{way}" in puzzle with id "{self.id}"')

    def _moveR(self):
        for i in range(self.height):
            for j in range(1, self.width):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i][j
                                                    - 1] = self.array[i][j-1], self.array[i][j]
                    return

    def _moveL(self):
        for i in range(self.height):
            for j in range(self.width-1):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i][j
                                                    + 1] = self.array[i][j+1], self.array[i][j]
                    return

    def _moveU(self):
        for i in range(self.height-1):
            for j in range(self.width):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i
                                                 + 1][j] = self.array[i+1][j], self.array[i][j]
                    return

    def _moveD(self):
        for i in range(1, self.height):
            for j in range(self.width):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i
                                                 - 1][j] = self.array[i-1][j], self.array[i][j]
                    return
