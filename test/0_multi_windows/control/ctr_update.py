from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from gui.Ui_Update import Ui_UpdateWindow
from model.crawling_stock_en import crawing


class Ctr_Update(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ctr_Update, self).__init__()
        self.objGUI = Ui_UpdateWindow()
        self.objGUI.setupUi(self)
        #test
        self.objGUI.pushButton_2.clicked.connect(self.__test)
    
    def __test(self):
        text_le_1 = self.objGUI.lineEdit.text()
        text_le_2 = self.objGUI.lineEdit_2.text()
        crawing(text_le_1,text_le_2)  


        #QMessageBox.information(None, 'my messagebox', test_le)



