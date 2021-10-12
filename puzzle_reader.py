
from classes.puzzle import Puzzle

class PuzzleReader():

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        f = open(self.file_name, 'r')

        # get width and height of puzzle from file
        self.width, self.height = f.readline().split()
        self.width, self.height = int(self.width), int(self.height)
        
        self.tab = []

        # read puzzle from file
        i: int = 0
        while line := f.readline():
            line = list(map(int, line.split()))
            self.tab.append(line)
            if len(self.tab[i]) != self.width:
                f.close()
                raise Exception(f'Wrong amount of numbers in line {i+2} in file {file_name}')
            i = i+1
        f.close()

        if len(self.tab) != self.height:
            raise Exception(f'Wrong amount of lines in file {file_name}')

    def getHeight(self) -> int:
        return self.height

    def getWitdth(self) -> int:
        return self.width
        
    def getArray(self):
        return self.tab

    def getPuzzle(self):
        return Puzzle(self.tab, self.file_name)