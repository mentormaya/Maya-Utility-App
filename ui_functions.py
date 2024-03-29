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
import re
import json
import pyperclip
import datetime as dt
from libs.PAN import PAN
from libs.Quotes import Quote
import nepali_datetime as ndt
from libs.Numbers import Number
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QFont
from libs.ImageToText import Image2Text
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QStackedWidget, QApplication, QTableWidget, QTableWidgetItem, QTextBrowser, QWidget, QFrame

class UI_Functions:
    def __init__(self, _statusBar, _content_frame):
        super().__init__()
        self.statusBar = _statusBar
        self.content_frame = _content_frame
        self.initSettings()
    
    def initSettings(self):
        self.settings = QSettings('BR Solutions', 'Maya_Utility_App')
        self.settings.setValue('UI/SUB_MENU_MAX', 200)
        self.settings.setValue('UI/SUB_MENU_MIN', 0)
        self.settings.setValue('UI/SUB_MENU_CHECK', 100)
        self.settings.setValue('TAX/VAT_PAN_PATTERN', "\d{9}")
    
    #number utility functions
    def convertNumber(self, num, frame):
        if num == "":
            self.statusBar.setText("Enter the number to convert")
            return
        try:
            num = float(num)
        except ValueError:
            self.statusBar.setText("Please input the valid Number!")
        except:
            self.statusBar.setText("Input Value Exception Occured!")
        else:
            num = Number(str(num))
            data = num.get_num()
            frame.findChild(QLineEdit, "number_disp").setText(data["num"])
            frame.findChild(QPushButton, "num_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["num"]))
            frame.findChild(QLineEdit, "english_disp").setText(data["english"])
            frame.findChild(QPushButton, "eng_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["english"]))
            frame.findChild(QLineEdit, "nepali_disp").setText(data["nepali"])
            frame.findChild(QPushButton, "nep_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["nepali"]))
            frame.findChild(QLineEdit, "decimal_disp").setText(data["decimal"])
            frame.findChild(QPushButton, "decimal_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["decimal"]))
            frame.findChild(QLineEdit, "whole_disp").setText(data["whole"])
            frame.findChild(QPushButton, "whole_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["whole"]))
            frame.findChild(QLineEdit, "lakh_format_disp").setText(data["lakh_format"])
            frame.findChild(QPushButton, "lakh_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["lakh_format"]))
            frame.findChild(QLineEdit, "million_format_disp").setText(data["million_format"])
            frame.findChild(QPushButton, "million_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["million_format"]))
            frame.findChild(QLabel, "words_eng_disp").setText(data["words_eng"])
            frame.findChild(QPushButton, "eng_words_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["words_eng"]))
            frame.findChild(QLabel, "words_nep_disp").setText(data["words_nep"])
            frame.findChild(QPushButton, "nep_words_copy_btn").clicked.connect(lambda: self.copyToClipBoard(data["words_nep"]))
            frame.findChild(QPushButton, "copy_num_all_btn").clicked.connect(lambda: self.copyToClipBoard(json.dumps(data, indent=4, ensure_ascii=False)))
            status = f'{data["lakh_format"]} is converted!'
            print(status)
            self.statusBar.setText(status)
    
    def clearText(self, _input):
        _input.setText("")
        self.statusBar.setText("Inputs are cleared!")
    
    def copyToClipBoard(self, _content):
        pyperclip.copy(_content)
        self.statusBar.setText("Copied to ClipBoard")
        print("Copied to ClipBoard")
    
    def toggleMenu(self, _menu):
        w = _menu.size().width()
        if w > int(self.settings.value('UI/SUB_MENU_CHECK')):
            self.showMenu(_menu, False)
        else:
            self.showMenu(_menu, True)
    
    def showMenu(self, _menu, show):
        if not show:
            _menu.setMaximumWidth(int(self.settings.value('UI/SUB_MENU_MIN')))
            _menu.setMinimumWidth(int(self.settings.value('UI/SUB_MENU_MIN')))
            # print("Hiding Menu")
        else:
            _menu.setMaximumWidth(int(self.settings.value('UI/SUB_MENU_MAX')))
            _menu.setMinimumWidth(int(self.settings.value('UI/SUB_MENU_MAX')))
            # print("Showing Menu")
            
    def showSubMenu(self, _index, _frame):
        _w = _frame.size().width()
        _menu = _frame.findChild(QStackedWidget, "submenu_pages")
        _curr = _menu.currentIndex()
        if _curr == _index:
            self.toggleMenu(_frame)
            # print("toggling menu!")
        elif _w <= int(self.settings.value('UI/SUB_MENU_CHECK')):
            self.showMenu(_frame, True)
            _menu.setCurrentIndex(_index)
            # print(f"Showing menu and clicked! {_w}")
        else:
            _menu.setCurrentIndex(_index)
            # print(f"menu clicked! {_w}")
    
    def loadSettings(self):
        _settings = self.settings.allKeys()
        settings_container = self.content_frame.findChild(QWidget, 'right_menu')
        settings_layout = settings_container.layout()
        seperator = QFrame()
        seperator.setFrameShape(QFrame.HLine)
        seperator.setLineWidth(3)
        for setting in _settings:
            # print(f'{setting} => {self.settings.value(setting)}')
            setting_name = QLabel(setting)
            font = QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            setting_name.setFont(font)
            setting_name.setObjectName(f'{setting}_label')
            settings_layout.addWidget(setting_name)
            
            setting_value = QLineEdit(str(self.settings.value(setting)))
            font = QFont()
            font.setPointSize(10)
            setting_value.setFont(font)
            setting_value.setObjectName(f'{setting}_value')
            settings_layout.addWidget(setting_value)
            settings_layout.addWidget(seperator)
    
    def showPage(self, _widget, _container):
        _container.setCurrentWidget(_widget)
    
    def searchPan(self, _pan, _output_container):
        self.container = _output_container
        self.pan = _pan
        if _pan == "":
            self.statusBar.setText("Enter the VAT/PAN number to search")
            return
        pattern = self.settings.value('TAX/VAT_PAN_PATTERN')
        try:
            if re.match(pattern, _pan) is None:
                raise ValueError("Number not in VAT/PAN Format!")
            _pan = int(_pan)
        except ValueError as v_err:
            self.statusBar.setText(f'Format Error: {str(v_err)}')
        except Exception as e:
            print(e)
            self.statusBar.setText("Input Value Exception Occured!")
        else:
            self.statusUpdate(f'Update: searching details for {_pan}')
            QApplication.processEvents()
            self.pan_search_thread = PAN(pan = _pan)
            self.pan_search_thread.status.connect(self.statusUpdate)
            self.pan_search_thread.complete.connect(self.panSearch_completed)
            self.pan_search_thread.start()
    
    def statusUpdate(self, status):
        print(f"{status}")
        self.statusBar.setText(f"{status}")
            
    def dispPanDetails(self, _details):
        self.statusUpdate(f'Update: Details for {self.pan} fetched Successfully!')
        _details = _details['raw_data']
        _address = f'{_details["panDetails"][0]["street_Name"]} ({_details["panDetails"][0]["ward_No"]}) {_details["panDetails"][0]["vdc_Town"]}'
        _businesses = ""
        if len(_details["businessDetail"]) > 0:
            for index, business in enumerate(_details["businessDetail"]):
                if index == 0:
                    _businesses = f'{business["trade_Name_Nep"]} ({business["trade_Name_Eng"]})'
                else:
                    _businesses = f'{_businesses}, {business["trade_Name_Nep"]} ({business["trade_Name_Eng"]})'
                    
        else:
            _businesses = "No Business Found Registered!"
        self.container.findChild(QLabel, "raw_pan_output").setText(json.dumps(_details, indent=4, ensure_ascii=False))
        table = self.container.findChild(QTableWidget, "pan_table_output")
        table.setItem(0, 0, QTableWidgetItem(str(_details["panDetails"][0]["trade_Name_Eng"])))
        table.setItem(1, 0, QTableWidgetItem(str(_details["panDetails"][0]["trade_Name_Nep"])))
        table.setItem(2, 0, QTableWidgetItem(str(_details["panDetails"][0]["pan"])))
        table.setItem(3, 0, QTableWidgetItem(str(_address)))
        table.setItem(4, 0, QTableWidgetItem(str(_details["panDetails"][0]["mobile"])))
        table.setItem(5, 0, QTableWidgetItem(str(_details["panDetails"][0]["telephone"])))
        table.setItem(6, 0, QTableWidgetItem(str(_details["panDetails"][0]["eff_Reg_Date"])))
        table.setItem(7, 0, QTableWidgetItem(str(_details["panDetails"][0]["office_Name"])))
        table.setItem(8, 0, QTableWidgetItem(str(_details["panDetails"][0]["is_Personal"])))
        table.setItem(9, 0, QTableWidgetItem(str(_details["panTaxClearance"][0]["return_Verified_Date"])))
        table.setItem(10, 0, QTableWidgetItem(str(_details["panDetails"][0]["account_Status"])))
        table.setItem(11, 0, QTableWidgetItem(str(_businesses)))

    def panSearch_completed(self, details):
        self.statusUpdate("Update: Pan Details Fetched")
        self.dispPanDetails(details)
    
    def updateDateTime(self, _np_date, _eng_date):
        self.np_dt_container = _np_date
        self.eng_dt_container = _eng_date
        self.today = {}
        self.today["english"] = dt.date.today().strftime("%Y-%m-%d %a")
        self.today["nepali"] = ndt.date.today().strftime('%K %N %D %G')
        self.np_dt_container.setText(self.today["nepali"])
        self.eng_dt_container.setText(self.today["english"])
    
    def getQuote(self, _quote_disp):
        self.quote_container = _quote_disp
        QApplication.processEvents()
        self.quote_thread = Quote()
        self.quote_thread.status.connect(self.statusUpdate)
        self.quote_thread.complete.connect(self.quoteFetched)
        self.quote_thread.start()
    
    def quoteFetched(self, _quote):
        self.quote = _quote
        self.quote_container.setText(f'{self.quote["q"]} ~ {self.quote["a"]}')
        
    def extTextfromImg(self, images):
        self.statusUpdate(f'Update: Ready to extract from {images["files"][0]}')
        self.img2text = Image2Text(images["files"][0])
        self.img2text.status.connect(self.statusUpdate)
        self.img2text.completed.connect(self.displayTextExtracted)
        self.img2text.start()
    
    def displayTextExtracted(self, text):
        disp = self.content_frame.findChild(QTextBrowser, "extracted_texts")
        disp.setText(text)