from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QAction, QMainWindow, QPushButton, QWidget, QGridLayout, QMessageBox

from game.RulesWindow import RulesWindow


class MyButton(QPushButton):
    def __init__(self, row, col, colour, figure, backColor):
        super().__init__()
        self.row = row
        self.col = col
        self.colour = colour
        self.backColor = backColor
        self.figure = figure
        self.setTextOnButton()
        self.setFixedSize(100, 100)
        self.setStyleSheet('color: %s;' % colour)

        font = QFont('Arial', 60)
        self.setFont(font)

    def setTextOnButton(self):
        self.setText(self.figure)

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col


class Field(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        self.lastButton = MyButton(-1, -1, 'red', 'O', None)
        self.count = 0
        self.buttons = []
        self.textLevel = []
        self.second_window = None
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle("Цепная реакция")

        self.max_level = 3
        self.level_numb = 1
        self.on_open(str(self.level_numb))

        menubar = self.menuBar()  # создание объекта меню
        file_menu = menubar.addMenu("Новая игра")  # создание выпадающего меню "File"

        open_action1 = QAction("Уровень 1", self)
        open_action1.triggered.connect(lambda _, name="1": self.on_open(name))

        open_action2 = QAction("Уровень 2", self)
        open_action2.triggered.connect(lambda _, name="2": self.on_open(name))

        open_action3 = QAction("Уровень 3", self)
        open_action3.triggered.connect(lambda _, name="3": self.on_open(name))

        action_restart = QAction("Заново", self)
        action_restart.triggered.connect(lambda _, : self.filling())

        rules_menu = menubar.addMenu("Правила")
        open_action_rules = QAction("Показать правила игры", self)
        open_action_rules.triggered.connect(self.open_rules_window)

        exit_menu = menubar.addMenu("выход")
        open_action_exit = QAction("выйти из игры", self)
        open_action_exit.triggered.connect(self.close)

        #todo переход на уровень
        exit_menu.addAction(open_action_exit)
        rules_menu.addAction(open_action_rules)

        file_menu.addAction(open_action1)
        file_menu.addAction(open_action2)
        file_menu.addAction(open_action3)
        file_menu.addAction(action_restart)

    def open_rules_window(self):
        self.second_window = RulesWindow()
        self.second_window.show()

    def filling(self):
        widget = QWidget()
        layout = QGridLayout()

        self.count = 0
        self.buttons = []

        self.lastButton = MyButton(-1, -1, 'red', 'O', None)

        cursorInTextLevel = 0
        for row in range(3):
            self.buttons.append([])
            for col in range(3):
                tmp = self.textLevel[cursorInTextLevel]
                mybutton = MyButton(row, col, tmp[0], tmp[1], None)
                mybutton.clicked.connect(lambda _, x=row, y=col: self.on_button_click(x, y))
                layout.addWidget(mybutton, row, col)
                self.buttons[row].append(mybutton)
                cursorInTextLevel = cursorInTextLevel + 1

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_open(self, name):
        filename = name + ".txt"

        print(name)
        with open(filename, "r") as file:
            self.textLevel = [line.strip().split() for line in file.readlines()]
            print(self.textLevel)

        self.filling()
        print('закончилось заполнение')

    def on_button_click(self, row, col):
        button = self.buttons[row][col]

        if button.backColor == 'grey':
            #print("exit")
            return

        if self.lastButton.row == -1 and self.lastButton.col == -1:
            self.lastButton = button
            button.setStyleSheet('background-color: grey;color: %s;' % button.colour)
            self.buttons[row][col].backColor = 'grey'
            self.count = self.count + 1
            return

        if abs(self.lastButton.row - row) != 0 and abs(self.lastButton.col - col) != 0:
            return

        if button.colour == self.lastButton.colour or button.figure == self.lastButton.figure:
            button.setStyleSheet('background-color: grey;color: %s;' % button.colour)
            self.lastButton = button
            self.buttons[row][col].backColor = 'grey'
            self.count = self.count + 1
            if self.count == 9:
                self.show_message_box()
                self.level_numb = self.level_numb + 1
                if self.level_numb <= self.max_level:
                    self.on_open(str(self.level_numb))
                    return


    def show_message_box(self):
        # создаем экземпляр QMessageBox
        msg_box = QMessageBox()

        # устанавливаем тип сообщения (Information)
        msg_box.setIcon(QMessageBox.Information)

        # устанавливаем заголовок сообщения
        msg_box.setWindowTitle("ПОЗДРАВЛЯЕМ!!!!!!")

        # устанавливаем текст сообщения
        msg_box.setText("ВЫ ВЫЙГРАЛИ")

        # отображаем окно сообщения
        msg_box.exec_()
