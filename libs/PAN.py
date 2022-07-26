import requests
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

BASE_API = "https://fastapi-production-c751.up.railway.app"

REQ_HEADERS = {
    'User-Agent': ''
}

class PAN(QThread):
    status = pyqtSignal(str)
    complete = pyqtSignal(dict)
    def __init__(self, pan = 0):
        super(PAN, self).__init__()
        self.pan = pan
        self.is_running = True
    
    def run(self):
        self.api_url = f'{BASE_API}/pan/v1/{self.pan}'
        QApplication.processEvents()
        self.resp = requests.get(self.api_url)
        QApplication.sendPostedEvents()
        if self.resp.status_code == 200:
            self.details = self.resp.json()
            self.complete.emit(self.details)
            self.update(f'Fetching Completed!')
        else:
            self.complete.emit({'msg': "No Details could be fetched", 'result': False})
    
    def update(self, msg):
        print(f'PAN Update: {msg}')
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating Search for {self.pan}')
        self.terminate()