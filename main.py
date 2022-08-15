'''
#######################################################################################################################
    Project Name: Maya Utility
    Project Description: This project is started to address the daily utility based task for me.
    Project Date: 2022/06/30
    Project Author: Ajay Singh (MaYa)
    Copyright: 2022
    License: MIT Lisence
#######################################################################################################################
'''
from sqlite3 import Date
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QLabel, QPushButton, QSizeGrip, QTabWidget, QLineEdit, QStackedWidget
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QPoint
from DB import DB
import sys

#importing assets
from assets import *
from ui_functions import UI_Functions
from widgets.Date_Converter import Date_Converter
from widgets.DropZone import DropZone

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
        self.db = DB("maya.db")
        
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
        
        #getting status label 
        self.status_disp = self.findChild(QLabel, "status_label")
        
        #adding button click connect to minimize button
        self.min_btn = self.findChild(QPushButton, "btn_minimize")
        self.min_btn.clicked.connect(self.minimizeWindow)
        
        #adding button click connect to maximize button
        self.max_btn = self.findChild(QPushButton, "btn_maximize")
        self.max_btn.clicked.connect(self.maximizeWindow)
        
        #adding button click connect to exit button
        self.btn_close = self.findChild(QPushButton, "btn_close")
        self.btn_close.clicked.connect(self.closeWindow)
        
        self.content_frame = self.findChild(QFrame, "content_frame")
        
        ui_f = UI_Functions(self.status_disp, self.content_frame)
        
        #adding date functionality
        self.nepali_date_disp = self.findChild(QLabel, "nepali_date")
        self.english_date_disp = self.findChild(QLabel, "int_date")
        
        ui_f.updateDateTime(self.nepali_date_disp, self.english_date_disp)
        
        #date conversion functionality
        self.date_converter_btn = self.findChild(QPushButton, "np_cal_btn")
        self.date_converter_btn.clicked.connect(lambda: self.showDateConverter())
        
        #Quotes Display
        self.quote_container = self.findChild(QLabel, "quotes_label")
        self.quote = ui_f.getQuote(self.quote_container)
        
        #Adding Submenu Animation
        self.submenu = self.findChild(QFrame, "sub_menu_frame")
        #Adding right-side-menu Animation
        self.right_menu = self.findChild(QFrame, "right_menu")
        self.right_menu.setMaximumWidth(0)
        self.right_menu.setMinimumWidth(0)
        self.findChild(QPushButton, "options_btn").clicked.connect(lambda: ui_f.toggleMenu(self.right_menu))
        
        #copy to clipboard for dates
        self.np_date = self.findChild(QLabel, "nepali_date")
        self.findChild(QPushButton, "npdt_copy_btn").clicked.connect(lambda: ui_f.copyToClipBoard(self.np_date.text()))
        self.int_date = self.findChild(QLabel, "int_date")
        self.findChild(QPushButton, "intdt_copy_btn").clicked.connect(lambda: ui_f.copyToClipBoard(self.int_date.text()))
        
        #adding button click connect to convert button
        self.convert_btn = self.findChild(QPushButton, "convert_btn")
        num_input = self.findChild(QLineEdit, "num_input")
        self.number_output = self.findChild(QFrame, "output_number")
        self.convert_btn.clicked.connect(lambda: ui_f.convertNumber(num_input.text(), self.utilites_number))
        
        #adding button click connect to clear number button
        self.clear_num_btn = self.findChild(QPushButton, "clear_btn")
        self.clear_num_btn.clicked.connect(lambda: ui_f.clearText(num_input))
        
        #menu and submenu connects
        self.sub_menus_frame = self.findChild(QFrame, "sub_menu_frame")
        self.findChild(QPushButton, "dashboard_menu").clicked.connect(lambda: ui_f.showSubMenu(0, self.sub_menus_frame))
        self.findChild(QPushButton, "utilities_menu").clicked.connect(lambda: ui_f.showSubMenu(1, self.sub_menus_frame))
        self.findChild(QPushButton, "api_menu").clicked.connect(lambda: ui_f.showSubMenu(2, self.sub_menus_frame))
        self.findChild(QPushButton, "tax_menu").clicked.connect(lambda: ui_f.showSubMenu(3, self.sub_menus_frame))
        self.findChild(QPushButton, "lms_menu").clicked.connect(lambda: ui_f.showSubMenu(4, self.sub_menus_frame))
        self.findChild(QPushButton, "settings_menu").clicked.connect(lambda: ui_f.showSubMenu(5, self.sub_menus_frame))
        self.findChild(QPushButton, "help_menu").clicked.connect(lambda: ui_f.showSubMenu(6, self.sub_menus_frame))
        self.findChild(QPushButton, "about_menu").clicked.connect(lambda: ui_f.showSubMenu(7, self.sub_menus_frame))
        
        #page connects 
        pages_container = self.findChild(QStackedWidget, "main_content_pages")
        home_page = self.findChild(QWidget, "dashboard")
        utilities_number_page = self.findChild(QWidget, "utilites_number")
        pdf_merger_utility_page = self.findChild(QWidget, "join_pdf_container")
        image_extraction_page = self.findChild(QWidget, "image_text_extraction_page")
        tax_pan_search_page = self.findChild(QWidget, "tax_pan_search")
        
        #Dashboard
        self.findChild(QPushButton, "home_page").clicked.connect(lambda: ui_f.showPage(home_page, pages_container))
        self.findChild(QPushButton, "numbers_page").clicked.connect(lambda: ui_f.showPage(utilities_number_page, pages_container))
        self.findChild(QPushButton, "join_pdf_page").clicked.connect(lambda: ui_f.showPage(pdf_merger_utility_page, pages_container))
        self.findChild(QPushButton, "image_extraction_page").clicked.connect(lambda: ui_f.showPage(image_extraction_page, pages_container))
        self.findChild(QPushButton, "pan_search_page_btn").clicked.connect(lambda: ui_f.showPage(tax_pan_search_page, pages_container))
        
        
        #PAN Search connects
        self.pan_input = tax_pan_search_page.findChild(QLineEdit, "pan_input")
        output_container = tax_pan_search_page.findChild(QTabWidget, "pan_output")
        raw_output_label = output_container.findChild(QLabel, "raw_pan_output")
        tax_pan_search_page.findChild(QPushButton, "clear_pan_btn").clicked.connect(lambda: ui_f.clearText(self.pan_input))
        tax_pan_search_page.findChild(QPushButton, "copy_pan_raw_btn").clicked.connect(lambda: ui_f.copyToClipBoard(raw_output_label.text()))
        tax_pan_search_page.findChild(QPushButton, "pan_search_btn").clicked.connect(lambda: ui_f.searchPan(self.pan_input.text(), output_container))
        
        
        #PHOTO TO TEXT EXTRACTOR
        self.image_text_extraction_page = self.findChild(DropZone, "image_text_extraction_page")    #Also the DropZone Component
        self.image_text_drop_zone_container = self.findChild(QFrame, "image_drop_zone")
        self.image_text_extraction_page.loaded.connect(ui_f.extTextfromImg)        
        
        #show the window
        self.show()
    
    def showDateConverter(self):
        self.dt_conv_win = Date_Converter(CONFIG)
        self.dt_conv_win.show()
        
    
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