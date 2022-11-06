from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 100, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(5, "")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.clicker())
        self.submitButton.setGeometry(QtCore.QRect(460, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # making combobox clickable
        self.comboBox.activated.connect(self.clicker)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicker(self):
        self.label.setText(f'{self.comboBox.currentText()}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Item From Combo Box"))
        self.comboBox.setItemText(0, _translate("MainWindow", "peperoni"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cheeze"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Everthing"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Something New"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Tomatoes"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
