import copy
from typing import Counter

from classes.tools import eq_2d_array


class Puzzle:

    def __init__(self, width: int, height: int, array, id) -> None:
        self.width = width
        self.height = height
        self.array = array
        self.id = id

        self.zero_x = -1
        self.zero_y = -1
        for (i, row) in enumerate(self.array):
            for (j, value) in enumerate(row):
                if value == 0:
                    self.zero_x = i
                    self.zero_y = j
        pass

    def __str__(self):
        to_return = ''
        for row in self.array:
            to_return += "\n------------------------------------\n| "
            # print("\n------------------------------------")
            # print("| ", end="")
            for value in row:
                to_return += str(value) + " | "
                # print(value, end=" | ")
        to_return += "\n------------------------------------\n"
        # print("\n------------------------------------")
        return to_return

    def print(self) -> None:
        """prints puzzle ¯\_(ツ)_/¯"""
        for i in range(len(self.array)):
            print(self.array[i])

    def check_possible_moves(self):
        possibe_moves = []

        # check if move to right is possible
        tmp = copy.deepcopy(self.array)
        self._moveR()
        if not eq_2d_array(tmp, self.array):
            self._moveL()
            possibe_moves.append('R')

        # check if move to left is possible
        tmp = copy.deepcopy(self.array)
        self._moveL()
        if not eq_2d_array(tmp, self.array):
            self._moveR()
            possibe_moves.append('L')

        # check if move up is possible
        tmp = copy.deepcopy(self.array)
        self._moveU()
        if not eq_2d_array(tmp, self.array):
            self._moveD()
            possibe_moves.append('U')

        # check if move down is possible
        tmp = copy.deepcopy(self.array)
        self._moveD()
        if not eq_2d_array(tmp, self.array):
            self._moveU()
            possibe_moves.append('D')

        return possibe_moves

    def is_solved(self):
        counter = 1
        for i in range(self.height):
            for j in range(self.width):
                if self.array[i][j] == counter:
                    counter += 1
                    continue
                if i == self.height-1 and j == self.width-1 and self.array[i][j] == 0:
                    return True
                else:
                    return False
        return True

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
        if (self.zero_y + 1) == self.width:
            return
        self.array[self.zero_x][self.zero_y], self.array[self.zero_x][self.zero_y +
                                                                      1] = self.array[self.zero_x][self.zero_y + 1], self.array[self.zero_x][self.zero_y]

    # def _moveR(self):
    #     for i in range(self.height):
    #         for j in range(1, self.width):
    #             if self.array[i][j] == 0:
    #                 self.array[i][j], self.array[i][j
    #                                                 - 1] = self.array[i][j-1], self.array[i][j]
    #                 return

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
