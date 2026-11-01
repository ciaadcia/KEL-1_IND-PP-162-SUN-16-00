from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
class TestWin(QWidgets):
  def __init__(self):
    super().__init__()
    self.initUI()
    self.set_appear()
    self.show()

  def initUI(self):
    self.btn_next = QPushButton(txt_sendresults, self)
    self.btn_next.clicked.connect(self.next_click)
    layout = QVBoxLayout()
    layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
    self.setLayout(layout)
  def next_click(self):
    self.hide()
    self.fw = FinalWin()
  def set_appear(self):
    self.setWindowTittle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
