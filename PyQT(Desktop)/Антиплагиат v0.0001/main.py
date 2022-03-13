import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QStatusBar
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QPlainTextEdit, QListWidget, QDoubleSpinBox
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 1000, 1000)
        self.setWindowTitle('Записная книжка')

        self.text1 = QLabel(self)
        self.text1.setText("Порог срабатывания(%)")
        self.text1.setGeometry(10, 10, 300, 20)

        self.text1_count = QDoubleSpinBox(self)
        self.text1_count.setValue(80)
        self.text1_count.setMaximum(100)
        self.text1_count.setGeometry(200, 10, 780, 30)

        self.text_number = QLabel(self)
        self.text_number.setText("Текст 1")
        self.text_number.setGeometry(10, 50, 200, 30)

        self.text_number_2 = QLabel(self)
        self.text_number_2.setText("Текст 2")
        self.text_number_2.setGeometry(500, 50, 200, 30)

        self.text_1 = QPlainTextEdit(self)
        self.text_1.setGeometry(10, 90, 480, 800)

        self.text_2 = QPlainTextEdit(self)
        self.text_2.setGeometry(500, 90, 490, 800)

        self.button = QPushButton(self)
        self.button.setText("Сравнить")
        self.button.setGeometry(10, 900, 980, 40)
        self.button.clicked.connect(self.check_text)

        self.status = QStatusBar(self)
        self.status.setGeometry(10, 940, 1000, 60)

    def check_text(self):
        print(self.text_1.toPlainText().split('\n'), 'asdasd')
        self.right = 0
        self.alls = len(self.text_1.toPlainText().split('\n')) + len(self.text_2.toPlainText().split('\n'))
        for i in self.text_1.toPlainText().split('\n'):
            for j in self.text_2.toPlainText().split('\n'):
                if i == j:
                    self.right += 2

        self.shog = self.right / self.alls * 100

        if self.shog > self.text1_count.value():
            self.status.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgba(0,255,0,255);color:black;font-weight:bold;}")
            self.status.showMessage(f'Код схож на {self.shog}%')
        else:
            self.status.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.status.showMessage(f'Код схож на {self.shog}%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
