from PyQt5 import QtCore, QtWidgets
from connectHide2 import Ui_secondary
# from connect2 import Ui_secondary

class Ui_Mian(object):
    # opening a second window
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_secondary()
        self.ui.setupUi(self.window,Mian)
        self.window.show()
        # Mian.hide()

    def setupUi(self, Mian):
        Mian.setObjectName("Main")
        Mian.resize(372, 374)
        self.submitButton = QtWidgets.QPushButton(Mian,clicked = lambda: self.clicker())
        self.submitButton.setGeometry(QtCore.QRect(10, 210, 351, 61))
        self.submitButton.setObjectName("submitButton")
        self.openButton = QtWidgets.QPushButton(Mian,clicked = lambda: self.openWindow())
        self.openButton.setGeometry(QtCore.QRect(10, 290, 351, 61))
        self.openButton.setObjectName("openButton")
        self.lineEdit = QtWidgets.QLineEdit(Mian)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 351, 191))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Mian)
        QtCore.QMetaObject.connectSlotsByName(Mian)

    # function space
    def clicker(self):
        line = self.lineEdit.text()
        # assign things to second window
        self.openWindow()
        self.ui.label.setText(f"{line}")

    def retranslateUi(self, Mian):
        _translate = QtCore.QCoreApplication.translate
        Mian.setWindowTitle(_translate("Mian", "Dialog"))
        self.submitButton.setText(_translate("Mian", "Submit"))
        self.openButton.setText(_translate("Mian", "Open Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mian = QtWidgets.QDialog()
    ui = Ui_Mian()
    ui.setupUi(Mian)
    Mian.show()
    sys.exit(app.exec_())
