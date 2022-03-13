import sys

from PyQt5.Qt import *

from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Отображение картинки')
        self.current = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.new_img = 'new.jpg'
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('PIL 2.0')
        self.pixmap = QPixmap(self.current)
        self.image = QLabel(self)
        self.image.move(250, -40)
        self.image.resize(400, 400)
        self.image.setPixmap(self.pixmap)
        self.btn = QPushButton('R', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.r_color)
        self.btn = QPushButton('G', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.g_color)
        self.btn = QPushButton('B', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 100)
        self.btn.clicked.connect(self.b_color)
        self.btn = QPushButton('ALL', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 140)
        self.btn.clicked.connect(self.full_color)
        self.btn = QPushButton('Против часовой стрелки', self)
        self.btn.resize(200, 30)
        self.btn.move(20, 320)
        self.btn.clicked.connect(self.l_turn)
        self.btn = QPushButton('По часовой стрелке', self)
        self.btn.resize(200, 30)
        self.btn.move(250, 320)
        self.btn.clicked.connect(self.r_turn)

    def r_color(self):
        img = Image.open(self.current)
        rgb_im = img.convert('RGB')
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = rgb_im.getpixel((i, j))
                rgb_im.putpixel((i, j), (r, 0, 0))

        rgb_im.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)

    def g_color(self):
        img = Image.open(self.current)
        rgb_im = img.convert('RGB')
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = rgb_im.getpixel((i, j))
                rgb_im.putpixel((i, j), (0, g, 0))
        rgb_im.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)

    def b_color(self):
        img = Image.open(self.current)
        rgb_im = img.convert('RGB')
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = rgb_im.getpixel((i, j))
                rgb_im.putpixel((i, j), (0, 0, b))
        rgb_im.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)

    def full_color(self):
        img = Image.open(self.current)
        rgb_im = img.convert('RGB')
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = rgb_im.getpixel((i, j))
                rgb_im.putpixel((i, j), (r, g, b))
        rgb_im.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)

    def l_turn(self):
        img = Image.open(self.new_img)
        img = img.rotate(90)
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)

    def r_turn(self):
        img = Image.open(self.new_img)
        img = img.rotate(90)
        img = img.transpose(Image.ROTATE_180)
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
