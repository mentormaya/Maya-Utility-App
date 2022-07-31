from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QCheckBox

class DropZone(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
    
    def set_image(self, file_path):
        self.setPixmap(QtGui.QPixmap(file_path))
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            # self.set_image(file_path)

            event.accept()
        else:
            event.ignore()
    