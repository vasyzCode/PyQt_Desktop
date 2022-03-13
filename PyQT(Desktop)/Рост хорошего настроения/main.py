import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.slider = QSlider(self)
        self.slider.valueChanged.connect(self.paint)
        self.slider.setValue(100)
        self.slider.setGeometry(970, 10, 30, 1000)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_smile(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw_smile(self, qp):
        koeff = self.slider.value() / 50
        qp.setBrush(QColor(244, 222, 204))
        qp.drawEllipse(40 * koeff, 40 * koeff, 400 * koeff, 400 * koeff)
        qp.setBrush(QColor(255, 255, 255))
        qp.drawEllipse(100 * koeff, 150 * koeff, 80 * koeff, 80 * koeff)
        qp.drawEllipse(300 * koeff, 150 * koeff, 80 * koeff, 80 * koeff)
        qp.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        qp.drawArc(125 * koeff, 170 * koeff, 250 * koeff, 200 * koeff, 0, -180 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
