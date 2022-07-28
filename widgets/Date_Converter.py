import datetime as dt
import nepali_datetime as ndt
from PyQt5.QtCore import QPoint
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox as alert
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QCheckBox

class Date_Converter(QWidget):
    def __init__(self, CONFIG):
        super().__init__()
        #load the ui file on the fly
        uic.loadUi("assets/UI/DateConverter.ui", self)
        self.CONFIG = CONFIG
        self.YEAR_DIVIDER = 2030
        
        #populating up app name and app info
        self.title = f'Date Converter :: {self.CONFIG["APP_NAME"]} {self.CONFIG["VERSION"]}'
        self.icon = self.CONFIG["ICON"]
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        
        #bydefault get today date and display
        self.today = {}
        self.today['int'] = dt.date.today()
        self.today['nep'] = ndt.date.today()
        self.calculateDate()
        
        #click connect for convert button
        self.convert_btn = self.findChild(QPushButton, "convert_btn")
        self.convert_btn.clicked.connect(lambda: self.convert())
        
        #checkbox value change
        self.convert_to = "BS"
        self.checkbox = self.findChild(QCheckBox, "BS_AD")
        self.checkbox.setChecked(True)
        self.checkbox.setText(self.convert_to)
        self.checkbox.stateChanged.connect(lambda: self.updateConvertTO())
    
    def updateConvertTO(self):
        if self.checkbox.isChecked() == True:
            self.convert_to = "BS"
        else:
            self.convert_to = "AD"
        self.checkbox.setText(self.convert_to)
    
    def convert(self):
        self.dt_input = self.findChild(QLineEdit, "date_input")
        self.month_input = self.findChild(QLineEdit, "month_input")
        self.year_input = self.findChild(QLineEdit, "year_input")
        
        if self.dt_input.text() == '':
            alert.warning(self, "Input Required", "Please enter the value for Date")
            return
        if self.month_input.text() == '':
            alert.warning(self, "Input Required", "Please enter the value for Month")
            return
        if self.year_input.text() == '':
            alert.warning(self, "Input Required", "Please enter the value for Year")
            return
        date = f'{self.year_input.text()}-{self.month_input.text()}-{self.dt_input.text()}'
        self.calculateDate(date)
    
    def calculateDate(self, date = ''):
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
            inputs = date.split("-")
            try:
                # calculate the date provided
                if self.convert_to == "BS":
                    ad_dt = dt.date(int(inputs[0]), int(inputs[1]), int(inputs[2]))
                    converted = ndt.date.from_datetime_date(ad_dt)
                    print(f'Converted {date} to BS as {converted.strftime("%K-%N-%D-%G")} corresponding to {ad_dt.strftime("%Y-%B-%d-%A")}')
                    self.date["int"]["year"] = ad_dt.strftime("%Y")
                    self.date["int"]["month_date"] = ad_dt.strftime("%B, %d")
                    self.date["int"]["day"] = ad_dt.strftime("%A")
                    self.date["nep"]["year"] = converted.strftime('%K')
                    self.date["nep"]["month_date"] = converted.strftime('%N, %D')
                    self.date["nep"]["day"] = converted.strftime('%G')
                else:
                    bs_dt = ndt.date(int(inputs[0]), int(inputs[1]), int(inputs[2]))
                    converted = bs_dt.to_datetime_date()
                    print(f'Converted {date} to AD as {converted.strftime("%Y-%B-%d-%A")} corresponding to {bs_dt.strftime("%K-%N-%D-%G")}')
                    self.date["int"]["year"] = converted.strftime("%Y")
                    self.date["int"]["month_date"] = converted.strftime("%B, %d")
                    self.date["int"]["day"] = converted.strftime("%A")
                    self.date["nep"]["year"] = bs_dt.strftime('%K')
                    self.date["nep"]["month_date"] = bs_dt.strftime('%N, %D')
                    self.date["nep"]["day"] = bs_dt.strftime('%G')
            except BaseException as err:
                alert.warning(self, "Unexpected Error!", f"{err.__class__.__name__}: {err}")
            else:
                self.updateDate()
    
    def updateDate(self):
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