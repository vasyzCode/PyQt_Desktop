import csv

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Цена", "Количество"])
        self.tableWidget.setAlternatingRowColors(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        prices = []
        rows = []
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index != 0:
                    rows.append([row[0], int(row[1]),
                                 int(0)])
                    prices.append(int(row[1]))
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.rows_count = len(rows)
        for i in range(self.rows_count):
            index = prices.index(max(prices))
            r = randint(1, 255)
            g = randint(1, 255)
            b = randint(1, 255)
            if self.tableWidget.rowCount() <= 4:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                new_item = QtWidgets.QTableWidgetItem(rows[index][0])
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 0, new_item)
                new_item = QtWidgets.QTableWidgetItem(str(rows[index][1]))
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 1, new_item)
                new_item = QtWidgets.QTableWidgetItem(str(rows[index][2]))
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 2, new_item)
            else:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(rows[index][0]))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(rows[index][1])))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(rows[index][2])))
            prices.remove(prices[index])
            rows.remove(rows[index])
        self.pushButton.clicked.connect(self.sort_table)
        self.tableWidget.cellChanged.connect(self.changed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "Итого:"))

    def changed(self, sender):
        result = 0
        print(self.tableWidget.rowCount(), self.rows_count)
        if self.tableWidget.rowCount() == self.rows_count:
            for row in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(row, 1) and self.tableWidget.item(row, 2):
                    result += int(self.tableWidget.item(row, 1).text()) * int(self.tableWidget.item(row, 2).text())
            self.lineEdit.setText(str(result))

    def sort_table(self, sender):
        prices = []
        rows = []
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index != 0:
                    rows.append([row[0], int(row[1]),
                                 int(self.tableWidget.item(
                                     self.tableWidget.findItems(row[0], QtCore.Qt.MatchExactly)[0].row(), 2).text())])
                    prices.append(int(row[1]))
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        for i in range(len(rows)):
            index = prices.index(max(prices))
            r = randint(1, 255)
            g = randint(1, 255)
            b = randint(1, 255)
            if self.tableWidget.rowCount() <= 4:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                new_item = QtWidgets.QTableWidgetItem(rows[index][0])
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 0, new_item)
                new_item = QtWidgets.QTableWidgetItem(str(rows[index][1]))
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 1, new_item)
                new_item = QtWidgets.QTableWidgetItem(str(rows[index][2]))
                new_item.setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))
                self.tableWidget.setItem(rowPosition, 2, new_item)
            else:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(rows[index][0]))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(rows[index][1])))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(rows[index][2])))
            prices.remove(prices[index])
            rows.remove(rows[index])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
