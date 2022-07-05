from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QLabel, QPushButton, QSizeGrip, QVBoxLayout
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QPoint
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
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.offset = None
        
        #making resizable from the right bottom corner
        grip_frame = self.findChild(QFrame, "grip_frame")
        sizegrip = QSizeGrip(grip_frame)
        # grip_frame.addWidget(sizegrip)
        
        #adding button click connect to minimize button
        self.min_btn = self.findChild(QPushButton, "btn_minimize")
        self.min_btn.clicked.connect(self.minimizeWindow)
        
        #adding button click connect to maximize button
        self.max_btn = self.findChild(QPushButton, "btn_maximize")
        self.max_btn.clicked.connect(self.maximizeWindow)
        
        #adding button click connect to exit button
        self.btn_close = self.findChild(QPushButton, "btn_close")
        self.btn_close.clicked.connect(self.closeWindow)
        
        #show the window
        self.show()
    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()
    
    def minimizeWindow(self, event):
        self.showMinimized()
    
    def maximizeWindow(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def closeWindow(self, event):
        self.close()
    
    def keyPressEvent(self, e):  
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoadUI()
    app.exec_()