import datetime as dt
import nepali_datetime as ndt
from PyQt5.QtCore import QPoint
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel

class Date_Converter(QWidget):
    def __init__(self, CONFIG):
        super().__init__()
        #load the ui file on the fly
        uic.loadUi("assets/UI/DateConverter.ui", self)
        self.CONFIG = CONFIG
        
        #populating up app name and app info
        self.title = f'Date Converter :: {self.CONFIG["APP_NAME"]} {self.CONFIG["VERSION"]}'
        self.icon = self.CONFIG["ICON"]
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        
        #bydefault get today date and display
        self.today = {}
        self.today['int'] = dt.date.today()
        self.today['nep'] = ndt.date.today()
        self.updateDate()
        
    def calculateDate(self, date):
        self.date = {}
        self.date["int"] = {}
        self.date["nep"] = {}
        
        if date == '':
            self.date["int"]["year"] = self.today['int'].strftime("%Y")
            self.date["int"]["month_date"] = self.today['int'].strftime("%B, %d")
            self.date["int"]["day"] = self.today['int'].strftime("%A")
            self.date["nep"]["year"] = self.today['nep'].strftime('%K')
            self.date["nep"]["month_date"] = self.today['nep'].strftime('%N, %D')
            self.date["nep"]["day"] = self.today['nep'].strftime('%G')
        else:
            # TODO calculate the date provided
            print('calculation being carried out')
    
    def updateDate(self, date = ''):
        self.calculateDate(date)
        #extract dates containers
        self.int_yr_label = self.findChild(QLabel, "int_yr_lbl")
        self.int_yr_label.setText(self.date["int"]["year"])
        self.int_month_date_label = self.findChild(QLabel, "int_month_date_label")
        self.int_month_date_label.setText(self.date["int"]["month_date"])
        self.int_day_label = self.findChild(QLabel, "int_day_label")
        self.int_day_label.setText(self.date["int"]["day"])
        self.nep_yr_label = self.findChild(QLabel, "nep_yr_lbl")
        self.nep_yr_label.setText(self.date["nep"]["year"])
        self.nep_month_date_label = self.findChild(QLabel, "nep_month_date_label")
        self.nep_month_date_label.setText(self.date["nep"]["month_date"])
        self.nep_day_label = self.findChild(QLabel, "nep_day_label")
        self.nep_day_label.setText(self.date["nep"]["day"])
        
    
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