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
        myText = qtw.QTextEdit(
            self,
            # html="<h1><em>Enter Something</em></h1>",
            acceptRichText=True,
            lineWrapMode=True,
            lineWrapColumnOrWidth=50,
            placeholderText='Enter Something',
            readOnly=False
        )
        self.layout().addWidget(myText)

        # button
        myButton = qtw.QPushButton("Press me!",clicked= lambda: pressed())
        self.layout().addWidget(myButton)

        self.show()

        # function space
        def pressed():
            my_label.setText(f"You Typed {myText.toPlainText()}")
            myText.setPlainText("You Pressed the button!")
            

app = qtw.QApplication([])
mw = mainWindow()

#run the app
app.exec_()