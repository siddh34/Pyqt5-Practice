from PyQt5 import QtCore, QtGui, QtWidgets
# from window2 import Ui_secondWindow
from window3 import Ui_Dialog

class Ui_MainWindow(object):
    # second Window
    def openWindow(self):
        # for main window2
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_secondWindow()
        # self.ui.setupUi(self.window)
        # self.window.show()
        
        # for dialog box (Window 3)
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget, clicked = self.openWindow)
        self.openButton.setGeometry(QtCore.QRect(40, 40, 301, 131))
        self.openButton.setObjectName("openButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
