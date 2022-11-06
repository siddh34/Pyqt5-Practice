from itertools import count
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 143)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget,clicked = lambda: self.increment())
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 40, 222, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.Numberlabel = QtWidgets.QLabel(self.centralwidget)
        self.Numberlabel.setGeometry(QtCore.QRect(320, 40, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Numberlabel.setFont(font)
        self.Numberlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Numberlabel.setObjectName("Numberlabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # function space
    def increment(self):
        self.count += 1
        # setting output as number
        self.Numberlabel.setText(str(self.count))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))
        self.Numberlabel.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
