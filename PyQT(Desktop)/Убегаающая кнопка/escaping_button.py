import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Убегающая кнопка')
        self.button = QPushButton('Нажми на меня', self)
        self.coords_button = self.random_coords()
        self.button.move(*self.coords_button)
        self.button.resize(150, 40)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if self.coords_button[0] + 150 >= event.x() - 4 >= self.coords_button[0] - 10 and self.coords_button[
            1] + 40 >= event.y() - 4 >= self.coords_button[1] - 10:
            self.coords_button = self.random_coords()
            self.button.move(*self.coords_button)
        self.x = event.x()
        self.y = event.y()

    def random_coords(self):
        return random.randint(0, 600), random.randint(0, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
