import sys

from PySide6 import QtWidgets

from minesweeper import Minesweeper


class MyWidget(QtWidgets.QWidget, Minesweeper):
    def __init__(self):
        self.mines = 30
        QtWidgets.QWidget.__init__(self)
        Minesweeper.__init__(self, height=14, width=18, mines=self.mines)
        self.setMaximumSize(450, 350)
        self.setWindowTitle("Minesweeper")
        self.width = 18
        self.height = 14
        self.setup_ui()
        self.reproduce(first=True)

    def setup_ui(self):
        self.create_layouts()
        self.create_widgets()
        self.modify_widgets()

        self.add_widgets_to_layouts()
        self.setup_connections()

    def coord(self, i):
        print("Coord :", i)

    def create_widgets(self):
        for i in range(14):
            for y in range(18):
                self.create_button(i, y)

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass

    def create_button(self, i, y, value=9):
        font_color = "black"
        if value == 9 and self.lose:
            case = QtWidgets.QPushButton("B")
            color = "#c84c4c"
            font_color = "black"
        elif value == 9:
            case = QtWidgets.QPushButton("")
            if y % 2 == 0 and (self.height - 1 - i) % 2 == 0:
                color = "#a2d149"
            elif y % 2 == 1 and (self.height - 1 - i) % 2 == 1:
                color = "#a2d149"
            else:
                color = "#d3f590"
        else:
            if value == 0:
                case = QtWidgets.QPushButton("")
            else:
                case = QtWidgets.QPushButton(str(value))
            if y % 2 == 0 and (self.height - 1 - i) % 2 == 0:
                color = "#d7b899"
            elif y % 2 == 1 and (self.height - 1 - i) % 2 == 1:
                color = "#d7b899"
            else:
                color = "#e5c29f"
        if value == 1:
            font_color = "blue"
        elif value == 2:
            font_color = "green"
        elif value == 3:
            font_color = "red"
        elif value == 4:
            font_color = "yellow"

        case.setStyleSheet(f"""
            background-color: {color};
            color: {font_color};
            border: None;
            max-width: 25px;
            max-height: 25px;
            min-width: 25px;
            min-height: 25px;
            margin: 0px;
            """)

        case.clicked.connect(lambda: self.playing(y, self.height - 1 - i))
        self.main_layout.addWidget(case, i, y, 1, 1)

    def playing(self, x, y):
        self.player_put((x, y))
        self.reproduce()

    def reproduce(self, first=False):
        if not first:
            if self.win():
                lose = QtWidgets.QMessageBox(text="Gagné !")
                for y, listy in enumerate(self.secret_grid):
                    for x, value in enumerate(listy):
                        self.create_button(y, x, value=value)
                lose.exec()
                sys.exit(app.exec())
        if self.lose:
            lose = QtWidgets.QMessageBox(text="Perdu!")
            for y, listy in enumerate(self.secret_grid):
                for x, value in enumerate(listy):
                    self.create_button(y, x, value=value)
            lose.exec()
            sys.exit(app.exec())

        for y, listy in enumerate(self.player_grid):
            for x, value in enumerate(listy):
                self.create_button(y, x, value=value)

    def win(self):
        compteur = 0
        for y, listy in enumerate(self.player_grid):
            for x, value in enumerate(listy):
                if value == 9:
                    compteur += 1
        if compteur == self.mines:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(450, 350)
    widget.show()

    sys.exit(app.exec())
