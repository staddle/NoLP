from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class mymainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        b = QLabel(self)
        b.setText("No LP peeking!")
        self.setGeometry(1000,200,400,400)
        b.move(170,170)
        self.setWindowTitle("NoLP")
        self.btn=QPushButton(self)
        self.btn.setText("Close")
        self.btn.clicked.connect(lambda:self.close())
        self.show()
        
app = QApplication(sys.argv)     
w = mymainwindow()
app.exec_()