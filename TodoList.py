from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.addIt())
        self.addButton.setGeometry(QtCore.QRect(30, 50, 91, 41))
        self.addButton.setObjectName("addButton")
        self.DeleteAnItemButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.deleteIt())
        self.DeleteAnItemButton.setGeometry(QtCore.QRect(160, 50, 93, 41))
        self.DeleteAnItemButton.setObjectName("DeleteAnItemButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.clearIt())
        self.clearButton.setGeometry(QtCore.QRect(280, 50, 93, 41))
        self.clearButton.setObjectName("clearButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(30, 110, 351, 261))
        self.my_listWidget.setObjectName("my_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    # Function Space
    def addIt(self):
        # taking what's in the window
        item = self.lineEdit.text()
        #adding the item in the list
        self.my_listWidget.addItem(item)
        #clearing the item box
        self.lineEdit.setText("")

    # deleting the item in the list
    def deleteIt(self):
        # grab the current row
        clicked = self.my_listWidget.currentRow()
        # delete
        self.my_listWidget.takeItem(clicked)

    # clearing the list
    def clearIt(self):
        self.my_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.DeleteAnItemButton.setText(_translate("MainWindow", "Delete an Item"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
