from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QLabel, QPushButton
from PyQt5 import uic
import sys

CONFIG = {
    ### App related constants
    "APP_NAME": "Maya Utility App",
    "VERSION": "v1.0.0",
    "COPY_TEXT": "Copyright@",
    "COPYRIGHT_YEAR": "2022",
    "COPYRIGHT": "Ajay Singh [Maya]",
    "CREDIT_TEXT": "Design Credit:",
    "AUTHOR": "Ajay Singh [Maya]"
}

class LoadUI(QMainWindow):
    def __init__(self):
        super(LoadUI, self).__init__()
        #setup loading UI and everything
        self.setupUI()
        
    def setupUI(self):
        #load the ui file on the fly
        uic.loadUi("assets/UI/Interface.ui", self)
        #show the window
        self.show()
        
        #populating up app name and app info
        self.app_title = self.findChild(QLabel, "app_title")
        self.app_title.setText(f'{CONFIG["APP_NAME"]} {CONFIG["VERSION"]}')
        
        #populating copyright and credit info
        self.credit_label = self.findChild(QLabel, "credit_label")
        self.credit_label.setText(f'{CONFIG["COPY_TEXT"]} {CONFIG["COPYRIGHT"]} {CONFIG["COPYRIGHT_YEAR"]}. {CONFIG["CREDIT_TEXT"]} {CONFIG["AUTHOR"]} All the rights are reserved.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoadUI()
    app.exec_()