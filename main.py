from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QLabel, QPushButton, QSizeGrip, QVBoxLayout
from PyQt5 import uic, QtGui, QtCore
import sys

CONFIG = {
    ### App related constants
    "APP_NAME": "Maya Utility App",
    "VERSION": "v1.0.0",
    "COPY_TEXT": "Copyright@",
    "COPYRIGHT_YEAR": "2022",
    "COPYRIGHT": "Ajay Singh",
    "CREDIT_TEXT": "Design Credit:",
    "AUTHOR": "Ajay Singh [Maya]",
    "ICON": "assets/icon.ico"
}

class LoadUI(QMainWindow):
    def __init__(self):
        super(LoadUI, self).__init__()
        #setup loading UI and everything
        self.setupUI()
        
    def setupUI(self):
        #load the ui file on the fly
        uic.loadUi("assets/UI/Interface.ui", self)
        
        #populating up app name and app info
        self.title = f'{CONFIG["APP_NAME"]} {CONFIG["VERSION"]}'
        self.icon = CONFIG["ICON"]
        self.app_title = self.findChild(QLabel, "app_title")
        self.app_title.setText(self.title)
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        # self.setGeometry(self.left, self.top, self.width, self.height)
        
        #populating copyright and credit info
        self.credit_label = self.findChild(QLabel, "credit_label")
        self.credit_label.setText(f'{CONFIG["COPY_TEXT"]} {CONFIG["COPYRIGHT"]} {CONFIG["COPYRIGHT_YEAR"]}. {CONFIG["CREDIT_TEXT"]} {CONFIG["AUTHOR"]} All the rights are reserved.')

        #Frameless window to make custom titlebar
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        
        grip_frame = self.findChild(QFrame, "grip_frame")
        sizegrip = QSizeGrip(self)
        grip_frame.addWidget(sizegrip)
        
        
        #show the window
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoadUI()
    app.exec_()