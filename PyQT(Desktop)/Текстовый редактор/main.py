import sys

from PyQt5.QtGui import QFont
from PyQt5 import uic, QtCore  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QBoxLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lms.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.create_file)
        self.pushButton_2.clicked.connect(self.save_file)
        self.pushButton_3.clicked.connect(self.open_file)

    def create_file(self):
        text_file = open(f"{self.lineEdit.text()}", 'w')
        text_file.close()

    def save_file(self):
        e = open(f"{self.lineEdit.text()}", 'w', encoding='utf-8')
        result = ''
        for line in self.textEdit.toPlainText().split('\n'):
            result += f"{line}\n"
        e.write(result)

    def open_file(self):
        self.textEdit.setText(open(f"{self.lineEdit.text()}", 'r', encoding='utf-8').read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
