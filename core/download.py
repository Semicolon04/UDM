from pathlib import Path
from os.path import join, basename
from urllib.request import urlopen, Request

default_download_path = join(Path.home(), 'Downloads')

STATE_PAUSED = 0
STATE_DOWNLOADING = 1
STATE_COMPLETED = 2
STATE_ERROR = 3

class Download:
    def __init__(self, url, directory=None, filename=None):
        self.source_url = url
        self.directory = directory if directory else default_download_path
        self.filename = filename if filename else basename(url)
        self.total_bytes = self._get_size()
        self.bytes_downloaded = 0
        self.state = STATE_PAUSED
        self.dir_fd = os.open(self.directory, os.O_RDONLY)

    def __str__(self):
        return 'Download from %s to %s' % (self.source_url, self.get_destination_path())

    def _get_size(self):
        request_to_send = Request(self.source_url, method='HEAD')
        return response.getheader('Content-Length')
    
    def get_destination_path(self):
        return join(self.directory, self.filename)

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