import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Ввести количество цветов флага', self)
        self.btn.move(20, 20)
        self.do_paint = False
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        self.dialog = QDialog()
        btn = QPushButton('ok', self.dialog)
        btn.move(50, 70)
        btn_1 = QPushButton('cancel', self.dialog)
        btn_1.move(200, 70)
        btn_1.clicked.connect(self.hideDialog)
        btn.clicked.connect(self.paint)
        self.input = QSpinBox(self.dialog)
        self.input.setGeometry(50, 20, 270, 30)
        self.dialog.setWindowTitle("Введите")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def hideDialog(self):
        self.dialog.hide()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.dialog.hide()
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        start_pos = 90
        for _ in range(int(self.input.text())):
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawRect(30, start_pos, 120, 30)
            start_pos += 30


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
