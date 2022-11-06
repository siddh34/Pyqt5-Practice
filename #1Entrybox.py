import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# Entry box

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI") #sets the title
        self.setLayout(qtw.QVBoxLayout()) #set vertical layout

        # creating a label
        my_label = qtw.QLabel("Whats your name?")
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        # creating an entry box
        myEntryBox = qtw.QLineEdit()
        myEntryBox.setObjectName("My Entry Field")
        myEntryBox.setText("")
        self.layout().addWidget(myEntryBox)

        # button
        myButton = qtw.QPushButton("Press me!",clicked= lambda: pressed())
        self.layout().addWidget(myButton)

        self.show()

        # function space
        def pressed():
            my_label.setText(f"Hello {myEntryBox.text()}")
            # clearing the entry box
            myEntryBox.setText("")

app = qtw.QApplication([])
mw = mainWindow()

#run the app
app.exec_()