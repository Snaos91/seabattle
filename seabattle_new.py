from random import randint
import snoop


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
    def __init__(self, hid=False):
        self.hid = hid
        self.field = [[" ", 1, 2, 3, 4, 5, 6],
                      [1, "-", "-", "-", "-", "-", "-"],
                      [2, "-", "-", "-", "-", "-", "-"],
                      [3, "-", "-", "-", "-", "-", "-"],
                      [4, "-", "-", "-", "-", "-", "-"],
                      [5, "-", "-", "-", "-", "-", "-"],
                      [6, "-", "-", "-", "-", "-", "-"]]

        self.busy = []
        self.list_ships = []

    def __str__(self):
        res = ""
        for x in self.field:
            res += "\n" + " ".join(map(str, x))

        if self.hid:
            res = res.replace("■", "-")
        return res

    def add_ships(self, ship):
        max_dots = ship.dots[-1]
        if max_dots[0] > 6 or max_dots[1] > 6:
            raise ShipException
        if any(x in ship.dots for x in self.busy):
            raise ShipException
        for d in ship.dots:
            self.field[d[0]][d[1]] = "■"
            self.busy.append(d)
            self.list_ships.append(d)

    def add_contour(self):
        for j in self.list_ships:
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

    def contour_del(self):
        try:
            for j in self.busy:
                if self.field[j[0]][j[1]] == "*":
                    self.field[j[0]][j[1]] = "-"
        except IndexError:
            pass


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy


class AI(Player):
    pass


class User(Player):
    pass

class Game:
    def __init__(self):
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        brd = Board()
        attempts = 0
        for i in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(i, [randint(1, 6), randint(1, 6)], randint(1, 2), i)
                try:
                    brd.add_ships(ship)
                    brd.add_contour()
                    break
                except ShipException:
                    pass
        brd.contour_del()
        return brd

    def loop(self):
        print("\n")
        print("Доска пользователя")
        print(self.us.board)
        print("-----------------")
        print("Доска компьютера")
        print(self.ai.board)

    def start(self):
        self.loop()


game = Game()
game.loop()
