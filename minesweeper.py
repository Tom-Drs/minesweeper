from random import randint
import pprint as pp
from copy import deepcopy
from random import randint


class Minesweeper:

    def __init__(self, mines=5, width=10, height=10):
        self.mines = mines
        self.width = width
        self.height = height
        self.lose = False
        self.secret_grid = [[0 for _ in range(width)] for _ in range(height)]
        self.player_grid = [[9 for _ in range(width)] for _ in range(height)]
        # self.init_mines()
        self.init_mines()
        print("Secret grid : ")
        pp.pprint(self.secret_grid)
        print("----------")
        # print("Your grid :")
        # pp.pprint(self.player_grid)
        # print("----------")

    def print_secret_grid(self):
        secret_grid = deepcopy(self.secret_grid)
        y_axe = [secret_grid[height].insert(0, self.height - (height + 1)) for height in range(self.height - 1, -1, -1)]

        secret_grid.append([0])

        x_axe = [secret_grid[-1].append(width) for width in range(self.width)]

        pp.pprint(secret_grid)

    def print_player_grid(self):
        secret_grid = deepcopy(self.player_grid)
        y_axe = [secret_grid[height].insert(0, self.height - (height + 1)) for height in range(self.height - 1, -1, -1)]

        secret_grid.append([0])

        x_axe = [secret_grid[-1].append(width) for width in range(self.width)]

        pp.pprint(secret_grid)

    def init_mines(self):
        coord_mines = []
        for _ in range(self.mines):
            coord = (randint(0, self.width - 1), randint(0, self.height - 1))
            while coord in coord_mines:
                coord = (randint(0, self.width -1), randint(0, self.height -1))
            self.put_secret_grid(coord, 9)
            for value in self.get_near_case(coord).values():
                if value[2] != 9:
                    self.put_secret_grid((value[0], value[1]), value[2] + 1)
            coord_mines.append(coord)

    def get_coordinates(self, coord):
        if not isinstance(coord, tuple):
            raise "Please argument need to be a tuple."
        else:
            return coord[0], self.height - 1 - coord[1]

    def get_near_case(self, coord):
        coord_convert = self.get_coordinates(coord)
        x = coord_convert[0]
        y = coord_convert[1]
        between_width = lambda n: 0 <= n <= self.width - 1
        between_heigth = lambda n: 0 <= n <= self.height - 1
        result = {}
        if between_width(x) and between_heigth(y - 1):
            result.update({"top": (coord[0], coord[1] + 1, self.secret_grid[y - 1][x])})
        if between_width(x) and between_heigth(y + 1):
            result.update({"bottom": (coord[0], coord[1] - 1, self.secret_grid[y + 1][x])})
        if between_width(x - 1) and between_heigth(y - 1):
            result.update({"left_top": (coord[0] - 1, coord[1] + 1, self.secret_grid[y - 1][x - 1])})
        if between_width(x + 1) and between_heigth(y - 1):
            result.update({"right_top": (coord[0] + 1, coord[1] + 1, self.secret_grid[y - 1][x + 1])})
        if between_width(x - 1) and between_heigth(y + 1):
            result.update({"left_bottom": (coord[0] - 1, coord[1] - 1, self.secret_grid[y + 1][x - 1])})
        if between_width(x + 1) and between_heigth(y + 1):
            result.update({"right_bottom": (coord[0] + 1, coord[1] - 1, self.secret_grid[y + 1][x + 1])})
        if between_width(x - 1) and between_heigth(y):
            result.update({"left": (coord[0] - 1, coord[1], self.secret_grid[y][x - 1])})
        if between_width(x + 1) and between_heigth(y):
            result.update({"right": (coord[0] + 1, coord[1], self.secret_grid[y][x + 1])})
        return result

    def put_secret_grid(self, coord, value):
        coord = self.get_coordinates(coord)
        self.secret_grid[coord[1]][coord[0]] = value

    def put_player_grid(self, coord, value):
        coord = self.get_coordinates(coord)
        self.player_grid[coord[1]][coord[0]] = value

    def player_put(self, coord, already=[]):
        secret_coord = self.get_coordinates(coord)
        secret_value = self.secret_grid[secret_coord[1]][secret_coord[0]]
        if secret_value == 9:
            print("PERDU !")
            self.lose = True
            return
        elif secret_value != 0:
            # print("Chiffre !")
            self.put_player_grid(coord, secret_value)
            # self.print_player_grid()
            # print("----------")
            return

        if coord not in already:
            already.append(coord)
            self.put_player_grid(coord, 0)
            for values in self.get_near_case(coord).values():
                self.player_put((values[0], values[1]), already)


        # self.print_player_grid()
        # print("----------")



