import sys

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.size = 1000
        self.setGeometry(0, 0, self.size, self.size)
        self.setWindowTitle('Без имени-1.png')
        self.lbl = QLabel(self)
        self.pix = QtGui.QPixmap('1.jpg')
        self.lbl.setPixmap(self.pix)
        self.lbl.move(0, 0)
        self.setMouseTracking(True)

    def keyPressEvent(self, event):
        img = Image.open('1.jpg')
        pixels = img.load()
        x, y = img.size

        rand = random.randint(-100, 100)
        for i in range(x):
            for j in range(y):
                r, g, b, a = pixels[i, j]
                pixels[i, j] = r + rand, g + rand, b + rand, a
        img.save('new.png')
        self.pix = QtGui.QPixmap('new.png')
        self.lbl.setPixmap(self.pix)

    def mouseMoveEvent(self, event):
        if event.x() + self.pix.size().height() > self.size:
            coord_x = self.size - self.pix.size().height()
        else:
            coord_x = event.x()
        if event.y() + self.pix.size().width() > self.size:
            coord_y = self.size - self.pix.size().width()
        else:
            coord_y = event.y()
        self.lbl.move(coord_x, coord_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
