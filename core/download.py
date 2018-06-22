from pathlib import Path
from os.path import join, basename


homepath = Path.home()

STATE_PAUSED = 0
STATE_DOWNLOADING = 1
STATE_COMPLETED = 2
STATE_ERROR = 3

class Download:
    def __init__(self, url, directory=None, filename=None):
        self.url = url
        self.directory = directory if directory else homepath
        self.filename = filename if filename else basename(url)
        self.total_byes = self._get_size()
        self.bytes_downloaded = 0
        self.state = STATE_PAUSED

    def _get_size(self):
        pass
    
    def _create_file(self):
        pass
    
    def start_downloading(self):
        pass
    
    def pause_downloading():
        pass
    
    def resume_downloading():
        pass