from PyQt5.QtWidgets import QMessageBox

class Alert(QMessageBox):
    def __init__(self, CONFIG = {}):
        super().__init__()