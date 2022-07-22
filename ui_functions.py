'''
#######################################################################################################################
    
#######################################################################################################################
'''
import re
import json
import asyncio
import aiohttp
import requests
import pyperclip
from libs.Numbers import Number
from PyQt5.QtCore import QThread, pyqtSignal
from requests import Timeout, TooManyRedirects, HTTPError
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QStackedWidget, QApplication, QTableWidget, QTableWidgetItem

SUB_MENU_MAX = 175
SUB_MENU_MIN = 0
SUB_MENU_CHECK = 100

VAT_PAN_PATTERN =   "\d{9}"

BASE_API = "https://fastapi-production-c751.up.railway.app"

REQ_HEADERS = {
    'User-Agent': ''
}

class PAN(QThread):
    status = pyqtSignal(str)
    complete = pyqtSignal(dict)
    def __init__(self, pan = 0):
        super(PAN, self).__init__()
        self.pan = pan
        self.is_running = True
    
    def run(self):
        self.api_url = f'{BASE_API}/pan/v1/{self.pan}'
        QApplication.processEvents()
        self.resp = requests.get(self.api_url)
        QApplication.sendPostedEvents()
        if self.resp.status_code == 200:
            self.details = self.resp.json()
            self.complete.emit(self.details)
            self.update(f'Fetching Completed!')
        else:
            self.complete.emit({'msg': "No Details could be fetched", 'result': False})
    
    def update(self, msg):
        print(f'PAN Update: {msg}')
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating Search for {self.pan}')
        self.terminate()

class UI_Functions:
    def __init__(self, _statusBar):
        super().__init__()
        self.statusBar = _statusBar
    
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
            status = f'{data["num"]} is converted!'
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
        if w > SUB_MENU_CHECK:
            self.showMenu(_menu, False)
        else:
            self.showMenu(_menu, True)
    
    def showMenu(self, _menu, show):
        if not show:
            _menu.setMaximumWidth(SUB_MENU_MIN)
            _menu.setMinimumWidth(SUB_MENU_MIN)
            # print("Hiding Menu")
        else:
            _menu.setMaximumWidth(SUB_MENU_MAX)
            _menu.setMinimumWidth(SUB_MENU_MAX)
            # print("Showing Menu")
            
    def showSubMenu(self, _index, _frame):
        _w = _frame.size().width()
        _menu = _frame.findChild(QStackedWidget, "submenu_pages")
        _curr = _menu.currentIndex()
        if _curr == _index:
            self.toggleMenu(_frame)
            # print("toggling menu!")
        elif _w <= SUB_MENU_CHECK:
            self.showMenu(_frame, True)
            _menu.setCurrentIndex(_index)
            # print(f"Showing menu and clicked! {_w}")
        else:
            _menu.setCurrentIndex(_index)
            # print(f"menu clicked! {_w}")
    
    def showPage(self, _widget, _container):
        _container.setCurrentWidget(_widget)
    
    def searchPan(self, _pan, _output_container):
        self.container = _output_container
        self.pan = _pan
        if _pan == "":
            self.statusBar.setText("Enter the VAT/PAN number to search")
            return
        try:
            if re.match(VAT_PAN_PATTERN, _pan) is None:
                raise ValueError("Number not in VAT/PAN Format!")
            _pan = int(_pan)
        except ValueError as v_err:
            self.statusBar.setText(f'Format Error: {str(v_err)}')
        except:
            self.statusBar.setText("Input Value Exception Occured!")
        else:
            self.statusUpdate(f'searching details for {_pan}')
            QApplication.processEvents()
            self.pan_search_thread = PAN(pan = _pan)
            self.pan_search_thread.status.connect(self.statusUpdate)
            self.pan_search_thread.complete.connect(self.panSearch_completed)
            self.pan_search_thread.start()
    
    def statusUpdate(self, status):
        print(f"Update: {status}")
        self.statusBar.setText(f"Update: {status}")
            
    def dispPanDetails(self, _details):
        self.statusUpdate(f'Details for {self.pan} fetched Successfully!')
        _details = _details['raw_data']
        _address = f'{_details["panDetails"][0]["street_Name"]} ({_details["panDetails"][0]["ward_No"]}) {_details["panDetails"][0]["vdc_Town"]}'
        _businesses = "Businesses"
        self.container.findChild(QLabel, "raw_pan_output").setText(json.dumps(_details, indent=4, ensure_ascii=False))
        table = self.container.findChild(QTableWidget, "pan_table_output")
        table.setItem(0, 1, QTableWidgetItem(str(_details["panDetails"][0]["trade_Name_Eng"])))
        table.setItem(1, 1, QTableWidgetItem(str(_details["panDetails"][0]["trade_Name_Nep"])))
        table.setItem(2, 1, QTableWidgetItem(str(_details["panDetails"][0]["pan"])))
        table.setItem(3, 1, QTableWidgetItem(str(_address)))
        table.setItem(4, 1, QTableWidgetItem(str(_details["panDetails"][0]["mobile"])))
        table.setItem(5, 1, QTableWidgetItem(str(_details["panDetails"][0]["telephone"])))
        table.setItem(6, 1, QTableWidgetItem(str(_details["panDetails"][0]["eff_Reg_Date"])))
        table.setItem(7, 1, QTableWidgetItem(str(_details["panDetails"][0]["office_Name"])))
        table.setItem(8, 1, QTableWidgetItem(str(_details["panDetails"][0]["is_Personal"])))
        table.setItem(9, 1, QTableWidgetItem(str(_businesses)))
        table.setItem(10, 1, QTableWidgetItem(str(_details["panTaxClearance"][0]["return_Verified_Date"])))
        table.setItem(11, 1, QTableWidgetItem(str(_details["panDetails"][0]["account_Status"])))

    def panSearch_completed(self, details):
        self.statusUpdate("Pan Details Fetched")
        self.dispPanDetails(details)