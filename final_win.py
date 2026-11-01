from PYQt5.QtCore import Qt, QTimer, QTime, QLocale
from math import exp
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        pass

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
