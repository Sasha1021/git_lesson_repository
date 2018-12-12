import sys

import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class Dnevnik(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Дневник огородника')
        self.initUI()

    def initUI(self):
        self.nazvanie_label = QLabel(self)
        self.nazvanie_label.setText("Дневник огородника")
        self.nazvanie_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.nazvanie_label.move(55, 20)

        self.soderj_label = QLabel(self)
        self.soderj_label.setText("Содержание")
        self.soderj_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.soderj_label.move(130, 50)

        self.lyna_label = QLabel(self)
        self.lyna_label = QPushButton("Лунный календарь", self)
        self.lyna_label.show()
        self.lyna_label.move(10, 115)

        self.plan_label = QLabel(self)
        self.plan_label = QPushButton("План посадки", self)
        self.plan_label.show()
        self.plan_label.move(10, 85)

        self.blagodni_label = QLabel(self)
        self.blagodni_label = QPushButton("Благоприятные дни для посадки", self)
        self.blagodni_label.show()
        self.blagodni_label.move(10, 145)

        self.blagorabot_label = QLabel(self)
        self.blagorabot_label = QPushButton("Наиболее благоприятные дни для проведения работ", self)
        self.blagorabot_label.show()
        self.blagorabot_label.move(10, 175)


class Plan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лунный календарь')
        self.meciz_label = QLabel(self)
        self.setGeometry(310, 260, 310, 260)
        self.meciz_label.setText("Лунный календарь 2019")
        self.meciz_label.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.meciz_label.move(25, 20)

class Lyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лунный календарь')
        self.meciz_label = QLabel(self)
        self.setGeometry(310, 260, 310, 260)
        self.meciz_label.setText("Лунный календарь 2019")
        self.meciz_label.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.meciz_label.move(25, 20)

        self.january_label = QLabel(self)
        self.january_label = QPushButton("Январь", self)
        self.january_label.show()
        self.january_label.move(10, 85)

        self.february_label = QLabel(self)
        self.february_label = QPushButton("Февраль", self)
        self.february_label.show()
        self.february_label.move(110, 85)

        self.mart_label = QLabel(self)
        self.mart_label = QPushButton("Март", self)
        self.mart_label.show()
        self.mart_label.move(210, 85)

        self.aprel_label = QLabel(self)
        self.aprel_label = QPushButton("Апрель", self)
        self.aprel_label.show()
        self.aprel_label.move(10, 120)

        self.mai_label = QLabel(self)
        self.mai_label = QPushButton("Май", self)
        self.mai_label.show()
        self.mai_label.move(110, 120)

        self.june_label = QLabel(self)
        self.june_label = QPushButton("Июнь", self)
        self.june_label.show()
        self.june_label.move(210, 120)

        self.july_label = QLabel(self)
        self.july_label = QPushButton("Июль", self)
        self.july_label.show()
        self.july_label.move(10, 155)

        self.avgyst_label = QLabel(self)
        self.avgyst_label = QPushButton("Август", self)
        self.avgyst_label.show()
        self.avgyst_label.move(110, 155)

        self.september_label = QLabel(self)
        self.september_label = QPushButton("Сентябрь", self)
        self.september_label.show()
        self.september_label.move(210, 155)

        self.october_label = QLabel(self)
        self.october_label = QPushButton("Октябрь", self)
        self.october_label.show()
        self.october_label.move(10, 190)

        self.november_label = QLabel(self)
        self.november_label = QPushButton("Ноябрь", self)
        self.november_label.show()
        self.november_label.move(110, 190)

        self.december_label = QLabel(self)
        self.december_label = QPushButton("Декабрь", self)
        self.december_label.show()
        self.december_label.move(210, 190)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(110, 225)


class January(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class February(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("2.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Mart(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("3.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Aprel(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("4.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Mai(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("5.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class June(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("6.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class July(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("7.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Avgyst(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("8.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class September(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("9.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class October(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("10.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class November(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("11.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class December(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("12.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


class Blagodni(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("14.png")


        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.nazad_label = QLabel(self)
        self.nazad_label = QPushButton("Назад", self)
        self.nazad_label.show()
        self.nazad_label.move(200, 700)


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
    def show_window_1(self):
        self.w1 = Dnevnik()
        self.w1.lyna_label.clicked.connect(self.show_window_2)
        self.w1.lyna_label.clicked.connect(self.w1.close)
        self.w1.blagodni_label.clicked.connect(self.show_window_15)
        self.w1.blagodni_label.clicked.connect(self.w1.close)
        self.w1.blagorabot_label.clicked.connect(self.show_window_16)
        self.w1.blagorabot_label.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Lyna()
        self.w2.january_label.clicked.connect(self.show_window_3)
        self.w2.january_label.clicked.connect(self.w2.close)
        self.w2.february_label.clicked.connect(self.show_window_4)
        self.w2.february_label.clicked.connect(self.w2.close)
        self.w2.mart_label.clicked.connect(self.show_window_5)
        self.w2.mart_label.clicked.connect(self.w2.close)
        self.w2.aprel_label.clicked.connect(self.show_window_6)
        self.w2.aprel_label.clicked.connect(self.w2.close)
        self.w2.mai_label.clicked.connect(self.show_window_7)
        self.w2.mai_label.clicked.connect(self.w2.close)
        self.w2.june_label.clicked.connect(self.show_window_8)
        self.w2.june_label.clicked.connect(self.w2.close)
        self.w2.july_label.clicked.connect(self.show_window_9)
        self.w2.july_label.clicked.connect(self.w2.close)
        self.w2.avgyst_label.clicked.connect(self.show_window_10)
        self.w2.avgyst_label.clicked.connect(self.w2.close)
        self.w2.september_label.clicked.connect(self.show_window_11)
        self.w2.september_label.clicked.connect(self.w2.close)
        self.w2.october_label.clicked.connect(self.show_window_12)
        self.w2.october_label.clicked.connect(self.w2.close)
        self.w2.november_label.clicked.connect(self.show_window_13)
        self.w2.november_label.clicked.connect(self.w2.close)
        self.w2.december_label.clicked.connect(self.show_window_14)
        self.w2.december_label.clicked.connect(self.w2.close)
        self.w2.nazad_label.clicked.connect(self.show_window_1)
        self.w2.nazad_label.clicked.connect(self.w2.close)
        self.w2.show()

    def show_window_3(self):
        self.w3 = January()
        self.w3.nazad_label.clicked.connect(self.show_window_2)
        self.w3.nazad_label.clicked.connect(self.w3.close)
        self.w3.show()

    def show_window_4(self):
        self.w4 = February()
        self.w4.nazad_label.clicked.connect(self.show_window_2)
        self.w4.nazad_label.clicked.connect(self.w4.close)
        self.w4.show()

    def show_window_5(self):
        self.w5 = Mart()
        self.w5.nazad_label.clicked.connect(self.show_window_2)
        self.w5.nazad_label.clicked.connect(self.w5.close)
        self.w5.show()

    def show_window_6(self):
        self.w6 = Aprel()
        self.w6.nazad_label.clicked.connect(self.show_window_2)
        self.w6.nazad_label.clicked.connect(self.w6.close)
        self.w6.show()

    def show_window_7(self):
        self.w7 = Mai()
        self.w7.nazad_label.clicked.connect(self.show_window_2)
        self.w7.nazad_label.clicked.connect(self.w7.close)
        self.w7.show()

    def show_window_8(self):
        self.w8 = June()
        self.w8.nazad_label.clicked.connect(self.show_window_2)
        self.w8.nazad_label.clicked.connect(self.w8.close)
        self.w8.show()

    def show_window_9(self):
        self.w9 = July()
        self.w9.nazad_label.clicked.connect(self.show_window_2)
        self.w9.nazad_label.clicked.connect(self.w9.close)
        self.w9.show()

    def show_window_10(self):
        self.w10 = Avgyst()
        self.w10.nazad_label.clicked.connect(self.show_window_2)
        self.w10.nazad_label.clicked.connect(self.w10.close)
        self.w10.show()

    def show_window_11(self):
        self.w11 = September()
        self.w11.nazad_label.clicked.connect(self.show_window_2)
        self.w11.nazad_label.clicked.connect(self.w11.close)
        self.w11.show()

    def show_window_12(self):
        self.w12 = October()
        self.w12.nazad_label.clicked.connect(self.show_window_2)
        self.w12.nazad_label.clicked.connect(self.w12.close)
        self.w12.show()

    def show_window_13(self):
        self.w13 = November()
        self.w13.nazad_label.clicked.connect(self.show_window_2)
        self.w13.nazad_label.clicked.connect(self.w13.close)
        self.w13.show()

    def show_window_14(self):
        self.w14 = December()
        self.w14.nazad_label.clicked.connect(self.show_window_2)
        self.w14.nazad_label.clicked.connect(self.w14.close)
        self.w14.show()

    def show_window_15(self):
        self.w15 = Blagodni()
        self.w15.nazad_label.clicked.connect(self.show_window_1)
        self.w15.nazad_label.clicked.connect(self.w15.close)
        self.w15.show()

    def show_window_16(self):
        self.w16 = Blagorabot()
        self.w16.nazad_label.clicked.connect(self.show_window_1)
        self.w16.nazad_label.clicked.connect(self.w16.close)
        self.w16.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    sys.exit(app.exec())
