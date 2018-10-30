from pathlib import Path

import os
import requests

homepath = os.getcwd()+ "/files"

STATE_PAUSED = 0
STATE_DOWNLOADING = 1
STATE_COMPLETED = 2
STATE_ERROR = 3

class Download:
    def __init__(self, url, directory=homepath, filename=None):
        self.url = url
        self.directory = directory
        self.filename = filename if filename else os.path.basename(url)
        self.total_byes = self._get_size()
        self.bytes_downloaded = 0
        self.state = STATE_PAUSED
        self.dir_fd = os.open(self.directory, os.O_RDONLY)

    def _get_size(self):
        pass

    def opener(self, path, flags):
        return os.open(path, flags, dir_fd=self.dir_fd)

    def _create_file(self, content):
        open(self.filename, 'wb', opener=self.opener).write(content.content)

    def start_downloading(self):
        content = requests.get(self.url, allow_redirects=True)
        self._create_file(content)

    def pause_downloading():
        pass

    def resume_downloading():
        pass