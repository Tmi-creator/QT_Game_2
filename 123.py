from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel


class Window(QWidget):

    def __init__(self):
        self.istext = False
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        QWidget.__init__(self)
        self.button = QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('all.png'))
        self.button.setIconSize(QtCore.QSize(600, 600))
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        self.console = QLabel('a', self)
        self.console.move(10, 900)

    def handleButton(self):
        if not self.istext:
            self.istext = True
            self.console.setText('test_Text')
            self.button.setIcon(QtGui.QIcon('all.png'))
            self.button.setFixedSize(QtCore.QSize(200, 200))
        elif self.istext:
            self.console.setText('choose completed')
            self.istext = False
            self.button.setIcon(QtGui.QIcon('background_img.jpg'))
            self.button.setIconSize(QtCore.QSize(200, 200))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    import sys

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
