from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 230, 161, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.RedCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RedCheckBox.setGeometry(QtCore.QRect(170, 50, 81, 20))
        self.RedCheckBox.setObjectName("RedCheckBox")
        self.BlueCheckBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.BlueCheckBox_2.setGeometry(QtCore.QRect(170, 110, 81, 20))
        self.BlueCheckBox_2.setObjectName("BlueCheckBox_2")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.checkedIt())
        self.SubmitButton.setGeometry(QtCore.QRect(140, 160, 131, 41))
        self.SubmitButton.setObjectName("SubmitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # default checked
        # self.RedCheckBox.setChecked(True)

    # Function space
    def checkedIt(self):
        if self.RedCheckBox.isChecked():
            self.red = "Red"
        else:
            self.red = ""
        if self.BlueCheckBox_2.isChecked():
            self.blue = "Blue"
        else:
            self.blue = ""
        if(self.RedCheckBox.isChecked() == False and self.BlueCheckBox_2.isChecked() == False):
            self.label.setText("Pick A Color")
            return
        # setting both strings at the end
        self.label.setText(f"{self.red} {self.blue}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pick A Color"))
        self.RedCheckBox.setText(_translate("MainWindow", "Red"))
        self.BlueCheckBox_2.setText(_translate("MainWindow", "Blue"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
