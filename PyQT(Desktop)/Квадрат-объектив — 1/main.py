import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 700, 700, 700)
        self.setWindowTitle('Квадрат-объектив — 1')
        self.button = QPushButton(self)
        self.button.setText('Показать')
        self.button.move(20, 20)
        self.n = QLineEdit(self)
        self.n.move(200, 100)
        self.coeff = QLineEdit(self)
        self.coeff.move(200, 60)
        self.side = QLineEdit(self)
        self.side.move(200, 20)
        self.label = QLabel(self)
        self.label.setText('n')
        self.label.move(160, 100)
        self.label2 = QLabel(self)
        self.label2.setText('coeff')
        self.label2.move(160, 60)
        self.label3 = QLabel(self)
        self.label3.setText('side')
        self.label3.move(160, 20)

        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        side = int(self.side.text())
        coeff = float(self.coeff.text())
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))
        qp.drawRect(int(350 - side / 2), int(350 - side / 2), int(side), int(side))
        for _ in range(int(self.n.text()) - 1):
            side *= coeff
            qp.drawRect(int(350 - side / 2), int(350 - side / 2), int(side), int(side))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
