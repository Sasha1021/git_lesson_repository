import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon


class Tityl(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('tityl.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.center()
        self.setWindowTitle('Дневник огородника')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Soderg(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('soderg.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Содержание')


class Plan(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('plan.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Список задач')


class Lyna(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('lyna.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Лунный календарь')


class January(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('january.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Январь')


class February(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('february.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Февраль')


class Mart(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('mart.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Март')


class Aprel(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('aprel.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Апрель')


class Mai(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('mai.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Май')


class June(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('june.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Июнь')


class July(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('july.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Июль')


class Avgyst(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('avgyst.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Август')


class September(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('september.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Сентябрь')


class October(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('october.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Октябрь')


class November(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('november.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Ноябрь')


class December(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('december.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Декабрь')


class Blagodni(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('blagodni.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Благоприятные дни для посадки')


class Blagorabot(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('blagorabot.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Благоприятные дни для проведения работ')


class Rasten(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('rasten.ui', self)
        self.setWindowIcon(QIcon('знак.png'))
        self.setWindowTitle('Перечень растений в моем саду')


class MainWindow(QMainWindow):
    def tityl(self):
        self.w1 = Tityl()
        self.w1.klik.clicked.connect(self.soderg)
        self.w1.klik.clicked.connect(self.w1.close)
        self.w1.show()

    def soderg(self):
        self.w2 = Soderg()
        self.w2.lyna.clicked.connect(self.lyna)
        self.w2.lyna.clicked.connect(self.w2.close)
        self.w2.plan.clicked.connect(self.plan)
        self.w2.plan.clicked.connect(self.w2.close)
        self.w2.blagodni.clicked.connect(self.blagodni)
        self.w2.blagodni.clicked.connect(self.w2.close)
        self.w2.blagorabot.clicked.connect(self.blagorabot)
        self.w2.blagorabot.clicked.connect(self.w2.close)
        self.w2.rastenia.clicked.connect(self.rasten)
        self.w2.rastenia.clicked.connect(self.w2.close)
        self.w2.nazad.clicked.connect(self.tityl)
        self.w2.nazad.clicked.connect(self.w2.close)
        self.w2.show()

    def plan(self):
        self.w3 = Plan()
        self.w3.nazad.clicked.connect(self.soderg)
        self.w3.nazad.clicked.connect(self.w3.close)
        self.w3.show()

    def lyna(self):
        self.w4 = Lyna()
        self.w4.nazad.clicked.connect(self.soderg)
        self.w4.nazad.clicked.connect(self.w4.close)
        self.w4.january.clicked.connect(self.January)
        self.w4.january.clicked.connect(self.w4.close)
        self.w4.february.clicked.connect(self.February)
        self.w4.february.clicked.connect(self.w4.close)
        self.w4.mart.clicked.connect(self.Mart)
        self.w4.mart.clicked.connect(self.w4.close)
        self.w4.aprel.clicked.connect(self.Aprel)
        self.w4.aprel.clicked.connect(self.w4.close)
        self.w4.mai.clicked.connect(self.Mai)
        self.w4.mai.clicked.connect(self.w4.close)
        self.w4.june.clicked.connect(self.June)
        self.w4.june.clicked.connect(self.w4.close)
        self.w4.july.clicked.connect(self.July)
        self.w4.july.clicked.connect(self.w4.close)
        self.w4.avgyst.clicked.connect(self.Avgyst)
        self.w4.avgyst.clicked.connect(self.w4.close)
        self.w4.september.clicked.connect(self.September)
        self.w4.september.clicked.connect(self.w4.close)
        self.w4.october.clicked.connect(self.October)
        self.w4.october.clicked.connect(self.w4.close)
        self.w4.november.clicked.connect(self.November)
        self.w4.november.clicked.connect(self.w4.close)
        self.w4.december.clicked.connect(self.December)
        self.w4.december.clicked.connect(self.w4.close)
        self.w4.show()

    def January(self):
        self.w5 = January()
        self.w5.nazad.clicked.connect(self.lyna)
        self.w5.nazad.clicked.connect(self.w5.close)
        self.w5.show()

    def February(self):
        self.w6 = February()
        self.w6.nazad.clicked.connect(self.lyna)
        self.w6.nazad.clicked.connect(self.w6.close)
        self.w6.show()

    def Mart(self):
        self.w7 = Mart()
        self.w7.nazad.clicked.connect(self.lyna)
        self.w7.nazad.clicked.connect(self.w7.close)
        self.w7.show()

    def Aprel(self):
        self.w8 = Aprel()
        self.w8.nazad.clicked.connect(self.lyna)
        self.w8.nazad.clicked.connect(self.w8.close)
        self.w8.show()

    def Mai(self):
        self.w9 = Mai()
        self.w9.nazad.clicked.connect(self.lyna)
        self.w9.nazad.clicked.connect(self.w9.close)
        self.w9.show()

    def June(self):
        self.w10 = June()
        self.w10.nazad.clicked.connect(self.lyna)
        self.w10.nazad.clicked.connect(self.w10.close)
        self.w10.show()

    def July(self):
        self.w11 = July()
        self.w11.nazad.clicked.connect(self.lyna)
        self.w11.nazad.clicked.connect(self.w11.close)
        self.w11.show()

    def Avgyst(self):
        self.w12 = Avgyst()
        self.w12.nazad.clicked.connect(self.lyna)
        self.w12.nazad.clicked.connect(self.w12.close)
        self.w12.show()

    def September(self):
        self.w13 = September()
        self.w13.nazad.clicked.connect(self.lyna)
        self.w13.nazad.clicked.connect(self.w13.close)
        self.w13.show()

    def October(self):
        self.w14 = October()
        self.w14.nazad.clicked.connect(self.lyna)
        self.w14.nazad.clicked.connect(self.w14.close)
        self.w14.show()

    def November(self):
        self.w15 = November()
        self.w15.nazad.clicked.connect(self.lyna)
        self.w15.nazad.clicked.connect(self.w15.close)
        self.w15.show()

    def December(self):
        self.w16 = December()
        self.w16.nazad.clicked.connect(self.lyna)
        self.w16.nazad.clicked.connect(self.w16.close)
        self.w16.show()

    def blagodni(self):
        self.w17 = Blagodni()
        self.w17.nazad.clicked.connect(self.soderg)
        self.w17.nazad.clicked.connect(self.w17.close)
        self.w17.show()

    def blagorabot(self):
        self.w18 = Blagorabot()
        self.w18.nazad.clicked.connect(self.soderg)
        self.w18.nazad.clicked.connect(self.w18.close)
        self.w18.show()

    def rasten(self):
        self.w19 = Rasten()
        self.w19.nazad.clicked.connect(self.soderg)
        self.w19.nazad.clicked.connect(self.w19.close)
        self.w19.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.tityl()
    sys.exit(app.exec_())
