
class Puzzle:

    def __init__(self, array, id) -> None:
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
                raise Exception(f'Incorrect way "{way}" in puzzle with id "{self.id}"')

    def _moveR(self):
        for i in range(4):
            for j in range(1,4):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i][j-1] = self.array[i][j-1], self.array[i][j]
                    return

    def _moveL(self):
        for i in range(4):
            for j in range(3):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i][j+1] = self.array[i][j+1], self.array[i][j]
                    return

    def _moveU(self):
        for i in range(3):
            for j in range(4):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i+1][j] = self.array[i+1][j], self.array[i][j]
                    return
   
    def _moveD(self):
        for i in range(1,4):
            for j in range(4):
                if self.array[i][j] == 0:
                    self.array[i][j], self.array[i-1][j] = self.array[i-1][j], self.array[i][j]
                    return