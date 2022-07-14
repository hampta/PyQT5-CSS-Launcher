from PySide2.QtCore import QThread, Signal
from downloader import Downloader

class DownloadWorker(QThread):
    _signal = Signal(int)
    def __init__(self, dir):
        super(DownloadWorker, self).__init__()
        self.downloader = Downloader(dir)

    def run(self):
        self.downloader.download_files()
        print(self.downloader.done)
        self._signal.emit(self.downloader.done)

    def stop(self):
        pass
