import pyperclip
from lib.Numbers import Number
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QStackedWidget

SUB_MENU_MAX = 175
SUB_MENU_MIN = 0
SUB_MENU_CHECK = 100
class UI_Functions:
    def __init__(self) -> None:
        pass
    
    #number utility functions
    def convertNumber(num, frame, _statusBar):
        # print(num)
        num = Number(num)
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
        else:
            _menu.setMaximumWidth(SUB_MENU_MAX)
            _menu.setMinimumWidth(SUB_MENU_MAX)
            
    def showSubMenu(_index, _frame):
        _w = _frame.size().width()
        _menu = _frame.findChild(QStackedWidget, "submenu_pages")
        _curr = _menu.currentIndex()
        if _curr == _index:
            UI_Functions.toggleMenu(_frame)
        elif _w < SUB_MENU_CHECK:
            UI_Functions.showMenu(_menu, True)
            _menu.setCurrentIndex(_index)
        else:
            _menu.setCurrentIndex(_index)