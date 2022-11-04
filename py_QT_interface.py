import sys
from random import *

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

from Hunter_Summons_warlock import Warlock
from Rogue_Paladin import Rogue, Paladin
from Shaman_Druid_Priest import Druid, Priest
from Warrior_Mage import Warrior, Mage

TEAMS = 4

units = {
    1: Warrior,
    2: Mage,
    3: Rogue,
    4: Paladin,
    # 5: Hunter,
    6: Warlock,
    # 7: Shaman,
    8: Druid,
    9: Priest

}

colours_of_teams = {
    1: 'QPushButton {background-color: red;}',
    2: 'QPushButton {background-color: blue;}',
    3: 'QPushButton {background-color: green;}',
    4: 'QPushButton {background-color: yellow;}'
}

description_of_units = {
    1: 'Warrior',
    2: 'Mage',
    3: "Rogue",
    4: "Paladin",
    5: "Hunter",
    6: "Warlock",
    7: 'Shaman',
    8: 'Druid',
    9: 'Priest'

}
landscape = {
    1: 'grass',
    2: 'forest',
    3: 'hill',
    4: 'destroyed_city',
    5: 'lake',
    6: 'mountain'
}

pictures_of_classes = {
    'Warrior': 'img/Warrior.png',
    'Mage': 'img/Mage.png',
    "Rogue": 'img/Rogue.png',
    "Paladin": 'img/Paladin.png',
    "Hunter": 'img/Hunter.png',
    "Warlock": 'img/Warlock.png',
    'Shaman': 'img/Warrior.png',
    'Druid': 'img/Warrior.png',
    'Priest': 'img/Warrior.png'
}

names_of_units = {
    1: 'Warrior',
    2: 'Mage',
    3: "Rogue",
    4: "Paladin",
    5: "Hunter",
    6: "Warlock",
    7: 'Shaman',
    8: 'Druid',
    9: 'Priest'

}


