import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QPlainTextEdit, QListWidget
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 500)
        self.setWindowTitle('Записная книжка')

        self.name = QLabel(self)
        self.name.setGeometry(10, 20, 100, 30)
        self.name.setText("Имя")

        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(100, 20, 200, 30)

        self.number = QLabel(self)
        self.number.setGeometry(10, 80, 100, 30)
        self.number.setText("Телефон")

        self.number_input = QLineEdit(self)
        self.number_input.setGeometry(100, 80, 200, 30)

        self.button = QPushButton(self)
        self.button.setGeometry(350, 50, 100, 30)
        self.button.setText("Добавить")
        self.button.clicked.connect(self.add_user)

        self.list_numbers = QListWidget(self)
        self.list_numbers.setGeometry(10, 150, 480, 340)

    def add_user(self):
        self.list_numbers.addItem(f"{self.name_input.text()} {self.number_input.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
