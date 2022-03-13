import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QPlainTextEdit, QRadioButton, QButtonGroup
from PyQt5 import QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x, y = 100, 100
        self.setGeometry(500, 300, 240, 400)
        self.setWindowTitle('Калькулятор')

        generate = [7, 8, 9, '/', 4, 5, 6, '*', 1, 2, 3, '-', "C", 0, "CE", '+', ".", "\u00B1"]
        x, y = 0, 100

        for gen in generate:
            if x > 200:
                x = 0
                y += 60
            self.button = QPushButton(self)
            self.button.setText(str(gen))
            self.button.setGeometry(x, y, 60, 60)
            self.button.clicked.connect(self.calc)
            x += 60

        self.button = QPushButton(self)
        self.button.setText('=')
        self.button.setGeometry(120, 340, 120, 60)
        self.button.clicked.connect(self.calc)

        self.display = QLabel(self)
        self.display.setGeometry(0, 30, 240, 70)

        self.display2 = QLabel(self)
        self.display2.setGeometry(0, 0, 240, 30)

    def calc(self):
        self.display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont('Arial', 20))
        self.display2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.display2.setFont(QFont('Arial', 12))
        if self.sender().text() in '0123456789':
            if "ERROR" in self.display.text():
                self.display2.setText("")
                self.display.setText(self.sender().text())
            else:
                self.display.setText(self.display.text() + self.sender().text())
        elif self.sender().text() == "CE":
            self.display.setText("")
            self.display2.setText("")
        elif self.sender().text() in '/*-+':
            if self.display2.text() != '' and self.display.text() == '':
                if self.display2.text()[-1] in '/*-+':
                    self.display2.setText(f'{self.display2.text()[:-1]}{self.sender().text()}')

            if self.display.text() != "":
                self.display2.setText(f'{self.display2.text()} {self.display.text()} {self.sender().text()}')
                self.display.setText("")

        elif self.sender().text() == '=':
            if self.display.text() != '':
                if '/0' in self.display2.text() + self.display.text():
                    self.display.setText("ERROR")
                else:
                    self.display.setText(str(eval(self.display2.text() + self.display.text())))
                    self.display2.setText('')
        elif self.sender().text() == '.':
            if '.' not in self.display.text() and self.display.text() != "":
                self.display.setText(self.display.text() + self.sender().text())

        elif self.sender().text() == 'C':
            self.display.setText("")

        if self.sender().text() == '\u00B1':
            if self.display.text() != '':
                if self.display.text()[0] == '-':
                    self.display.setText(f"{self.display.text()[1:]}")
                else:
                    self.display.setText(f"-{self.display.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
