from PyQt5 import QtWidgets

from game.rulesUi import Ui_Dialog


class RulesWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
