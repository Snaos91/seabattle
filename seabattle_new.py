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
        self.ships = []
        self.busy_game = []
        self.count = 0

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

        self.ships.append(ship)

    def add_contour_placement(self):
        lst_ship = self.list_ships
        for j in lst_ship:
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

    def shot(self, d):
        if d in self.busy_game:
            raise ShipException

        self.busy_game.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d[0]][d[1]] = "X"
                if ship.lives == 0:
                    self.count += 1
                    print("Корабль уничтожен!")
                    for j in self.busy_game:
                        if self.field[j[0]][j[1]] == "X":
                            try:
                                if self.field[j[0] - 1][j[1] - 1] == "-":
                                    self.field[j[0] - 1][j[1] - 1] = "*"
                                    self.busy_game.append([j[0] - 1, j[1] - 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0]][j[1] - 1] == "-":
                                    self.field[j[0]][j[1] - 1] = "*"
                                    self.busy_game.append([j[0], j[1] - 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0] + 1][j[1] - 1] == "-":
                                    self.field[j[0] + 1][j[1] - 1] = "*"
                                    self.busy_game.append([j[0] + 1, j[1] - 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0] + 1][j[1]] == "-":
                                    self.field[j[0] + 1][j[1]] = "*"
                                    self.busy_game.append([j[0] + 1, j[1]])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0] + 1][j[1] + 1] == "-":
                                    self.field[j[0] + 1][j[1] + 1] = "*"
                                    self.busy_game.append([j[0] + 1, j[1] + 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0]][j[1] + 1] == "-":
                                    self.field[j[0]][j[1] + 1] = "*"
                                    self.busy_game.append([j[0], j[1] + 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0] - 1][j[1] + 1] == "-":
                                    self.field[j[0] - 1][j[1] + 1] = "*"
                                    self.busy_game.append([j[0] - 1, j[1] + 1])
                            except IndexError:
                                pass
                            try:
                                if self.field[j[0] - 1][j[1]] == "-":
                                    self.field[j[0] - 1][j[1]] = "*"
                                    self.busy_game.append([j[0] - 1, j[1]])
                            except IndexError:
                                pass
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d[0]][d[1]] = "*"
        print("Мимо!")
        return False


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def move(self):
        while True:
            try:
                target = self.input_motion()
                repeat = self.enemy.shot(target)
                return repeat
            except ShipException as e:
                print(e)


class AI(Player):
    def input_motion(self):
        d = [randint(1, 6), randint(1, 6)]
        print(f"Ход компьютера: {d[0]} {d[1]}")
        return d


class User(Player):
    def input_motion(self):
        while True:
            try:
                player_line = int(input("Выберите линию для выстрела...."))
                player_column = int(input("Выберите столбец для выстрела... "))
                if 1 <= player_line <= 6 and 1 <= player_column <= 6:
                    return [player_line, player_column]
                else:
                    raise ValueError
            except ValueError:
                print("Ошибка! Попробуйте снова")


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
                    brd.add_contour_placement()
                    break
                except ShipException:
                    pass
        brd.contour_del()
        return brd

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")

    def start(self):
        self.greet()
        self.loop()


game = Game()
game.start()
