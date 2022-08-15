import requests
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

BASE_API = "https://zenquotes.io/api/random"

REQ_HEADERS = {
    'User-Agent': ''
}

class Quote(QThread):
    status = pyqtSignal(str)
    complete = pyqtSignal(dict)
    def __init__(self, mood = "motivational"):
        super(Quote, self).__init__()
        self.mood = mood
        self.is_running = True
    
    def run(self):
        self.api_url = f'{BASE_API}/'
        QApplication.processEvents()
        self.update(f'Fetching random quote...')
        self.resp = requests.get(self.api_url)
        QApplication.sendPostedEvents()
        if self.resp.status_code == 200:
            self.quote = self.resp.json()[0]
            self.complete.emit(self.quote)
            self.update(f'Fetching Completed!')
        else:
            self.complete.emit({'msg': "No Details could be fetched", 'result': False})
    
    def update(self, msg):
        msg = f'Quotes Update: {msg}'
        self.status.emit(msg)
    
    def stop(self):
        self.is_running = False
        self.update(f'Terminating Search for {self.mood} Quote')
        self.terminate()