class Window(QWidget):

    def __init__(self):
        self.istext = False
        self.map_points = {}
        self.coords_to_buttons = {}
        self.list_of_players = []
        self.players = [[], [], [], []]
        self.placement_players = [[[0, 0], [0, 1]], [[9, 9], [9, 8]], [[9, 0], [9, 1]], [[0, 9], [1, 9]]]
        self.placement_players_check = [[[0, 0], [0, 1]], [[9, 9], [9, 8]], [[9, 0], [9, 1]], [[0, 9], [1, 9]]]
        self.cnt_teams = 0
        self.pref_of_players = [0, 0, 0, 0]
        self.coords_players = []
        self.clicked_at_class = [False for _ in range(8)]

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(2100, 2100, 2100, 2100)
        QWidget.__init__(self)
        mapa = [QPushButton("", self) for i in range(100)]
        x = int(len(mapa) ** 0.5)
        for i in range(x):
            for j in range(x):
                mapa[i * x + j].resize(80, 80)
                mapa[i * x + j].move(j * 80 + 50, i * 80 + 50)
                mapa[i * x + j].clicked.connect(self.mapButtons)

                number = randint(1, 100)
                if number < 50:
                    number = 1
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/grass.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                if 50 <= number < 65:
                    number = 2
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/forest.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                if 65 <= number < 80:
                    number = 3
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/hill.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                if 80 <= number < 90:
                    number = 4
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/destroyed_city.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                if 90 <= number < 100:
                    number = 5
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/lake.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                if number == 100:
                    number = 6
                    mapa[i * x + j].setIcon(QtGui.QIcon('img/mountain.jpg'))
                    mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                self.map_points[mapa[i * x + j]] = landscape[number] + " " + str(j) + ";" + str(i)
                self.coords_to_buttons[(j, i)] = mapa[i * x + j]

        self.console = QLabel('Here will be info about tiles', self)
        self.console.move(50, 900)
        self.right_console = QLabel(
            'Here will be info about classes ans abilities                                                            ',
            self)
        self.right_console.move(1000, 800)

        self.classes_to_choose = [QPushButton("", self) for i in range(8)]
        for i in range(4):
            for j in range(2):
                self.classes_to_choose[i * 2 + j].resize(60, 60)
                self.classes_to_choose[i * 2 + j].move(j * 60 + 1000, i * 60 + 50)
                self.classes_to_choose[i * 2 + j].clicked.connect(self.ChooseClass)
                self.classes_to_choose[i * 2 + j].setIcon(
                    QtGui.QIcon(pictures_of_classes[names_of_units[i * 2 + j + 1]]))
                self.classes_to_choose[i * 2 + j].setIconSize(QtCore.QSize(60, 60))
                self.cur_command = 0

        self.commands = [QPushButton(str(i + 1), self) for i in range(TEAMS)]
        for i in range(TEAMS):
            self.commands[i].resize(60, 60)
            self.commands[i].move(900 + i * 60, 330)
            self.commands[i].clicked.connect(self.ChooseTeam)
        self.commands[0].setStyleSheet('QPushButton {background-color: #252850; color: white;}')

        self.stop_button = QPushButton('STOP', self)
        self.stop_button.move(1040, 400)
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setStyleSheet('QPushButton {background-color: red; color: white;}')

        self.buttons_of_players = [QPushButton('', self) for i in range(8)]
        for i in range(8):
            self.buttons_of_players[i].resize(50, 50)
            self.buttons_of_players[i].move(-100, -100)
            self.buttons_of_players[i].clicked.connect(self.rightConsole)

    def mapButtons(self):
        s = ''
        s += self.map_points[self.sender()]
        for i in range(len(self.list_of_players)):
            try:
                if self.sender() == self.coords_to_buttons[self.coords_players[i]]:
                    s += f'{i.name}, hp:{i.hp}, atk:{i.atk}, mana:{i.mana}, range:{i.range}, move:{i.move}'
                    self.rightConsole()
            except:
                pass
        self.console.setText(s)
        pass

    def rightConsole(self):
        pass

    def ChooseClass(self):
        if self.clicked_at_class[self.classes_to_choose.index(self.sender())]:
            result = self.placeUnits()
            if result:
                self.players[self.cur_command].append(units[self.classes_to_choose.index(self.sender()) + 1]())
                self.list_of_players.append(units[self.classes_to_choose.index(self.sender()) + 1]())
                print(self.list_of_players)
                self.clicked_at_class[self.classes_to_choose.index(self.sender())] = False
                self.sender().setStyleSheet('QPushButton {background-color: #None;}')
        else:
            for i in range(8):
                self.clicked_at_class[i] = False
                self.classes_to_choose[i].setStyleSheet('QPushButton {background-color: None;}')
            self.clicked_at_class[self.classes_to_choose.index(self.sender())] = True
            self.sender().setStyleSheet('QPushButton {background-color: #A3C1DA;}')
            self.right_console.setText(description_of_units[self.classes_to_choose.index(self.sender()) + 1])

    def ChooseTeam(self):
        for i in range(TEAMS):
            self.commands[i].setStyleSheet('QPushButton {background-color: None;}')
        self.cur_command = self.commands.index(self.sender())
        self.sender().setStyleSheet('QPushButton {background-color: #252850; color: white;}')

    def placeUnits(self):
        try:
            self.coords_players.append(self.placement_players[self.cur_command][0])
            print(self.coords_players)
            del [self.placement_players[self.cur_command][0]]
            return 1
        except:
            self.right_console.setText('Too much players at this team, choose another')
            return 0

    def stop(self):
        self.pref_of_players[0] = len(self.players[0])
        for i in range(1, TEAMS):
            self.pref_of_players[i] = self.pref_of_players[i - 1] + len(self.players[i])
        self.pref_of_players = [0] + self.pref_of_players

        for i in range(8 - len(self.list_of_players)):
            self.buttons_of_players = self.buttons_of_players[:-1]
        k = 0
        for i in range(len(self.buttons_of_players)):
            self.buttons_of_players[i].move(65 + self.coords_players[i][0] * 80, 65 + self.coords_players[i][1] * 80)
            self.buttons_of_players[i].setIcon(QtGui.QIcon(pictures_of_classes[self.list_of_players[i].name]))
            self.buttons_of_players[i].setIconSize(QtCore.QSize(45, 45))
            for j in range(TEAMS):
                if self.coords_players[i] in self.placement_players_check[j]:
                    k = j
            self.buttons_of_players[i].setStyleSheet(colours_of_teams[k + 1])

        self.clean()

    def clean(self):
        for i in range(TEAMS):
            self.commands[i].move(-100, -100)
        for i in range(8):
            self.classes_to_choose[i].move(-100, -100)
        self.stop_button.move(-100, -100)
        self.right_console.setText('Here will be info about classes ans abilities')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
