import sys

from PyQt5 import QtCore
import math
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.do_paint = False
        self.circle = False
        self.square = False
        self.triangle = False

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def getRandomSize(self):
        return random.randint(10, 300)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.triangle = True
            self.paint()

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if (event.button() == Qt.LeftButton):
            self.circle = True
            self.paint()
        elif (event.button() == Qt.RightButton):
            self.square = True
            self.paint()

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
        if self.circle:
            size_x = self.getRandomSize()
            qp.setBrush(QtGui.QBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
                                     Qt.SolidPattern))
            qp.drawEllipse(self.x - size_x / 2, self.y - size_x / 2, size_x, size_x)
            self.circle = False
        if self.square:
            size_x = self.getRandomSize()
            qp.setBrush(QtGui.QBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
                                     Qt.SolidPattern))
            qp.drawRect(self.x - size_x / 2, self.y - size_x / 2, size_x, size_x)
            self.square = False
        if self.triangle:
            a = self.getRandomSize()
            d = a * math.tan(math.radians(30))
            pos_top = QtCore.QPointF(self.x, self.y - a // 2)
            pos_left = QtCore.QPointF(self.x - d, self.y + a // 2)
            pos_right = QtCore.QPointF(self.x + d, self.y + a // 2)
            qp.setBrush(QtGui.QBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
                                     Qt.SolidPattern))
            path = QtGui.QPainterPath()
            path.moveTo(pos_top)
            path.lineTo(pos_right)
            path.lineTo(pos_left)
            self.triangle = False
            qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
