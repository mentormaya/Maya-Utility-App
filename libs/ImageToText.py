from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

class Image2Text(QThread):
    completed = pyqtSignal(str)
    status = pyqtSignal(str)
    def __init__(self, image):
        super(Image2Text, self).__init__()
        self.image = image
        self.result = ""
        self.is_running = True
        
    def run(self):
        self.update(f'Extraction for {self.image} started!')
        QApplication.processEvents()
        self.completed.emit(f'Extraction for {self.image} finished successfully!')
    
    def update(self, msg):
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating Extraction for {self.image}')
        self.terminate()