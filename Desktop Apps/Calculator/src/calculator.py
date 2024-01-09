import sys
import os
from math import sqrt, sin, cos, tan, log, pi

from PySide6.QtWidgets import QApplication , QMainWindow, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QShortcut

# Import the UI from the file compiled by pyside6-uic
from form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adjustSize()

        # Number Buttons
        self.ui.zeroButton.clicked.connect(lambda: self.write("0"))
        self.ui.oneButton.clicked.connect(lambda: self.write("1"))
        self.ui.twoButton.clicked.connect(lambda: self.write("2"))
        self.ui.threeButton.clicked.connect(lambda: self.write("3"))
        self.ui.fourButton.clicked.connect(lambda: self.write("4"))
        self.ui.fiveButton.clicked.connect(lambda: self.write("5"))
        self.ui.sixButton.clicked.connect(lambda: self.write("6"))
        self.ui.sevenButton.clicked.connect(lambda: self.write("7"))
        self.ui.eightButton.clicked.connect(lambda: self.write("8"))
        self.ui.nineButton.clicked.connect(lambda: self.write("9"))

        # Operator Buttons
        self.ui.decimalButton.clicked.connect(lambda: self.write("."))
        self.ui.negativeButton.clicked.connect(lambda: self.write(" - "))
        self.ui.divideButton.clicked.connect(lambda: self.write(" ÷ "))
        self.ui.multiplyButton.clicked.connect(lambda: self.write(" x "))
        self.ui.addButton.clicked.connect(lambda: self.write(" + "))
        self.ui.openParenthesisButton.clicked.connect(lambda: self.write("("))
        self.ui.closeParenthesisButton.clicked.connect(lambda: self.write(")"))
        self.ui.powerButton.clicked.connect(lambda: self.write("^"))
        self.ui.squareRootButton.clicked.connect(lambda: self.write("√("))
        self.ui.sinButton.clicked.connect(lambda: self.write("sin("))
        self.ui.cosButton.clicked.connect(lambda: self.write("cos("))
        self.ui.tanButton.clicked.connect(lambda: self.write("tan("))
        self.ui.logButton.clicked.connect(lambda: self.write("ln("))
        self.ui.piButton.clicked.connect(lambda: self.write("π"))

        # Other Buttons
        self.ui.deleteButton.clicked.connect(self.delete)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.equalsButton.clicked.connect(self.calculate)

        # Keyboard Shortcuts
        self.ui.zeroButton.setShortcut("0")
        self.ui.oneButton.setShortcut("1")
        self.ui.twoButton.setShortcut("2")
        self.ui.threeButton.setShortcut("3")
        self.ui.fourButton.setShortcut("4")
        self.ui.fiveButton.setShortcut("5")
        self.ui.sixButton.setShortcut("6")
        self.ui.sevenButton.setShortcut("7")
        self.ui.eightButton.setShortcut("8")
        self.ui.nineButton.setShortcut("9")
        self.ui.decimalButton.setShortcut(".")
        self.ui.negativeButton.setShortcut("-")
        self.ui.divideButton.setShortcut("/")
        self.ui.multiplyButton.setShortcut("*")
        self.ui.addButton.setShortcut("+")
        self.ui.deleteButton.setShortcut("Backspace")
        self.ui.clearButton.setShortcut("Escape")
        self.ui.openParenthesisButton.setShortcut("(")
        self.ui.closeParenthesisButton.setShortcut(")")
        self.ui.powerButton.setShortcut("^")
        # Both 'Enter' and 'Return' keys are bound to the equals button
        QShortcut("Enter", self.ui.equalsButton, self.ui.equalsButton.click)
        QShortcut("Return", self.ui.equalsButton, self.ui.equalsButton.click)

    # Remove last character
    def delete(self):
        label = self.ui.scrollAreaWidgetContents.layout().itemAt(self.ui.scrollAreaWidgetContents.layout().count()-1).widget()
        label.setText(label.text()[:-1])
        QTimer.singleShot(1, self.scroll_end)

    # Clear all
    def clear(self):
        for i in reversed(range(self.ui.scrollAreaWidgetContents.layout().count())):
            self.ui.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)
        self.add_line()
    
    # Add text to the last line
    def write(self, text):
        label = self.ui.scrollAreaWidgetContents.layout().itemAt(self.ui.scrollAreaWidgetContents.layout().count()-1).widget()
        label.setText(label.text() + text)
        QTimer.singleShot(1, self.scroll_end)

    # Add new line
    def add_line(self, text=" "):
        label = QLabel()
        label.setText(text)
        label.setAlignment(Qt.AlignRight)
        self.ui.scrollAreaWidgetContents.layout().addWidget(label)
        QTimer.singleShot(1, self.scroll_end)

    # Scroll to the end
    def scroll_end(self):
        x = self.ui.scrollArea.horizontalScrollBar().maximum()
        self.ui.scrollArea.horizontalScrollBar().setValue(x)
        y = self.ui.scrollArea.verticalScrollBar().maximum()
        self.ui.scrollArea.verticalScrollBar().setValue(y)

    # Calculate the result
    def calculate(self):
        label = self.ui.scrollAreaWidgetContents.layout().itemAt(self.ui.scrollAreaWidgetContents.layout().count()-1).widget()
        text = label.text()
        text = text.replace("x", "*")
        text = text.replace("÷", "/")
        text = text.replace("=", "")
        text = text.replace("√", "sqrt")
        text = text.replace("^", "**")
        text = text.replace("ln", "log")
        text = text.replace("π", "pi")        
        try:
            result = eval(text)
            self.add_line(f"=\t{result}")
        except:
            self.add_line(f"Error")
            self.add_line()

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Used to set the icon for the executable
    icon_path = os.path.join(sys._MEIPASS, 'icon.ico') if hasattr(sys, '_MEIPASS') else 'icon.ico'
    app.setWindowIcon(QIcon(icon_path))
    widget = MainWindow()
    widget.setWindowTitle('Calculator')
    widget.show()
    sys.exit(app.exec())

    # To compile the app, run the following command in the terminal:
    # pyinstaller calculator.spec
    # The spec file in this folder contains the configuration for this executable
    # The final executable will be in the resulting dist folder

