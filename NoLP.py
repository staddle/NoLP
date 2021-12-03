from pynput import keyboard
import threading
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
        self.btn.move(300,0)
        self.exbtn=QPushButton(self)
        self.exbtn.setText("Exit Program")
        self.exbtn.clicked.connect(lambda:on_exit())
        self.show()

shown = False

class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
 
        # helper function to execute the threads
    def run(self):
        print(str(self.thread_name) +" "+ str(self.thread_ID));
        app = QApplication(sys.argv)     
        w = mymainwindow()
        app.exec_()

def on_activate():
    print('pressed')
    thread1 = thread("keyb", 1000)
    thread1.start()
    print('pressed2')
    
def on_exit():
    print("exiting")
    sys.exit();

def for_canonical(f):
    return lambda k: f(l.canonical(k))

with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+d': on_activate, 
        '<ctrl>+<shift>+e': on_exit}) as h:
    h.join()
