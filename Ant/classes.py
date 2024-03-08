import numpy as np


class Field:
    def __init__(self, size: tuple):
        self.cells = np.ones(size, dtype=bool)

    def invertion(self, x: int, y: int):
        self.cells[x][y] = 1 if self.cells[x][y] == 0 else 0


class Ant:
    def __init__(self, start_x: int, start_y: int):
        self.x = start_x
        self.y = start_y
        self.position = 0

    def turn(self, right=True):
        if right:
            value = 90
        else:
            value = 270
        self.position = self.position + value - (self.position + value) // 360 * 360

