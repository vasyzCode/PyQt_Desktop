import sys

from PyQt5.QtGui import QFont
from PyQt5 import uic, QtCore  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QBoxLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calendar.ui', self)  # Загружаем дизайн
        self.button.clicked.connect(self.create_task)

    def create_task(self):
        day, month, year = self.calendar.selectedDate().day(), self.calendar.selectedDate().month(), self.calendar.selectedDate().year()
        hour, min, sec = self.timeedit.time().hour(), self.timeedit.time().minute(), self.timeedit.time().second()
        task = f"{year}-{month}-{day} {hour}:{min}:{sec} - {self.input.text()}"
        self.widgets.addItem(task)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
