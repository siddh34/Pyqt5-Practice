from PyQt5.QtWidgets import QMainWindow, QApplication ,QComboBox, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # load the file
        uic.loadUi("dependantComboBox.ui",self)

        # variables
        self.combox1 = self.findChild(QComboBox,"comboBox")
        self.combox2 = self.findChild(QComboBox,"comboBox_2")
        self.label = self.findChild(QLabel,"label")

        # add to combo 
        self.combox1.addItem("Male",["Wes","John","Dan"])
        self.combox1.addItem("Female",["April","Step","Beth"])
        
        self.combox1.activated.connect(self.clicker)
        self.combox2.activated.connect(self.clicker2)
        # show the app
        self.show()
    def clicker(self):
        self.combox2.clear()
        self.combox2.addItems(self.combox1.itemData(self.combox1.currentIndex()))
    def clicker2(self):
        self.label.setText(f"You Picked .... {self.combox1.currentText()} - {self.combox2.currentText()}")

# initialize the app
app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()
