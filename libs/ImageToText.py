from PIL import Image
from pytesseract import pytesseract
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

TESSERACT_EXE_PATH = "C:\\Users\\A00172\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

class Image2Text(QThread):
    completed = pyqtSignal(str)
    status = pyqtSignal(str)
    def __init__(self, image):
        super(Image2Text, self).__init__()
        self.image = image
        self.result = ""
        self.is_running = True
        pytesseract.tesseract_cmd = TESSERACT_EXE_PATH
        
    def run(self):
        self.update(f'Extraction for {self.image} started!')
        QApplication.processEvents()
        #Open image with PIL
        img = Image.open(self.image)
        
        #Extract text from image
        self.result = pytesseract.image_to_string(img)
        self.update(f'Extraction for {self.image} finished successfully!')
        self.completed.emit(self.result)
    
    def update(self, msg):
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating Extraction for {self.image}')
        self.terminate()