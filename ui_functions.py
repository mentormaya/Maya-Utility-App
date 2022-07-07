from lib.Numbers import Number
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton
class UI_Functions:
    def __init__(self) -> None:
        pass
    
    #number utility functions
    def convertNumber(num, frame):
        # print(num)
        num = Number(num)
        data = num.get_num()
        frame.findChild(QLineEdit, "number_disp").setText(data["num"])
        frame.findChild(QPushButton, "num_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["num"]))
        frame.findChild(QLineEdit, "english_disp").setText(data["english"])
        frame.findChild(QPushButton, "eng_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["english"]))
        frame.findChild(QLineEdit, "nepali_disp").setText(data["nepali"])
        frame.findChild(QPushButton, "nep_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["nepali"]))
        frame.findChild(QLineEdit, "decimal_disp").setText(data["decimal"])
        frame.findChild(QPushButton, "decimal_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["decimal"]))
        frame.findChild(QLineEdit, "whole_disp").setText(data["whole"])
        frame.findChild(QPushButton, "whole_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["whole"]))
        frame.findChild(QLineEdit, "lakh_format_disp").setText(data["lakh_format"])
        frame.findChild(QPushButton, "lakh_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["lakh_format"]))
        frame.findChild(QLineEdit, "million_format_disp").setText(data["million_format"])
        frame.findChild(QPushButton, "million_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["million_format"]))
        frame.findChild(QLabel, "words_eng_disp").setText(data["words_eng"])
        frame.findChild(QPushButton, "eng_words_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["words_eng"]))
        frame.findChild(QLabel, "words_nep_disp").setText(data["words_nep"])
        frame.findChild(QPushButton, "nep_words_copy_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data["words_nep"]))
        frame.findChild(QPushButton, "copy_num_all_btn").clicked.connect(lambda: UI_Functions.copyToClipBoard(data))
    def clearText(_input):
        _input.setText("")
    
    def copyToClipBoard(_content):
        print(_content)