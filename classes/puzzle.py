import copy
from typing import Counter
from classes.tools import eq_2d_array
from copy import deepcopy


class Puzzle:

    def __init__(self, width: int, height: int, array, id) -> None:
        self.width = deepcopy(width)
        self.height = deepcopy(height)
        self.array = deepcopy(array)
        self.id = deepcopy(id)
        self.to_recreate = ""

        self.zero_x = -1
        self.zero_y = -1
        for (i, row) in enumerate(self.array):
            for (j, value) in enumerate(row):
                if value == 0:
                    self.zero_x = i
                    self.zero_y = j
                    break
            if self.zero_x != -1:
                break
        pass

    def __str__(self):
        to_return = ''
        for row in self.array:
            to_return += "\n------------------------------------\n| "
            for value in row:
                to_return += str(value) + " | "
        to_return += "\n------------------------------------\n"
        return to_return

    def get_combination(self):
        return self.to_recreate

    def deep_copy(self):
        new = Puzzle(self.width, self.height, self.array, self.id)
        new.to_recreate = deepcopy(self.to_recreate)
        new.zero_x = deepcopy(self.zero_x)
        new.zero_y = deepcopy(self.zero_y)
        return new

    def check_possible_moves(self):
        possibe_moves = []
        changed = False

        # check if move to right is possible
        tmp = copy.deepcopy(self.array)
        self._moveR()
        if not eq_2d_array(tmp, self.array):
            changed = True
            self._moveL()
            possibe_moves.append('R')

        # check if move to left is possible
        tmp = copy.deepcopy(self.array)
        self._moveL()
        if not eq_2d_array(tmp, self.array):
            changed = True
            self._moveR()
            possibe_moves.append('L')

        # check if move up is possible
        tmp = copy.deepcopy(self.array)
        self._moveU()
        if not eq_2d_array(tmp, self.array):
            changed = True
            self._moveD()
            possibe_moves.append('U')

        # check if move down is possible
        tmp = copy.deepcopy(self.array)
        self._moveD()
        if not eq_2d_array(tmp, self.array):
            changed = True
            self._moveU()
            possibe_moves.append('D')

        if changed:
            self.to_recreate = self.to_recreate[:-2]

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
                self.to_recreate += 'R'
            case 'L':
                self._moveL()
                self.to_recreate += 'L'
            case 'U':
                self._moveU()
                self.to_recreate += 'U'
            case 'D':
                self._moveD()
                self.to_recreate += 'D'
            case _:
                raise Exception(
                    f'Incorrect way "{way}" in puzzle with id "{self.id}"')

    def _moveR(self):
        if (self.zero_y - 1) < 0:
            return
        self.array[self.zero_x][self.zero_y], self.array[self.zero_x][self.zero_y -
                                                                      1] = self.array[self.zero_x][self.zero_y - 1], self.array[self.zero_x][self.zero_y]
        self.zero_y -= 1

    def _moveL(self):
        if (self.zero_y + 1) >= self.width:
            return
        self.array[self.zero_x][self.zero_y], self.array[self.zero_x][self.zero_y +
                                                                      1] = self.array[self.zero_x][self.zero_y + 1], self.array[self.zero_x][self.zero_y]
        self.zero_y += 1

    def _moveU(self):
        if(self.zero_x + 1) >= self.height:
            return
        self.array[self.zero_x][self.zero_y], self.array[self.zero_x +
                                                         1][self.zero_y] = self.array[self.zero_x + 1][self.zero_y], self.array[self.zero_x][self.zero_y]
        self.zero_x += 1

    def _moveD(self):
        if(self.zero_x - 1) < 0:
            return
        self.array[self.zero_x][self.zero_y], self.array[self.zero_x -
                                                         1][self.zero_y] = self.array[self.zero_x - 1][self.zero_y], self.array[self.zero_x][self.zero_y]
        self.zero_x -= 1
