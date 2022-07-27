from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic, QtGui, QtCore

class Date_Converter(QWidget):
    def __init__(self, CONFIG):
        super().__init__()
        #load the ui file on the fly
        uic.loadUi("assets/UI/DateConverter.ui", self)
        
        #populating up app name and app info
        self.title = f'Date Converter :: {CONFIG["APP_NAME"]} {CONFIG["VERSION"]}'
        self.icon = CONFIG["ICON"]
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))