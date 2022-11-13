from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QActionGroup
from PyQt5.QtCore import Qt
from pathlib import Path
from gui.Ui_Stock import Ui_MainWindow



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

    def __initGUI(self, window):
        self.objGUI.actionupdate.triggered.connect(self.__setUpdate) # type: ignore  

    def __setUpdate(self):
        from control.ctr_update import Ctr_Update
        self.UpWin = Ctr_Update()
        self.UpWin.setFixedSize(self.UpWin.size())
        self.UpWin.show()

