from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox

class DropZone(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
    
    def add_image(self, file_paths):
        print(file_paths)
        image_viewer = QLabel("Image will be here!")
        image_viewer.setPixmap(QtGui.QPixmap(file_paths[0]))
        layout = QVBoxLayout(self.findChild(QFrame, "image_drop_border"))
        layout.addWidget(image_viewer)
    
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
            file_paths = [url.toLocalFile() for url in event.mimeData().urls()]
            self.add_image(file_paths)
            event.accept()
        else:
            event.ignore()
    