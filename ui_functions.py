import re
import json
import aiohttp
import requests
import pyperclip
from libs.Numbers import Number
from requests import Timeout, TooManyRedirects, HTTPError
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QStackedWidget

SUB_MENU_MAX = 175
SUB_MENU_MIN = 0
SUB_MENU_CHECK = 100

VAT_PAN_PATTERN =   "\d{9}"

BASE_API = "https://fastapi-production-c751.up.railway.app"

class UI_Functions:
    def __init__(self) -> None:
        pass
    
    #number utility functions
    def convertNumber(num, frame, _statusBar):
        if num == "":
            _statusBar.setText("Enter the number to convert")
            return
        try:
            num = float(num)
        except ValueError:
            _statusBar.setText("Please input the valid Number!")
        except:
            _statusBar.setText("Input Value Exception Occured!")
        else:
            num = Number(str(num))
            data = num.get_num()
            frame.findChild(QLineEdit, "number_disp").setText(data["num"])
            frame.findChild(QPushButton, "num_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["num"], _statusBar))
            frame.findChild(QLineEdit, "english_disp").setText(data["english"])
            frame.findChild(QPushButton, "eng_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["english"], _statusBar))
            frame.findChild(QLineEdit, "nepali_disp").setText(data["nepali"])
            frame.findChild(QPushButton, "nep_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["nepali"], _statusBar))
            frame.findChild(QLineEdit, "decimal_disp").setText(data["decimal"])
            frame.findChild(QPushButton, "decimal_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["decimal"], _statusBar))
            frame.findChild(QLineEdit, "whole_disp").setText(data["whole"])
            frame.findChild(QPushButton, "whole_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["whole"], _statusBar))
            frame.findChild(QLineEdit, "lakh_format_disp").setText(data["lakh_format"])
            frame.findChild(QPushButton, "lakh_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["lakh_format"], _statusBar))
            frame.findChild(QLineEdit, "million_format_disp").setText(data["million_format"])
            frame.findChild(QPushButton, "million_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["million_format"], _statusBar))
            frame.findChild(QLabel, "words_eng_disp").setText(data["words_eng"])
            frame.findChild(QPushButton, "eng_words_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["words_eng"], _statusBar))
            frame.findChild(QLabel, "words_nep_disp").setText(data["words_nep"])
            frame.findChild(QPushButton, "nep_words_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["words_nep"], _statusBar))
            frame.findChild(QPushButton, "copy_num_all_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data, _statusBar))
            status = f'{data["num"]} is converted!'
            print(status)
            _statusBar.setText(status)
    
    def clearText(_input, _statusBar):
        _input.setText("")
        _statusBar.setText("Inputs are cleared!")
    
    def copyToClipBoard(_content, _statusBar):
        pyperclip.copy(_content)
        _statusBar.setText("Copied to ClipBoard")
        print("Copied to ClipBoard")
    
    def toggleMenu(_menu):
        w = _menu.size().width()
        if w > SUB_MENU_CHECK:
            UI_Functions.showMenu(_menu, False)
        else:
            UI_Functions.showMenu(_menu, True)
    
    def showMenu(_menu, show):
        if not show:
            _menu.setMaximumWidth(SUB_MENU_MIN)
            _menu.setMinimumWidth(SUB_MENU_MIN)
            # print("Hiding Menu")
        else:
            _menu.setMaximumWidth(SUB_MENU_MAX)
            _menu.setMinimumWidth(SUB_MENU_MAX)
            # print("Showing Menu")
            
    def showSubMenu(_index, _frame):
        _w = _frame.size().width()
        _menu = _frame.findChild(QStackedWidget, "submenu_pages")
        _curr = _menu.currentIndex()
        if _curr == _index:
            UI_Functions.toggleMenu(_frame)
            # print("toggling menu!")
        elif _w <= SUB_MENU_CHECK:
            UI_Functions.showMenu(_frame, True)
            _menu.setCurrentIndex(_index)
            # print(f"Showing menu and clicked! {_w}")
        else:
            _menu.setCurrentIndex(_index)
            # print(f"menu clicked! {_w}")
    
    def showPage(_widget, _container):
        _container.setCurrentWidget(_widget)
    
    async def getPan(_session, _pan, _statusBar, _container):
        _api_url = f'{BASE_API}/pan/v1/{_pan}'
        async with _session.get(_api_url) as resp:
                return await resp.json()
    
    async def searchPan(_pan, _statusBar, _output_container):
        if _pan == "":
            _statusBar.setText("Enter the VAT/PAN number to search")
            return
        try:
            if re.match(VAT_PAN_PATTERN, _pan) is None:
                raise ValueError("Number not in VAT/PAN Format!")
            _pan = int(_pan)
        except ValueError as v_err:
            _statusBar.setText(f'Format Error: {str(v_err)}')
        except:
            _statusBar.setText("Input Value Exception Occured!")
        else:
            _statusBar.setText(f'searching details for {_pan}')
            async with aiohttp.ClientSession() as session:
                pan_details = await UI_Functions.getPan(session, _pan, _statusBar, _output_container)
                _output_container.findChild(QLabel, "raw_pan_output").setText(json.dumps(pan_details, indent=4, ensure_ascii=False))
                _statusBar.setText(f'Details fetched Successfully for PAN {_pan}!')