import sys
from random import *

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from Hunter_Summons_warlock import Warlock
from Rogue_Paladin import Rogue, Paladin
from Shaman_Druid_Priest import Druid, Priest
from Warrior_Mage import Warrior, Mage

TEAMS = 4
EPS = 1e-6

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

landscape_img = {
    1: 'img/grass.jpg',
    2: 'img/forest.jpg',
    3: 'img/hill',
    4: 'img/destroyed_city',
    5: 'img/lake',
    6: 'img/mountain'
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
        self.turn = 0
        self.death = []
        self.ismove = False
        self.isattack = False
        self.index_now = 0
        self.map_landscape = [0 for _ in range(100)]
        self.cur_command = 0
        self.skip_start = False
        self.ismap = False
        super().__init__()
        self.initUI()

    def initUI(self):
        if not self.skip_start:
            self.setGeometry(100, 100, 100, 100)
            QWidget.__init__(self)
            self.background = QLabel('', self)
            self.setWindowTitle('Tactics game at PyQt')
            self.background.setPixmap(QPixmap('img/background.jpg'))
            # self.background.resize(1000, 1000)
            self.background.move(0, 0)
            self.mapa = [QPushButton("", self) for _ in range(100)]
            self.start_buttons = [QPushButton('From database', self) for i in range(5)]
            self.start_console = QLabel('                                                    ', self)
            self.start_console.move(800, 600)
            for i in range(5):
                self.start_buttons[i].move(110 + i * 100, 10)
                self.start_buttons[i].clicked.connect(self.draw_map)
                color1, color2, color3 = randint(0, 255), randint(0, 255), randint(0, 255)
                self.start_buttons[i].resize(100, 30)
                self.start_buttons[i].setStyleSheet(
                    'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
                    f' stop: 0 rgba({color1},{color2},{color3},255), stop: 0.2 rgba({color3},{color1},{color2},125), '
                    f'stop: 0.3 rgba({color2},{color3},{color1},0));'
                    ' color: white;}')
            self.start_buttons[0].setText('Random')
            self.start_buttons[1].setText('From file')
            self.start_buttons[3].setText('Add to a database')
            self.start_buttons[4].setText('Stop')
            self.console = QLabel('Here will be info about tiles', self)
            self.console.move(50, 900)
            self.right_console = QLabel(
                'Here will be info about classes                                                                       '
                '                                                \n                                                    '
                '   \n                                                ',
                self)
            self.right_console.move(900, 800)
            self.skill_console = QLabel('Here will be info about abilities                            \n            '
                                        '                                    \n                                        '
                                        '               ',
                                        self)
            self.skill_console.move(-100, -600)

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

            self.skills = [QPushButton('', self) for _ in range(4)]
            for i in range(4):
                self.skills[i].move(-100, -100)
                self.skills[i].resize(80, 80)
                self.skills[i].setStyleSheet(
                    'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
                    ' stop: 0 rgba(152,0,2,255), stop: 0.2 rgba(152,0,2,125), stop: 0.4 rgba(152,0,2,0));'
                    ' color: white;}')
                self.skills[i].setIcon(QtGui.QIcon('img/Warrior.png'))
                self.skills[i].setIconSize(QtCore.QSize(70, 70))
                self.skills[i].clicked.connect(self.descriprionOfSkills)

            self.cur_player = QPushButton("", self)
            self.cur_player.move(-100, -100)
            self.cur_team_player = 1

            self.move_button = QPushButton('MOVE', self)
            self.attack_button = QPushButton('ATTACK', self)
            self.move_button.move(-1000, -500)
            self.attack_button.move(-1100, -500)
            self.move_button.clicked.connect(self.move_player)
            self.attack_button.clicked.connect(self.attack)

            self.attack_button.setStyleSheet(
                'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
                ' stop: 0 rgba(255,2,0,255), stop: 0.2 rgba(195,2,0,125), stop: 0.4 rgba(155,2,0,0));'
                ' color: white;}')
            self.move_button.setStyleSheet(
                'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
                ' stop: 0 rgba(66,170,255,255), stop: 0.2 rgba(66,170,255,125), stop: 0.4 rgba(66,170,255,0));'
                ' color: white;}')

            self.turn_on_all = QLabel('turn: ' + str(self.turn) + "           ", self)
            self.turn_on_all.move(10, 10)
            self.coords_to_move = [0, 0]
            self.button_to_attack = QPushButton('', self)
            self.number_attack = 0
            self.button_to_attack.move(-100, -100)
            self.right_console.setStyleSheet("QLabel{font-size: 16pt; color: white;}")
            self.console.setStyleSheet("QLabel{font-size: 16pt; color: white;}")
            self.skill_console.setStyleSheet("QLabel{font-size: 16pt; color: white;}")

    def draw_map(self):
        if self.sender().text() == 'Random':
            x = int(len(self.mapa) ** 0.5)
            for i in range(x):
                for j in range(x):
                    self.mapa[i * x + j].resize(80, 80)
                    self.mapa[i * x + j].move(j * 80 + 50, i * 80 + 50)
                    self.mapa[i * x + j].clicked.connect(self.mapButtons)

                    number = randint(1, 100)
                    if number < 50:
                        number = 1
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/grass.jpg'))
                    if 50 <= number < 65:
                        number = 2
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/forest.jpg'))
                    if 65 <= number < 80:
                        number = 3
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/hill.jpg'))
                    if 80 <= number < 90:
                        number = 4
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/destroyed_city.jpg'))
                    if 90 <= number < 100:
                        number = 5
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/lake.jpg'))
                    if number == 100:
                        number = 6
                        self.mapa[i * x + j].setIcon(QtGui.QIcon('img/mountain.jpg'))
                    self.mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                    self.map_landscape[i * x + j] = number
                    self.map_points[self.mapa[i * x + j]] = landscape[number] + " " + str(j) + ";" + str(i)
                    self.coords_to_buttons[(j, i)] = self.mapa[i * x + j]
            for i in range(2):
                for j in range(2):
                    self.map_landscape[i * x + j] = 1
                    self.mapa[i * x + j].setIcon(QtGui.QIcon('img/grass.jpg'))
                    self.mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                    self.map_landscape[(i + 8) * x + j] = 1
                    self.mapa[(i + 8) * x + j].setIcon(QtGui.QIcon('img/grass.jpg'))
                    self.mapa[(i + 8) * x + j].setIconSize(QtCore.QSize(80, 80))
                    self.map_landscape[(i + 8) * x + j + 8] = 1
                    self.mapa[(i + 8) * x + j + 8].setIcon(QtGui.QIcon('img/grass.jpg'))
                    self.mapa[(i + 8) * x + j + 8].setIconSize(QtCore.QSize(80, 80))
                    self.map_landscape[i * x + j + 8] = 1
                    self.mapa[i * x + j + 8].setIcon(QtGui.QIcon('img/grass.jpg'))
                    self.mapa[i * x + j + 8].setIconSize(QtCore.QSize(80, 80))
            self.ismap = True


        elif self.sender().text() == 'From file':
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать файл', '',
                'Файл (*.txt);;Файл (*.docx);;Файл (*.doc);;Все файлы (*)')[0]
            f = open(fname, 'r+')
            try:
                map_file = f.readline()
                parts_of_map = map_file.split(';')
                x = int(len(self.mapa) ** 0.5)
                if len(parts_of_map) == x:
                    for i in range(x):
                        for j in range(x):
                            self.mapa[i * x + j].resize(80, 80)
                            self.mapa[i * x + j].move(j * 80 + 50, i * 80 + 50)
                            self.mapa[i * x + j].clicked.connect(self.mapButtons)
                            self.map_landscape[i * x + j] = int(parts_of_map[i][j])
                            self.mapa[i * x + j].setIcon(QtGui.QIcon(landscape_img[int(parts_of_map[i][j])]))
                            self.mapa[i * x + j].setIconSize(QtCore.QSize(80, 80))
                            self.map_points[self.mapa[i * x + j]] = landscape[int(parts_of_map[i][j])] + " " + str(
                                j) + ";" + str(i)
                    self.ismap = True
                else:
                    self.start_console.setText('Error at file')
                    self.ismap = False
                    return 0
            except:
                self.start_console.setText('Error at file')
                self.ismap = False
                return 0
        if self.sender().text() == 'Stop':
            if self.ismap:
                for i in range(5):
                    self.start_buttons[i].move(-100, -100)
                self.skip_start = True
            else:
                self.right_console.setText('Make a map')

    def mapButtons(self):
        if self.ismove:
            self.coords_to_move = list(map(int, self.map_points[self.sender()][-4:].split(';')))
            self.move_player(from_map=True)
        else:
            s = ''
            s += self.map_points[self.sender()]
            self.console.setText(s)

    def rightConsole(self):
        player = self.list_of_players[self.buttons_of_players.index(self.sender())]
        self.cur_player = self.sender()
        self.right_console.setText(
            f'player {self.buttons_of_players.index(self.sender()) + 1}, {player.name},'
            f' hp: {player.hp}, atk: {player.atk},\nmana: {player.mana}, range: {player.range},\nmove: {player.move}')
        index = self.index_of_player()
        if index == self.buttons_of_players.index(self.sender()):
            self.move_button.move(1000, 500)
            self.attack_button.move(1200, 500)
        else:
            self.ismove = False
            self.move_button.move(-100, -100)
            self.attack_button.move(-100, -100)
            if self.isattack:
                self.button_to_attack = self.sender()
                self.attack(from_console=True)

    def ChooseClass(self):
        if self.clicked_at_class[self.classes_to_choose.index(self.sender())]:
            result = self.placeUnits()
            if result:
                self.players[self.cur_command].append(units[self.classes_to_choose.index(self.sender()) + 1]())
                self.list_of_players.append(self.players[self.cur_command][-1])
                self.clicked_at_class[self.classes_to_choose.index(self.sender())] = False
                self.sender().setStyleSheet('QPushButton {background-color: None;}')
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
            del [self.placement_players[self.cur_command][0]]
            return 1
        except:
            self.right_console.setText('Too much players at this team,\nchoose another')
            return 0

    def stop(self):
        if self.skip_start:
            self.pref_of_players[0] = len(self.players[0])
            for i in range(1, TEAMS):
                self.pref_of_players[i] = self.pref_of_players[i - 1] + len(self.players[i])
            self.pref_of_players = [0] + self.pref_of_players

            for i in range(8 - len(self.list_of_players)):
                self.buttons_of_players = self.buttons_of_players[:-1]
            k = 0
            for i in range(len(self.buttons_of_players)):
                self.buttons_of_players[i].move(65 + self.coords_players[i][0] * 80,
                                                65 + self.coords_players[i][1] * 80)
                self.buttons_of_players[i].setIcon(QtGui.QIcon(pictures_of_classes[self.list_of_players[i].name]))
                self.buttons_of_players[i].setIconSize(QtCore.QSize(45, 45))
                for j in range(TEAMS):
                    if self.coords_players[i] in self.placement_players_check[j]:
                        k = j
                self.buttons_of_players[i].setStyleSheet(colours_of_teams[k + 1])
            self.skill_console.move(900, 650)
            self.clean()
            self.iswin()
        else:
            self.right_console.setText('Error, stop genering map')

    def clean(self):
        for i in range(TEAMS):
            self.commands[i].move(-100, -100)
        for i in range(8):
            self.classes_to_choose[i].move(-100, -100)
        self.stop_button.move(-100, -100)
        self.right_console.setText('Here will be info about players')
        for i in range(2):
            for j in range(2):
                self.skills[i * 2 + j].move(1000 + i * 80, j * 80 + 300)

    def descriprionOfSkills(self):
        for i in range(4):
            self.skills[i].setStyleSheet(
                'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
                ' stop: 0 rgba(152,0,2,255), stop: 0.2 rgba(152,0,2,125), stop: 0.4 rgba(152,0,2,0));'
                ' color: white;}')
        self.sender().setStyleSheet(
            'QPushButton {background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 3, fx: 0.5, fy: 0.5,'
            ' stop: 0 rgba(0,2,152,255), stop: 0.2 rgba(0,2,152,125), stop: 0.4 rgba(0,2,152,0));'
            ' color: white;}')
        self.number_attack = self.skills.index(self.sender())
        if self.cur_player in self.buttons_of_players:
            self.skill_console.setText(
                self.list_of_players[self.buttons_of_players.index(self.cur_player)].descriptions[1 +
                                                                                                  self.skills.index(
                                                                                                      self.sender())])
        else:
            self.skill_console.setText('No Player to see his abilities')

    def move_player(self, from_map=False):

        if from_map:
            coords_now = self.coords_players[self.buttons_of_players.index(self.cur_player)]
            move_player = self.list_of_players[self.buttons_of_players.index(self.cur_player)].move
            if1 = self.map_landscape[
                      self.coords_to_move[1] * int(len(self.mapa) ** 0.5) + self.coords_to_move[0]] not in [5, 6]
            if abs(coords_now[0] - self.coords_to_move[0]) + abs(
                    coords_now[1] - self.coords_to_move[1]) <= move_player and if1:
                self.coords_players[self.buttons_of_players.index(self.cur_player)] = self.coords_to_move
                self.cur_player.move(65 + self.coords_to_move[0] * 80, 65 + self.coords_to_move[1] * 80)
                self.turn_f()
                self.ismove = False
            else:
                self.right_console.setText("Error, can't move here")
        else:
            if self.ismove:
                self.ismove = False
            else:
                self.ismove = True

    def attack(self, from_console=False):
        if from_console:
            player_attack = self.list_of_players[self.index_now]
            player_attacking = self.list_of_players[self.buttons_of_players.index(self.button_to_attack)]
            coords_attacker = self.coords_players[self.index_now]
            coords_attacking = self.coords_players[self.buttons_of_players.index(self.button_to_attack)]
            if player_attack.mana >= player_attack.manacosts[self.number_attack + 1]:
                if (abs(coords_attacker[0] - coords_attacking[0]) ** 2 + abs(
                        coords_attacker[1] - coords_attacking[1]) ** 2) ** 0.5 - player_attack.range < EPS:
                    if player_attacking.immortal != 0:
                        player_attack.skills[self.number_attack + 1](player_attacking)
                    self.isattack = False
                    player_attack.mana -= player_attack.manacosts[self.number_attack + 1]
                    if player_attacking.hp <= 0:
                        self.right_console.setText(f'player {self.list_of_players.index(player_attacking) + 1} died')
                        self.button_to_attack.move(-100, -100)
                        self.death.append(player_attacking)
                        for i in range(4):
                            try:
                                self.players[i].remove(player_attacking)
                            except:
                                pass
                        self.iswin()
                    self.turn_f()
                else:
                    self.right_console.setText("Can't attack")
            else:
                self.right_console.setText('Not enough mana.\nMaybe try simple attack?')
        else:
            if self.isattack:
                self.isattack = False
            else:
                self.isattack = True

    def turn_f(self):
        self.turn += 1
        self.turn_on_all.setText("turn: " + str(self.turn))
        self.move_button.move(-100, -100)
        self.attack_button.move(-100, -100)
        self.index_now += 1
        self.isattack = False
        self.ismove = False
        for i in self.list_of_players:
            if i.immortal:
                i.immortal -= 1

    def iswin(self):
        alive = 0
        for i in range(4):
            if self.players[i]:
                alive += 1
        if alive in [0, 1]:
            for i in self.mapa:
                i.move(-100, -100)
            for i in self.skills:
                i.move(-100, -100)
            for i in self.buttons_of_players:
                i.move(-100, -100)
            self.turn_on_all.move(-100, -100)
            self.right_console.move(500, 400)
            self.right_console.setText("Good game. That's all.\nThanks for playing.")
            self.console.move(-100, -100)
            self.skill_console.move(-100, -100)

    def index_of_player(self):
        self.index_now %= len(self.list_of_players)
        while True:
            if self.list_of_players[self.index_now] in self.death:
                self.index_now += 1
            else:
                break
            self.index_now %= len(self.list_of_players)

        return self.index_now


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
