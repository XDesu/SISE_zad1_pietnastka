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

    def __hash__(self) -> int:
        raise Exception('Not implemented')
        to_hash = ''
        for row in self.array:
            for value in row:
                to_hash += str(value)
        return hash(to_hash)

    def __repr__(self) -> str:
        raise Exception('Not implemented')

    def __eq__(self, other: 'Puzzle') -> bool:
        return eq_2d_array(self.array, other.array)

    def get_combination(self):
        return self.to_recreate

    def deep_copy(self):
        new = Puzzle(self.width, self.height, self.array, self.id)
        new.to_recreate = deepcopy(self.to_recreate)
        # new.to_recreate = self.to_recreate + ".")[:-1]
        # new.to_recreate = self.to_recreate[:]
        new.zero_x = deepcopy(self.zero_x)
        new.zero_y = deepcopy(self.zero_y)
        # for val in self.get_combination():
        #     new.move(val)
        return new

    def check_possible_moves(self):
        possibe_moves = []

        if self.zero_y > 0:
            possibe_moves.append('R')
        if self.zero_y < self.width - 1:
            possibe_moves.append('L')
        if self.zero_x > 0:
            possibe_moves.append('D')
        if self.zero_x < self.height - 1:
            possibe_moves.append('U')

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
                # self.to_recreate.append('R')
            case 'L':
                self._moveL()
                self.to_recreate += 'L'
                # self.to_recreate.append('L')
            case 'U':
                self._moveU()
                self.to_recreate += 'U'
                # self.to_recreate.append('U')
            case 'D':
                self._moveD()
                self.to_recreate += 'D'
                # self.to_recreate.append('D')
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
