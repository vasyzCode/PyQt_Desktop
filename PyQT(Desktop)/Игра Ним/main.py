import sys

import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QPlainTextEdit, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 400, 400)
        self.setWindowTitle('Калькулятор')

        self.first_button_generate = random.randint(1, 10)

        self.second_button_generate = random.randint(1, 10)
        while self.second_button_generate == self.first_button_generate:
            self.second_button_generate = random.randint(1, 10)

        self.result = QLabel(self)
        self.result.setGeometry(10, 10, 400, 40)
        self.result.setText("Вы победили, начинаем новую игру")

        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 100, 125, 40)
        self.button1.setText(f"+{self.first_button_generate}")
        self.button1.clicked.connect(self.first_button)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(225, 100, 125, 40)
        self.button2.setText(f"-{self.second_button_generate}")
        self.button2.clicked.connect(self.second_button)

        self.ost = QLabel(self)
        self.ost.setGeometry(10, 150, 400, 40)
        self.ost.setText("Осталось ходов")

        self.chisl = QLabel(self)
        self.chisl.setGeometry(10, 200, 400, 40)
        self.chisl.setText("Текущее число")

        self.display_ost = QLCDNumber(self)
        self.display_ost.setGeometry(235, 150, 100, 40)
        self.display_ost.display(10)

        self.display_chisl = QLCDNumber(self)
        self.display_chisl.setGeometry(235, 200, 100, 40)
        self.display_chisl.display(random.randint(1, 40))

    def first_button(self):

        self.display_ost.display(self.display_ost.value() - 1)
        self.display_chisl.display(self.display_chisl.value() + self.first_button_generate)
        if self.display_chisl.value() != 0 and self.display_ost.value() == 0:
            self.result.setText("Вы проиграли, начинаем новую игру")
            self.display_ost.display(10)
            self.display_chisl.display(random.randint(1, 40))
            self.first_button_generate = random.randint(1, 10)

            self.second_button_generate = random.randint(1, 10)
            while self.second_button_generate == self.first_button_generate:
                self.second_button_generate = random.randint(1, 10)

            self.button1.setText(f"+{self.first_button_generate}")
            self.button2.setText(f"-{self.second_button_generate}")
        if self.display_chisl.value() == 0:
            self.result.setText("Вы выиграли, начинаем новую игру")
            self.display_ost.display(10)
            self.display_chisl.display(random.randint(1, 40))
            self.first_button_generate = random.randint(1, 10)

            self.second_button_generate = random.randint(1, 10)
            while self.second_button_generate == self.first_button_generate:
                self.second_button_generate = random.randint(1, 10)

            self.button1.setText(f"+{self.first_button_generate}")
            self.button2.setText(f"-{self.second_button_generate}")

    def second_button(self):
        self.display_ost.display(self.display_ost.value() - 1)
        self.display_chisl.display(self.display_chisl.value() - self.second_button_generate)
        if self.display_chisl.value() != 0 and self.display_ost.value() == 0:
            self.result.setText("Вы проиграли, начинаем новую игру")
            self.display_ost.display(10)
            self.display_chisl.display(random.randint(1, 40))
            self.first_button_generate = random.randint(1, 10)

            self.second_button_generate = random.randint(1, 10)
            while self.second_button_generate == self.first_button_generate:
                self.second_button_generate = random.randint(1, 10)

            self.button1.setText(f"+{self.first_button_generate}")
            self.button2.setText(f"-{self.second_button_generate}")

        if self.display_chisl.value() == 0:
            self.result.setText("Вы выиграли, начинаем новую игру")
            self.display_ost.display(10)
            self.display_chisl.display(random.randint(1, 40))
            self.first_button_generate = random.randint(1, 10)

            self.second_button_generate = random.randint(1, 10)
            while self.second_button_generate == self.first_button_generate:
                self.second_button_generate = random.randint(1, 10)

            self.button1.setText(f"+{self.first_button_generate}")
            self.button2.setText(f"-{self.second_button_generate}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
