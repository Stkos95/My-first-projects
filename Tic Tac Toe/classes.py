class Mark:
    def __init__(self, val=None):
        self.__value = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val



class Board:
    def __init__(self):
        self.res = 0
        self.marks = [[Mark() for _ in range(3)] for _ in range(3)]

    def show_board(self):
        for ind, i in enumerate(self.marks):
            res = []
            if ind != 0:
                print('----------',end='\n')
            for j in i:
                res += ' ' if j.value is None else j.value
            print(*res, sep=' | ')


    def put_value(self, x: int, y: int, val):
        if x < 3 and y < 3:
            self.marks[x][y] = Mark(val)
        else:
            print("Некорректные координаты")

    def check_winner(self, value):
        row_or_col = self._check_rows_columns_winner(value)
        diagonal = self._check_diagonal_winner(value)
        return any((row_or_col, diagonal))


    def _check_rows_columns_winner(self, value):
        for i in range(3):
            res_row = sum(1 for j in range(3) if self.marks[i][j].value == value)
            res_col = sum(1 for j in range(3) if self.marks[j][i].value == value)
            if any(map(lambda x: x == 3, [res_row, res_col])):
                return True
        return False

    def _check_diagonal_winner(self, value):
        res = sum([1 for i in range(3) if self.marks[i][i].value == value])
        res_1 = sum([1 for i in range(3) if self.marks[i][2 - i].value == value])
        return any(map(lambda x: x == 3, [res_1, res]))

    def count_available_steps(self):
        return sum(1 for i in self.marks for j in i if not j.value )

    def check_available_cell(self, x, y):
        try:
            preoccupied = self.marks[x][y].value
            if preoccupied:
                print('Cell already taken, choose other one.')
        except IndexError:
            print('Coordinates too big. Corrects coordinates: 0 < x < 2')
            preoccupied = True
        return preoccupied


