from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondary(object):
    def setupUi(self, secondary,Mian):
        secondary.setObjectName("secondary")
        secondary.resize(459, 182)
        self.label = QtWidgets.QLabel(secondary)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hideMainButton = QtWidgets.QPushButton(secondary,clicked = lambda: self.hideMain(Mian))
        self.hideMainButton.setGeometry(QtCore.QRect(30, 110, 101, 51))
        self.hideMainButton.setObjectName("hideMainButton")
        self.hideThisButton_2 = QtWidgets.QPushButton(secondary, clicked = lambda: self.hideThis(secondary,Mian))
        self.hideThisButton_2.setGeometry(QtCore.QRect(180, 110, 101, 51))
        self.hideThisButton_2.setObjectName("hideThisButton_2")
        self.showMainButton_3 = QtWidgets.QPushButton(secondary, clicked = lambda: self.showMain(Mian))
        self.showMainButton_3.setGeometry(QtCore.QRect(330, 110, 101, 51))
        self.showMainButton_3.setObjectName("showMainButton_3")

        self.retranslateUi(secondary)
        QtCore.QMetaObject.connectSlotsByName(secondary)

    # function space
    def hideThis(self,secondW,Mian):
        secondW.hide()
        Mian.show()

    def showMain(self, Mian):
        Mian.show()

    def hideMain(self, Mian):
        Mian.hide()

    def retranslateUi(self, secondary):
        _translate = QtCore.QCoreApplication.translate
        secondary.setWindowTitle(_translate("secondary", "Dialog"))
        self.label.setText(_translate("secondary", "TextLabel"))
        self.hideMainButton.setText(_translate("secondary", "Hide Main"))
        self.hideThisButton_2.setText(_translate("secondary", "Hide This"))
        self.showMainButton_3.setText(_translate("secondary", "Show Main"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondary = QtWidgets.QDialog()
    ui = Ui_secondary()
    ui.setupUi(secondary)
    secondary.show()
    sys.exit(app.exec_())
