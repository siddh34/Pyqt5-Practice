from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 399)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Peperoni = QtWidgets.QRadioButton(self.centralwidget)
        self.Peperoni.setGeometry(QtCore.QRect(230, 50, 95, 31))
        self.Peperoni.setObjectName("Peperoni")
        self.Cheese = QtWidgets.QRadioButton(self.centralwidget)
        self.Cheese.setGeometry(QtCore.QRect(230, 110, 95, 31))
        self.Cheese.setObjectName("Cheese")
        self.new_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(230, 170, 161, 31))
        self.new_2.setObjectName("new_2")
        self.Submit = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.selectIt())
        self.Submit.setGeometry(QtCore.QRect(200, 220, 161, 41))
        self.Submit.setObjectName("Submit")
        self.Display = QtWidgets.QLabel(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(140, 280, 301, 41))
        self.Display.setAlignment(QtCore.Qt.AlignCenter)
        self.Display.setObjectName("Display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set default button checked 
        self.Peperoni.setChecked(True)

    # function space
    def selectIt(self):
        if self.Peperoni.isChecked():
            self.Display.setText("Peperoni")
            self.Peperoni.setText("Marked")
        elif self.Cheese.isChecked():
            self.Display.setText(self.Cheese.text())
            self.Cheese.setText("Marked")
        elif self.new_2.isChecked():
            self.Display.setText("New")
            self.new_2.setText("Marked")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Peperoni.setText(_translate("MainWindow", "Peperoni"))
        self.Cheese.setText(_translate("MainWindow", "Cheese"))
        self.new_2.setText(_translate("MainWindow", "Something New"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.Display.setText(_translate("MainWindow", "Choose Something to display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
