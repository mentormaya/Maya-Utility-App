'''
    this is the comment
    for long run
'''
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QLabel, QPushButton, QSizeGrip, QVBoxLayout, QLineEdit
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QPoint
import sys

#importing assets
from assets import *
from ui_functions import *

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
        
        #Adding Submenu Animation
        self.submenu = self.findChild(QFrame, "sub_menu_frame")
        #Adding right-side-menu Animation
        self.right_menu = self.findChild(QFrame, "right_menu")
        self.right_menu.setMaximumWidth(0)
        self.right_menu.setMinimumWidth(0)
        self.findChild(QPushButton, "options_btn").clicked.connect(lambda: UI_Functions.toggleMenu(self.right_menu))
        
        #copy to clipboard for dates
        self.np_date = self.findChild(QLabel, "nepali_date")
        self.findChild(QPushButton, "npdt_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(self.np_date.text()))
        self.int_date = self.findChild(QLabel, "int_date")
        self.findChild(QPushButton, "intdt_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(self.int_date.text()))
        
        #adding button click connect to convert button
        self.convert_btn = self.findChild(QPushButton, "convert_btn")
        num_input = self.findChild(QLineEdit, "num_input")
        self.number_output = self.findChild(QFrame, "output_number")
        # num_input.setText("113565645.15")
        # print(num_input.text()) 
        self.convert_btn.clicked.connect(lambda: UI_Functions.convertNumber(num_input.text(), self.utilites_number))
        
        #adding button click connect to clear number button
        self.clear_num_btn = self.findChild(QPushButton, "clear_btn")
        self.clear_num_btn.clicked.connect(lambda: UI_Functions.clearText(num_input))
        
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