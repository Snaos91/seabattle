from random import randint


class ShipException(Exception):
    pass


class Ship:
    def __init__(self, len_ship, bow_ship, hv, lives):
        self.len_ship = len_ship
        self.bow_ship = bow_ship
        self.hv = hv
        self.lives = lives

    @property
    def dots(self):
        ship_dots = []
        start = self.bow_ship
        if self.hv == 1:
            for i in range(self.len_ship):
                start = self.bow_ship[0] + i, self.bow_ship[1]
                ship_dots.append(list(start))
        elif self.hv == 2:
            for i in range(self.len_ship):
                start = self.bow_ship[0], self.bow_ship[1] + i
                ship_dots.append(list(start))
        return ship_dots


class Board:
    def __init__(self):
        self.field = [[" ", 1, 2, 3, 4, 5, 6],
                      [1, "-", "-", "-", "-", "-", "-"],
                      [2, "-", "-", "-", "-", "-", "-"],
                      [3, "-", "-", "-", "-", "-", "-"],
                      [4, "-", "-", "-", "-", "-", "-"],
                      [5, "-", "-", "-", "-", "-", "-"],
                      [6, "-", "-", "-", "-", "-", "-"]]

        self.busy = []

    def print_busy(self):
        return f'Busy {self.busy}'

    def print_field(self):
        for x in self.field:
            print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

    def add_ships(self, ship):
        max_dots = ship.dots[-1]
        contour = []
        print(max_dots)
        if max_dots[0] > 6 or max_dots[1] > 6:
            raise ShipException
        for d in ship.dots:
            self.field[d[0]][d[1]] = "■"
            self.busy.append(d)
            contour.append(d)

        for j in contour:
            try:
                if self.field[j[0] - 1][j[1] - 1] == "-":
                    self.field[j[0] - 1][j[1] - 1] = "*"
                    self.busy.append([j[0] - 1, j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0]][j[1] - 1] == "-":
                    self.field[j[0]][j[1] - 1] = "*"
                    self.busy.append([j[0], j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1] - 1] == "-":
                    self.field[j[0] + 1][j[1] - 1] = "*"
                    self.busy.append([j[0] + 1, j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1]] == "-":
                    self.field[j[0] + 1][j[1]] = "*"
                    self.busy.append([j[0] + 1, j[1]])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1] + 1] == "-":
                    self.field[j[0] + 1][j[1] + 1] = "*"
                    self.busy.append([j[0] + 1, j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0]][j[1] + 1] == "-":
                    self.field[j[0]][j[1] + 1] = "*"
                    self.busy.append([j[0], j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] - 1][j[1] + 1] == "-":
                    self.field[j[0] - 1][j[1] + 1] = "*"
                    self.busy.append([j[0] - 1, j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] - 1][j[1]] == "-":
                    self.field[j[0] - 1][j[1]] = "*"
                    self.busy.append([j[0] - 1, j[1]])
            except IndexError:
                pass


ship_1 = Ship(3, [randint(1, 6), randint(1, 6)], randint(1, 2), 3)
brd = Board()
brd.add_ships(ship_1)
print(brd.print_busy())
brd.print_field()

////////

from random import randint


class ShipException(Exception):
    pass


class Ship:
    def __init__(self, len_ship, bow_ship, hv, lives):
        self.len_ship = len_ship
        self.bow_ship = bow_ship
        self.hv = hv
        self.lives = lives

    @property
    def dots(self):
        ship_dots = []
        start = self.bow_ship
        if self.hv == 1:
            for i in range(self.len_ship):
                start = self.bow_ship[0] + i, self.bow_ship[1]
                ship_dots.append(list(start))
        elif self.hv == 2:
            for i in range(self.len_ship):
                start = self.bow_ship[0], self.bow_ship[1] + i
                ship_dots.append(list(start))
        return ship_dots


class Board:
    def __init__(self):
        self.field = [[" ", 1, 2, 3, 4, 5, 6],
                      [1, "-", "-", "-", "-", "-", "-"],
                      [2, "-", "-", "-", "-", "-", "-"],
                      [3, "-", "-", "-", "-", "-", "-"],
                      [4, "-", "-", "-", "-", "-", "-"],
                      [5, "-", "-", "-", "-", "-", "-"],
                      [6, "-", "-", "-", "-", "-", "-"]]

        self.busy = []

    def print_busy(self):
        return f'Busy {self.busy}'

    def print_field(self):
        for x in self.field:
            print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

    def add_ships(self, ship):
        max_dots = ship.dots[-1]
        contour = []
        print(max_dots)
        if max_dots[0] > 6 or max_dots[1] > 6:
            raise ShipException
        if any(x in ship.dots for x in self.busy):
            raise ShipException
        for d in ship.dots:
            self.field[d[0]][d[1]] = "■"
            self.busy.append(d)
            contour.append(d)

        for j in contour:
            try:
                if self.field[j[0] - 1][j[1] - 1] == "-":
                    self.field[j[0] - 1][j[1] - 1] = "*"
                    self.busy.append([j[0] - 1, j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0]][j[1] - 1] == "-":
                    self.field[j[0]][j[1] - 1] = "*"
                    self.busy.append([j[0], j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1] - 1] == "-":
                    self.field[j[0] + 1][j[1] - 1] = "*"
                    self.busy.append([j[0] + 1, j[1] - 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1]] == "-":
                    self.field[j[0] + 1][j[1]] = "*"
                    self.busy.append([j[0] + 1, j[1]])
            except IndexError:
                pass
            try:
                if self.field[j[0] + 1][j[1] + 1] == "-":
                    self.field[j[0] + 1][j[1] + 1] = "*"
                    self.busy.append([j[0] + 1, j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0]][j[1] + 1] == "-":
                    self.field[j[0]][j[1] + 1] = "*"
                    self.busy.append([j[0], j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] - 1][j[1] + 1] == "-":
                    self.field[j[0] - 1][j[1] + 1] = "*"
                    self.busy.append([j[0] - 1, j[1] + 1])
            except IndexError:
                pass
            try:
                if self.field[j[0] - 1][j[1]] == "-":
                    self.field[j[0] - 1][j[1]] = "*"
                    self.busy.append([j[0] - 1, j[1]])
            except IndexError:
                pass


ship_1 = Ship(3, [randint(1, 6), randint(1, 6)], randint(1, 2), 3)
ship_2 = Ship(2, [randint(1, 6), randint(1, 6)], randint(1, 2), 3)
brd = Board()
brd.add_ships(ship_1)
brd.add_ships(ship_2)
print(brd.print_busy())
brd.print_field()