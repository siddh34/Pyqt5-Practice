import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Form 1")

        # seting the window
        # self.setLayout(qtw.QVBoxLayout())
        # for form we do it as below
        formLayout = qtw.QFormLayout()
        self.setLayout(formLayout)

        # Labels
        label1 = qtw.QLabel("This is a form")
        label1.setFont(qtg.QFont("Helvectica",26))

        # form widgets
        firstName = qtw.QLineEdit(self)
        lastName = qtw.QLineEdit(self)

        # adding widgets to form
        formLayout.addRow(label1)
        formLayout.addRow("Enter your FIRST NAME : ",firstName)
        formLayout.addRow("Enter your LAST NAME : ",lastName)
        formLayout.addRow(qtw.QPushButton("Press me!",clicked=lambda: pressed()))
        
        # function space
        def pressed():
            label1.setText(f"You Pressed the button, {firstName.text()} {lastName.text()}")
            firstName.clear()
            lastName.clear()



        #show the app
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()

