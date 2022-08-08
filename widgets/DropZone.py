from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox

IMAGE_HEIGHT = 150

class DropZone(QFrame):
    loaded = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.file_paths = []
    
    def add_image(self):
        # print(self.file_paths)
        layout = self.findChild(QFrame, "image_drop_border").layout()
        for image in self.file_paths:
            image_viewer = self.findChild(QLabel, "Image_Label")
            image_viewer.setPixmap(QtGui.QPixmap(image).scaledToHeight(IMAGE_HEIGHT))
            image_viewer.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(image_viewer)
        self.loaded.emit({"msg": "Image Loaded", "files": self.file_paths})
    
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
            self.file_paths = [url.toLocalFile() for url in event.mimeData().urls()]
            self.add_image()
            event.accept()
        else:
            event.ignore()
    