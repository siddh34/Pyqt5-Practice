from sys import prefix
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# Entry box

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI") #sets the title
        self.setLayout(qtw.QVBoxLayout()) #set vertical layout

        # creating a label
        my_label = qtw.QLabel("Spin Box Tutorial")
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        # creating an spin box(QSpinBox)
        # for Doubles we can use QDoubleSpinBox
        mySpinBox = qtw.QDoubleSpinBox(
            self,
            value=10.5,
            minimum=0,
            maximum=100,
            singleStep=5.7,
            suffix=' Order'
        )
        self.layout().addWidget(mySpinBox)

        # button
        myButton = qtw.QPushButton("Press me!",clicked= lambda: pressed())
        self.layout().addWidget(myButton)

        self.show()

        # function space
        def pressed():
            my_label.setText(f"You Picked {mySpinBox.value()} Order!!")
            

app = qtw.QApplication([])
mw = mainWindow()

#run the app
app.exec_()