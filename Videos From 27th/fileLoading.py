from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load the file
        uic.loadUi("openAFile.ui",self)

        # variables
        self.button = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel,"label")

        self.button.clicked.connect(self.clicker)

        # show the app
        self.show()
    def clicker(self):
        #self.label.setText("You clicked the button")
        fname = QFileDialog.getOpenFileName(self,"Open File","d:\\","All Files(*);;Python FIles (*.py)")
        if fname:
            self.label.setText(f"Directory : {fname[0]}")


app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()