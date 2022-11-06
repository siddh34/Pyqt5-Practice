from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 170, 161, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.RedCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RedCheckBox.setGeometry(QtCore.QRect(170, 50, 81, 20))
        self.RedCheckBox.setObjectName("RedCheckBox")
        self.BlueCheckBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.BlueCheckBox_2.setGeometry(QtCore.QRect(170, 110, 81, 20))
        self.BlueCheckBox_2.setObjectName("BlueCheckBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # update the button
        self.RedCheckBox.toggled.connect(lambda: self.buttonState())
        self.BlueCheckBox_2.toggled.connect(lambda: self.buttonState())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # function space
    def buttonState(self):
        if self.RedCheckBox.isChecked() == True:
            self.red = "Red"
        else: 
            self.red = ""
        if self.BlueCheckBox_2.isChecked() == True:
            self.blue = "Blue"
        else:
            self.blue = ""
        
        self.label.setText(f"{self.red} {self.blue}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pick A Color"))
        self.RedCheckBox.setText(_translate("MainWindow", "Red"))
        self.BlueCheckBox_2.setText(_translate("MainWindow", "Blue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
