from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
            super(UI, self).__init__()

            # load ui
            uic.loadUi("load.ui", self)
            
            # def widgets
            self.textedit = self.findChild(QTextEdit,"textEdit")
            self.label = self.findChild(QLabel,"label")
            self.button = self.findChild(QPushButton,"Submit")
            self.clearButton = self.findChild(QPushButton,"Reset")

            # do something
            self.button.clicked.connect(self.clicker)
            self.clearButton.clicked.connect(self.clear)

            # show the app
            self.show()
    
    # doer function
    def clicker(self):
        self.label.setText(f"Hello there... {self.textedit.toPlainText()}")
        self.textedit.setText("")

    def clear(self):
        self.label.setText(f"Enter your name... ")
        self.textedit.setText("")

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()