from random import randint


class BoardException(Exception):
    pass


class ShotForTheFieldException(BoardException):  # исключение, выстел за границы поля или поле занято
    pass


class ShotCageAgainException(BoardException):  # исключение, выстел в клетку, которая уже участвовала в игре
    pass


class Dot:  # класс точки
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # сравнение точек
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ship:  # класс корабля
    def __init__(self, ship_length, bow_ship, hor_vert, lives):
        self.ship_lenght = ship_length
        self.bow_ship = bow_ship
        self.hor_vert = hor_vert
        self.lives = lives

    @property
    def dots(self):
        ship_dots = []
        start = self.bow_ship
        if self.hor_vert == 1:
            for i in range(self.ship_lenght):
                start = self.bow_ship[0] + i, self.bow_ship[1]
                ship_dots.append(list(start))
        elif self.hor_vert == 2:
            for i in range(self.ship_lenght):
                start = self.bow_ship[0], self.bow_ship[1] + i
                ship_dots.append(list(start))
        return ship_dots


class Board:
    def __init__(self, hid=False):
        self.field = [[" ", 1, 2, 3, 4, 5, 6],
                      [1, "-", "-", "-", "-", "-", "-"],
                      [2, "-", "-", "-", "-", "-", "-"],
                      [3, "-", "-", "-", "-", "-", "-"],
                      [4, "-", "-", "-", "-", "-", "-"],
                      [5, "-", "-", "-", "-", "-", "-"],
                      [6, "-", "-", "-", "-", "-", "-"]]

        self.hid = hid
        self.count_lives = 0
        self.busy = []

    def print_field(self):
        for x in self.field:
            print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

    def add_ship(self, ship):
        contour = []
        max_dot = ship.dots[-1]

        if max_dot[0] > 6 or max_dot[1] > 6:
            return ShotForTheFieldException
        # else:
        #     for d in ship.dots:
        #         if d in self.busy:
        #             raise ShotForTheFieldException()
        else:
            for d in ship.dots:
                self.field[d[0]][d[1]] = "■"
                self.busy.append(d)
                contour.append(d)
            self.count_lives = len(ship.dots)

        for j in contour:
            if self.field[j[0] - 1][j[1] - 1] == "-":
                self.field[j[0] - 1][j[1] - 1] = "*"
                self.busy.append([j[0] - 1, j[1] - 1])
            elif self.field[j[0]][j[1] - 1] == "-":
                self.field[j[0]][j[1] - 1] = "*"
                self.busy.append([j[0], j[1] - 1])
            elif self.field[j[0] + 1][j[1] - 1] == "-":
                self.field[j[0] + 1][j[1] - 1] = "*"
                self.busy.append([j[0] + 1, j[1] - 1])
            elif self.field[j[0] + 1][j[1]] == "-":
                self.field[j[0] + 1][j[1]] = "*"
                self.busy.append([j[0] + 1, j[1]])
            elif self.field[j[0] + 1][j[1] + 1] == "-":
                self.field[j[0] + 1][j[1] + 1] = "*"
                self.busy.append([j[0] + 1, j[1] + 1])
            elif self.field[j[0]][j[1] + 1] == "-":
                self.field[j[0]][j[1] + 1] = "*"
                self.busy.append([j[0], j[1] + 1])
            elif self.field[j[0] - 1][j[1] + 1] == "-":
                self.field[j[0] - 1][j[1] + 1] = "*"
                self.busy.append([j[0] - 1, j[1] + 1])
            elif self.field[j[0] - 1][j[1]] == "-":
                self.field[j[0] - 1][j[1]] = "*"
                self.busy.append([j[0] - 1, j[1]])


class Game:
    def __init__(self):
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def get_board(self):
        return

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        for i in lens:
            try:
                ship = Ship(i, (randint(1, 6), randint(1, 6)), randint(1, 2), i)
                board.add_ship(ship)
            except ShotForTheFieldException:
                continue

        return board


game = Game()
