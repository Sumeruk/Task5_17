from PyQt5.QtWidgets import QApplication

from game.Field import Field

if __name__ == '__main__':
    app = QApplication([])
    field = Field()
    field.show()
    app.exec_()