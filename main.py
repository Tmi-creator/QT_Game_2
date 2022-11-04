from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):

    def __init__(self):
        self.istext = False
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        QWidget.__init__(self)
        mapa = [QPushButton(str(i), self) for i in range(100)]
        x = int(len(mapa) ** 0.5)
        for i in range(x):
            for j in range(x):
                mapa[i * x + j].resize(80, 80)
                mapa[i * x + j].move(j*80 + 50, i*80 + 50)
                mapa[i * x + j].clicked.connect(self.handleButton)

    def handleButton(self):
        print(self.sender())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    import sys

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
