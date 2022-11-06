import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# combo boxes

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI") #sets the title
        self.setLayout(qtw.QVBoxLayout()) #set vertical layout

        # creating a label
        my_label = qtw.QLabel("Whats your name?")
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        # combo box
        mycombo = qtw.QComboBox(self,editable=True,insertPolicy=qtw.QComboBox.InsertAtBottom)
        mycombo.addItem("Pizza", 1)
        mycombo.addItem("Chai", 2)
        mycombo.addItem("Sabji", 3)
        mycombo.addItem("Wafers", 4)
        mycombo.insertItems(1,["one","two","Three"])
        self.layout().addWidget(mycombo)

        # button
        myButton = qtw.QPushButton("Press me!",clicked= lambda: pressed())
        self.layout().addWidget(myButton)

        self.show()

        # function space
        def pressed():
            my_label.setText(f"You Picked : {mycombo.currentData()}")

app = qtw.QApplication([])
mw = mainWindow()

#run the app
app.exec_()