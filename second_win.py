# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from final_win import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.next_click
    def set_appear(self):
        self.setWindowTitle(window_name)
    
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.btn_name = QLabel(txt_name)
        self.l_line.addWidget(self.btn_name, alignment = Qt.AlignLeft)
        self.btn_hintname = QLineEdit(txt_hintname)
        self.l_line.addWidget(self.btn_hintname, alignment = Qt.AlignLeft)
        self.btn_age = QLabel(txt_age)
        self.l_line.addWidget(self.btn_age, alignment = Qt.AlignLeft)
        self.btn_hintage = QLineEdit(txt_hintage)
        self.l_line.addWidget(self.btn_hintage, alignment = Qt.AlignLeft)
        self.btn_test1 = QLabel(txt_test1)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)

        self.btn_timer1 = QPushButton(txt_starttest1)
        self.l_line.addWidget(self.btn_timer1, alignment = Qt.AlignLeft)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.l_line.addWidget(self.txt_hinttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test2), alignment = Qt.AlignLeft)
        
        self.btn_timer2 = QPushButton(txt_starttest2)
        self.l_line.addWidget(self.btn_timer2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(QLabel(txt_test3), alignment = Qt.AlignLeft)
        self.btn_timer3 = QPushButton(txt_starttest3)
        self.l_line.addWidget(self.btn_timer3, alignment = Qt.AlignLeft)

        self.btn_hinttest2 = QLineEdit(txt_hinttest2)
        self.l_line.addWidget(self.btn_hinttest2, alignment = Qt.AlignLeft)
        self.btn_hinttest3 = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.btn_hinttest3, alignment = Qt.AlignLeft)

        self.btn_next = QPushButton(txt_sendresults)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        
        

        self.text_timer = QLabel()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_timer1.clicked.connect(self.timer_test)
        self.btn_timer2.clicked.connect(self.timer_sits)
        self.btn_timer3.clicked.connect(self.timer_final)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.btn_hintname.text(), self.txt_hinttest1.text(), self.btn_hinttest2.text(), self.btn_hinttest3.text())
        self.tw = FinalWin(self.exp) 
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
app = QApplication([])
a = TestWin()
app.exec_()