import sys
from math import sqrt, sin, cos, tan, log, pi

from PySide6.QtWidgets import QApplication , QMainWindow, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

from form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adjustSize()

        self.ui.pushButton.clicked.connect(lambda: self.write("0"))
        self.ui.pushButton_2.clicked.connect(lambda: self.write("1"))
        self.ui.pushButton_3.clicked.connect(lambda: self.write("2"))
        self.ui.pushButton_4.clicked.connect(lambda: self.write("3"))
        self.ui.pushButton_5.clicked.connect(lambda: self.write("4"))
        self.ui.pushButton_6.clicked.connect(lambda: self.write("5"))
        self.ui.pushButton_7.clicked.connect(lambda: self.write("6"))
        self.ui.pushButton_8.clicked.connect(lambda: self.write("7"))
        self.ui.pushButton_9.clicked.connect(lambda: self.write("8"))
        self.ui.pushButton_10.clicked.connect(lambda: self.write("9"))

        self.ui.pushButton_11.clicked.connect(lambda: self.write("."))
        self.ui.pushButton_12.clicked.connect(lambda: self.write("-"))
        self.ui.pushButton_13.clicked.connect(lambda: self.write("÷"))
        self.ui.pushButton_14.clicked.connect(lambda: self.write("x"))
        self.ui.pushButton_15.clicked.connect(lambda: self.write("+"))

        self.ui.pushButton_16.clicked.connect(self.delete)
        self.ui.pushButton_17.clicked.connect(self.clear)
        self.ui.pushButton_18.clicked.connect(self.calculate)

        self.ui.pushButton_19.clicked.connect(lambda: self.write("("))
        self.ui.pushButton_20.clicked.connect(lambda: self.write(")"))
        self.ui.pushButton_21.clicked.connect(lambda: self.write("^"))
        self.ui.pushButton_22.clicked.connect(lambda: self.write("√("))
        self.ui.pushButton_23.clicked.connect(lambda: self.write("sin("))
        self.ui.pushButton_24.clicked.connect(lambda: self.write("cos("))
        self.ui.pushButton_25.clicked.connect(lambda: self.write("tan("))
        self.ui.pushButton_26.clicked.connect(lambda: self.write("ln("))
        self.ui.pushButton_27.clicked.connect(lambda: self.write("π"))

        self.ui.pushButton.setShortcut("0")
        self.ui.pushButton_2.setShortcut("1")
        self.ui.pushButton_3.setShortcut("2")
        self.ui.pushButton_4.setShortcut("3")
        self.ui.pushButton_5.setShortcut("4")
        self.ui.pushButton_6.setShortcut("5")
        self.ui.pushButton_7.setShortcut("6")
        self.ui.pushButton_8.setShortcut("7")
        self.ui.pushButton_9.setShortcut("8")
        self.ui.pushButton_10.setShortcut("9")
        self.ui.pushButton_11.setShortcut(".")
        self.ui.pushButton_12.setShortcut("-")
        self.ui.pushButton_13.setShortcut("/")
        self.ui.pushButton_14.setShortcut("*")
        self.ui.pushButton_15.setShortcut("+")
        self.ui.pushButton_16.setShortcut("Backspace")
        self.ui.pushButton_17.setShortcut("Escape")
        self.ui.pushButton_18.setShortcut("Return")
        self.ui.pushButton_19.setShortcut("(")
        self.ui.pushButton_20.setShortcut(")")
        self.ui.pushButton_21.setShortcut("^")

    def delete(self):
        label = self.ui.scrollAreaWidgetContents.layout().itemAt(self.ui.scrollAreaWidgetContents.layout().count()-1).widget()
        label.setText(label.text()[:-1])
        QTimer.singleShot(1, self.scroll_end)

    def clear(self):
        for i in reversed(range(self.ui.scrollAreaWidgetContents.layout().count())):
            self.ui.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)
        self.add_line()
    
    def write(self, text):
        label = self.ui.scrollAreaWidgetContents.layout().itemAt(self.ui.scrollAreaWidgetContents.layout().count()-1).widget()
        label.setText(label.text() + text)
        QTimer.singleShot(1, self.scroll_end)

    def add_line(self, text=" "):
        label = QLabel()
        label.setText(text)
        label.setAlignment(Qt.AlignRight)
        self.ui.scrollAreaWidgetContents.layout().addWidget(label)
        QTimer.singleShot(1, self.scroll_end)

    def scroll_end(self):
        x = self.ui.scrollArea.horizontalScrollBar().maximum()
        self.ui.scrollArea.horizontalScrollBar().setValue(x)
        y = self.ui.scrollArea.verticalScrollBar().maximum()
        self.ui.scrollArea.verticalScrollBar().setValue(y)

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
            self.add_line(f" = {result}")
        except:
            self.add_line(f"Error")
            self.add_line()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle('Calculator')
    widget.setWindowIcon(QIcon('icon.ico'))
    widget.show()
    sys.exit(app.exec())
