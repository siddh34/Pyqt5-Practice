from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.push1())
        self.Button1.setGeometry(QtCore.QRect(22, 27, 211, 91))
        self.Button1.setObjectName("Button1")
        self.ClearStatusBar = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.clearStatus())
        self.ClearStatusBar.setGeometry(QtCore.QRect(280, 27, 211, 91))
        self.ClearStatusBar.setDefault(False)
        self.ClearStatusBar.setFlat(False)
        self.ClearStatusBar.setObjectName("ClearStatusBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # function space

    def push1(self):
        self.statusbar.showMessage("You have pressed Button1")

    def clearStatus(self):
        self.statusbar.clearMessage()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "Button 1"))
        self.ClearStatusBar.setText(_translate("MainWindow", "Clear Status Bar "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
