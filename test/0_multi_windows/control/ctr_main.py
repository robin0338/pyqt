from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QActionGroup
from PyQt5.QtCore import Qt
from pathlib import Path
from gui.Ui_Stock import Ui_MainWindow
from gui.Ui_Update import Ui_UpdateWindow



class Ctr_Main():
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        self.objGUI = Ui_MainWindow()
        self.objGUI.setupUi(window)
        self.__initGUI(window)
        window.setFixedSize(window.size())
        window.show()
        sys.exit(app.exec_())

    def update_window(self):
        self.update = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateWindow()
        self.ui.setupUi(self.update)
        self.update.show()

    def __initGUI(self, window):
        self.objGUI.actionupdate.triggered.connect(self.update_window) # type: ignore  
