from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondary(object):
    def setupUi(self, secondary):
        secondary.setObjectName("secondary")
        secondary.resize(481, 97)
        self.label = QtWidgets.QLabel(secondary)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(secondary)
        QtCore.QMetaObject.connectSlotsByName(secondary)

    def retranslateUi(self, secondary):
        _translate = QtCore.QCoreApplication.translate
        secondary.setWindowTitle(_translate("secondary", "Dialog"))
        self.label.setText(_translate("secondary", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondary = QtWidgets.QDialog()
    ui = Ui_secondary()
    ui.setupUi(secondary)
    secondary.show()
    sys.exit(app.exec_())
