from PIL import Image
from pytesseract import pytesseract
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal, QSettings


class Image2Text(QThread):
    completed = pyqtSignal(str)
    status = pyqtSignal(str)
    def __init__(self, image):
        super(Image2Text, self).__init__()
        self.initSettings()
        self.image = image
        self.result = ""
        self.is_running = True
        pytesseract.tesseract_cmd = self.settings.value('TESSERACT_EXE_PATH')
        
    def initSettings(self):
        self.settings = QSettings('BR Solutions', 'AI')
        self.settings.setValue('TESSERACT_EXE_PATH', "C:\\Users\\A00172\\AppData\\Local\\Tesseract-OCR\\tesseract.exe")
        self.app_settings = QSettings('BR Solutions', 'Maya_Utility_App')
        
    def run(self):
        self.update(f'Started: Extraction for {self.image} started!')
        QApplication.processEvents()
        #Open image with PIL
        img = Image.open(self.image)
        
        #Extract text from image
        try:
            self.result = pytesseract.image_to_string(img)
        except pytesseract.TesseractNotFoundError as e:
            self.update(f'Tesseract Not Found: {e}')
            print(e)
        else:
            self.update(f'Complete: Extraction for {self.image} finished successfully!')
            self.completed.emit(self.result)
    
    def update(self, msg):
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating: Terminating Extraction for {self.image}')
        self.terminate()