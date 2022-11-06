from inspect import classify_class_attrs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
import sqlite3 as sq

# database connection code
connection = sq.connect("MyList.db")

# create a cursor
cur = connection.cursor()

# create table
cur.execute(""" CREATE TABLE if not exists MyTodoTable(
    listItem text
) """)

# commit the changes
connection.commit()

# connection closed
connection.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.addIt())
        self.addButton.setGeometry(QtCore.QRect(30, 50, 91, 41))
        self.addButton.setObjectName("addButton")
        self.DeleteAnItemButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.deleteIt())
        self.DeleteAnItemButton.setGeometry(QtCore.QRect(150, 50, 93, 41))
        self.DeleteAnItemButton.setObjectName("DeleteAnItemButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clearIt())
        self.clearButton.setGeometry(QtCore.QRect(270, 50, 93, 41))
        self.clearButton.setObjectName("clearButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(30, 110, 451, 261))
        self.my_listWidget.setObjectName("my_listWidget")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.saveIt())
        self.SaveButton.setGeometry(QtCore.QRect(380, 50, 93, 41))
        self.SaveButton.setObjectName("SaveButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.grabIt()

    # Function Space

    def grabIt(self):
        # connect to db
        connection = sq.connect("MyList.db")
        # make a cursor
        cur = connection.cursor()
        # excute 
        cur.execute("SELECT * FROM MyTodoTable")
        records = cur.fetchall()
        # commit
        connection.commit()
        # close
        connection.close()

        # looping through records
        for record in records:
            self.my_listWidget.addItem(str(record[0]))



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

    # saving the data in database
    def saveIt(self):
        # connect
        connection = sq.connect("MyList.db")
        # cursor 
        cur = connection.cursor()
        # delete from database (Previous values)
        cur.execute("Delete from MyTodoTable;",)
        items = []
        # taking items for list widget
        for index in range(self.my_listWidget.count()):
            items.append(self.my_listWidget.item(index).text())
        
        for item in items:
            cur.execute("INSERT INTO MyTodoTable VALUES (:item)",
                {
                    'item': item,
                }
            )
        # commit the changes
        connection.commit()
        # close the connection
        connection.close()
        # msg box
        msg = QMessageBox()
        msg.setWindowTitle("Save changed to database!!")
        msg.setText("Your TodoList has been saved successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.DeleteAnItemButton.setText(_translate("MainWindow", "Delete an Item"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.DeleteAnItemButton.setText(_translate("MainWindow", "Delete an Item"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
