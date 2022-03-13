import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QPlainTextEdit
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 500)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.chizb = QCheckBox('Чизбургер', self)
        self.chizb.move(10, 10)
        self.chizb.stateChanged.connect(self.changeHide1)

        self.chizb_count = QLineEdit(self)
        self.chizb_count.setGeometry(150, 10, 40, 25)
        self.chizb_count.setEnabled(False)

        self.gamburg = QCheckBox('Гамбургер', self)
        self.gamburg.move(10, 40)
        self.gamburg.stateChanged.connect(self.changeHide2)

        self.gamburg_count = QLineEdit(self)
        self.gamburg_count.setGeometry(150, 40, 40, 25)
        self.gamburg_count.setEnabled(False)

        self.cola = QCheckBox('Кока-кола', self)
        self.cola.move(10, 70)
        self.cola.stateChanged.connect(self.changeHide3)

        self.cola_count = QLineEdit(self)
        self.cola_count.setGeometry(150, 70, 40, 25)
        self.cola_count.setEnabled(False)

        self.nagents = QCheckBox('Нагетсы', self)
        self.nagents.move(10, 100)
        self.nagents.stateChanged.connect(self.changeHide4)

        self.nagents_count = QLineEdit(self)
        self.nagents_count.setGeometry(150, 100, 40, 25)
        self.nagents_count.setEnabled(False)

        self.button = QPushButton(self)
        self.button.setText("Заказать")
        self.button.setGeometry(10, 150, 100, 30)
        self.button.clicked.connect(self.print_check)

        self.display = QPlainTextEdit(self)
        self.display.setGeometry(10, 200, 300, 200)
        self.display.setEnabled(False)

    def changeHide1(self, state):
        if state == Qt.Checked:
            self.chizb_count.setEnabled(True)
            self.chizb_count.setText('1')
        else:
            self.chizb_count.setEnabled(False)
            self.chizb_count.setText('')

    def changeHide2(self, state):
        if state == Qt.Checked:
            self.gamburg_count.setEnabled(True)
            self.gamburg_count.setText('1')
        else:
            self.gamburg_count.setEnabled(False)
            self.gamburg_count.setText('')

    def changeHide3(self, state):
        if state == Qt.Checked:
            self.cola_count.setEnabled(True)
            self.cola_count.setText('1')
        else:
            self.cola_count.setEnabled(False)
            self.cola_count.setText('')

    def changeHide4(self, state):
        if state == Qt.Checked:
            self.nagents_count.setEnabled(True)
            self.nagents_count.setText('1')
        else:
            self.nagents_count.setEnabled(False)
            self.nagents_count.setText('')

    def print_check(self):
        text = """Ваш заказ:\n"""
        summ = 0
        if self.chizb.checkState() == 2:
            text += f"\nЧизбургер----{self.chizb_count.text()}----{int(self.chizb_count.text()) * 10}"
            summ += int(self.chizb_count.text()) * 10
        if self.gamburg.checkState() == 2:
            text += f"\nГамбургер----{self.gamburg_count.text()}----{int(self.gamburg_count.text()) * 20}"
            summ += int(self.gamburg_count.text()) * 20
        if self.cola.checkState() == 2:
            text += f"\nКока-кола----{self.cola_count.text()}----{int(self.cola_count.text()) * 30}"
            summ += int(self.cola_count.text()) * 30
        if self.nagents.checkState() == 2:
            text += f"\nНагентсы----{self.nagents_count.text()}----{int(self.nagents_count.text()) * 40}"
            summ += int(self.nagents_count.text()) * 40
        text += f"\n\nИтого: {summ}"
        self.display.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
