import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLabel, QFileDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PIL import Image


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 400, 400)
        self.setWindowTitle("Изменение прозрачности")

        self.mySlider = QSlider(Qt.Vertical, self)
        self.mySlider.setGeometry(20, 40, 20, 300)
        self.mySlider.valueChanged[int].connect(self.changeValue)

        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.jpg)')[0]
        self.pixmap = QPixmap(self.fname)
        self.pixmap = self.pixmap.scaled(250, 250)

        self.label = QLabel(self)
        self.label.setGeometry(100, 40, 250, 250)
        self.label.setPixmap(self.pixmap)

    def changeValue(self, value):
        im_rgb = Image.open(self.fname)
        im_rgba = im_rgb.copy()
        im_rgba.putalpha(int(self.mySlider.value() * 2.55))
        im_rgba.save('new.png')
        self.pixmap = QPixmap('new.png')
        self.pixmap = self.pixmap.scaled(250, 250)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
