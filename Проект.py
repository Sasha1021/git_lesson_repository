import sys

import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class Dnevnik(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 350, 300, 350)
        self.setWindowTitle('Дневник огородника')
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("a8777.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.nazvanie_label = QPushButton("Дневник огородника", self)
        self.nazvanie_label.resize(250, 45)
        self.nazvanie_label.setFont(QtGui.QFont("Segoe Print", 14, QtGui.QFont.Bold))
        self.nazvanie_label.move(45, 20)

class Soderg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Содержание')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("05.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setGeometry(400, 350, 400, 350)
        self.soderj_label = QLabel(self)
        self.soderj_label.setText("Содержание")
        self.soderj_label.resize(350, 35)
        self.soderj_label.setFont(QtGui.QFont("Segoe Print", 14, QtGui.QFont.Bold))
        self.soderj_label.move(160, 20)
        self.initUI()

    def initUI(self):
        self.lyna_label = QLabel(self)
        self.lyna_label = QPushButton("Лунный календарь", self)
        self.lyna_label.resize(200, 35)
        self.lyna_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.lyna_label.show()
        self.lyna_label.move(140, 85)

        self.blagodni_label = QLabel(self)
        self.blagodni_label = QPushButton("Благоприятные дни для посадки", self)
        self.blagodni_label.resize(330, 35)
        self.blagodni_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.blagodni_label.show()
        self.blagodni_label.move(80, 135)

        self.sad_label = QLabel(self)
        self.sad_label = QPushButton("Перечень обитателей в моем саду", self)
        self.sad_label.resize(370, 35)
        self.sad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.sad_label.show()
        self.sad_label.move(60, 185)

        self.blagorabot_label = QLabel(self)
        self.blagorabot_label = QPushButton("Благоприятные дни для проведения работ", self)
        self.blagorabot_label.resize(450, 35)
        self.blagorabot_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.blagorabot_label.show()
        self.blagorabot_label.move(15, 235)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.resize(150, 35)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(170, 350)

class Lyna(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("lyna.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setWindowTitle('Лунный календарь')
        self.meciz_label = QLabel(self)
        self.setGeometry(300, 200, 300, 200)
        self.meciz_label.setText("Лунный календарь 2019")
        self.meciz_label.resize(450, 35)
        self.meciz_label.setFont(QtGui.QFont("Segoe Print", 14, QtGui.QFont.Bold))
        self.meciz_label.move(40, 20)
        self.initUI()

    def initUI(self):
        self.january_label = QLabel(self)
        self.january_label = QPushButton("Январь", self)
        self.january_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.january_label.show()
        self.january_label.move(20, 85)

        self.february_label = QLabel(self)
        self.february_label = QPushButton("Февраль", self)
        self.february_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.february_label.show()
        self.february_label.move(130, 85)

        self.mart_label = QLabel(self)
        self.mart_label = QPushButton("Март", self)
        self.mart_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.mart_label.show()
        self.mart_label.move(240, 85)

        self.aprel_label = QLabel(self)
        self.aprel_label = QPushButton("Апрель", self)
        self.aprel_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.aprel_label.show()
        self.aprel_label.move(20, 120)

        self.mai_label = QLabel(self)
        self.mai_label = QPushButton("Май", self)
        self.mai_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.mai_label.show()
        self.mai_label.move(130, 120)

        self.june_label = QLabel(self)
        self.june_label = QPushButton("Июнь", self)
        self.june_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.june_label.show()
        self.june_label.move(240, 120)

        self.july_label = QLabel(self)
        self.july_label = QPushButton("Июль", self)
        self.july_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.july_label.show()
        self.july_label.move(20, 155)

        self.avgyst_label = QLabel(self)
        self.avgyst_label = QPushButton("Август", self)
        self.avgyst_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.avgyst_label.show()
        self.avgyst_label.move(130, 155)

        self.september_label = QLabel(self)
        self.september_label = QPushButton("Сентябрь", self)
        self.september_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.september_label.show()
        self.september_label.move(240, 155)

        self.october_label = QLabel(self)
        self.october_label = QPushButton("Октябрь", self)
        self.october_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.october_label.show()
        self.october_label.move(20, 190)

        self.november_label = QLabel(self)
        self.november_label = QPushButton("Ноябрь", self)
        self.november_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.november_label.show()
        self.november_label.move(130, 190)

        self.december_label = QLabel(self)
        self.december_label = QPushButton("Декабрь", self)
        self.december_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.december_label.show()
        self.december_label.move(240, 190)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 9, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(130, 225)


class January(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Январь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class February(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Февраль')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("2.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Mart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Март')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("3.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Aprel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Апрель')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("4.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Mai(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Май')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("5.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class June(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Июнь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("6.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class July(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Июль')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("7.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Avgyst(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Август')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("8.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class September(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сентябрь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("9.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class October(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Октябрь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("10.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class November(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ноябрь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("11.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class December(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Декабрь')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("12.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Blagodni(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Благоприятные дни для посадки')
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("02.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.resize(150, 35)
        self.nazad_label.setFont(QtGui.QFont("Segoe Print", 10, QtGui.QFont.Bold))
        self.nazad_label.show()
        self.nazad_label.move(810, 710)


class Blagorabot(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("13.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class MainWindow(QMainWindow):
    def w_1(self):
        self.w1 = Dnevnik()
        self.w1.nazvanie_label.clicked.connect(self.w_2)
        self.w1.nazvanie_label.clicked.connect(self.w1.close)
        self.w1.show()

    def w_2(self):
        self.w2 = Soderg()
        self.w2.lyna_label.clicked.connect(self.w_3)
        self.w2.lyna_label.clicked.connect(self.w2.close)
        self.w2.blagodni_label.clicked.connect(self.w_4)
        self.w2.blagodni_label.clicked.connect(self.w2.close)
        self.w2.nazad_label.clicked.connect(self.w_1)
        self.w2.nazad_label.clicked.connect(self.w2.close)
        self.w2.show()

    def w_3(self):
        self.w3 = Lyna()
        self.w3.january_label.clicked.connect(self.w_5)
        self.w3.january_label.clicked.connect(self.w3.close)
        self.w3.february_label.clicked.connect(self.w_6)
        self.w3.february_label.clicked.connect(self.w3.close)
        self.w3.mart_label.clicked.connect(self.w_7)
        self.w3.mart_label.clicked.connect(self.w3.close)
        self.w3.aprel_label.clicked.connect(self.w_8)
        self.w3.aprel_label.clicked.connect(self.w3.close)
        self.w3.mai_label.clicked.connect(self.w_9)
        self.w3.mai_label.clicked.connect(self.w3.close)
        self.w3.june_label.clicked.connect(self.w_10)
        self.w3.june_label.clicked.connect(self.w3.close)
        self.w3.july_label.clicked.connect(self.w_11)
        self.w3.july_label.clicked.connect(self.w3.close)
        self.w3.avgyst_label.clicked.connect(self.w_12)
        self.w3.avgyst_label.clicked.connect(self.w3.close)
        self.w3.september_label.clicked.connect(self.w_13)
        self.w3.september_label.clicked.connect(self.w3.close)
        self.w3.october_label.clicked.connect(self.w_14)
        self.w3.october_label.clicked.connect(self.w3.close)
        self.w3.november_label.clicked.connect(self.w_15)
        self.w3.november_label.clicked.connect(self.w3.close)
        self.w3.december_label.clicked.connect(self.w_16)
        self.w3.december_label.clicked.connect(self.w3.close)
        self.w3.nazad_label.clicked.connect(self.w_2)
        self.w3.nazad_label.clicked.connect(self.w3.close)
        self.w3.show()

    def w_4(self):
        self.w4 = Blagodni()
        self.w4.nazad_label.clicked.connect(self.w_2)
        self.w4.nazad_label.clicked.connect(self.w4.close)
        self.w4.show()

    def w_5(self):
        self.w5 = January()
        self.w5.nazad_label.clicked.connect(self.w_3)
        self.w5.nazad_label.clicked.connect(self.w5.close)
        self.w5.show()

    def w_6(self):
        self.w6 = February()
        self.w6.nazad_label.clicked.connect(self.w_3)
        self.w6.nazad_label.clicked.connect(self.w6.close)
        self.w6.show()

    def w_7(self):
        self.w7 = Mart()
        self.w7.nazad_label.clicked.connect(self.w_3)
        self.w7.nazad_label.clicked.connect(self.w7.close)
        self.w7.show()

    def w_8(self):
        self.w8 = Aprel()
        self.w8.nazad_label.clicked.connect(self.w_3)
        self.w8.nazad_label.clicked.connect(self.w8.close)
        self.w8.show()

    def w_9(self):
        self.w9 = Mai()
        self.w9.nazad_label.clicked.connect(self.w_3)
        self.w9.nazad_label.clicked.connect(self.w9.close)
        self.w9.show()

    def w_10(self):
        self.w10 = June()
        self.w10.nazad_label.clicked.connect(self.w_3)
        self.w10.nazad_label.clicked.connect(self.w10.close)
        self.w10.show()

    def w_11(self):
        self.w11 = July()
        self.w11.nazad_label.clicked.connect(self.w_3)
        self.w11.nazad_label.clicked.connect(self.w11.close)
        self.w11.show()

    def w_12(self):
        self.w12 = Avgyst()
        self.w12.nazad_label.clicked.connect(self.w_3)
        self.w12.nazad_label.clicked.connect(self.w12.close)
        self.w12.show()

    def w_13(self):
        self.w13 = September()
        self.w13.nazad_label.clicked.connect(self.w_3)
        self.w13.nazad_label.clicked.connect(self.w13.close)
        self.w13.show()

    def w_14(self):
        self.w14 = October()
        self.w14.nazad_label.clicked.connect(self.w_3)
        self.w14.nazad_label.clicked.connect(self.w14.close)
        self.w14.show()

    def w_15(self):
        self.w15 = November()
        self.w15.nazad_label.clicked.connect(self.w_3)
        self.w15.nazad_label.clicked.connect(self.w15.close)
        self.w15.show()

    def w_16(self):
        self.w16 = December()
        self.w16.nazad_label.clicked.connect(self.w_3)
        self.w16.nazad_label.clicked.connect(self.w16.close)
        self.w16.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.w_1()
    sys.exit(app.exec_())
