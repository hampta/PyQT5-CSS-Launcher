import configparser
import os
import sys

from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox)

from config import Config
from downloader import Downloader
from gui import design

__version__ = 0.1


class Launcher(QMainWindow, design.Ui_MainWindow):
    # init the gui and the config
    def __init__(self) -> None:
        super(Launcher, self).__init__(None)
        self.config = Config()
        self.setupUi(self)
        self.exec()
        self.setWindowTitle("CSS Launcher")
        self.downloadButton.clicked.connect(self.download)
        self.nicknameEdit.textEdited.connect(self.set_nick)
        self.clanEdit.textEdited.connect(self.set_clan)
        self.playButton.clicked.connect(self.play)
        self.is_downloading = False

    def exec(self):
        config = configparser.ConfigParser()
        if self.__is_installed():
            config.read(self.config.dir+self.config.app_cfg)
            self.game_dir = config.get("launcher", "installed_dir")
            self.downloadButton.setText("Validate")
        else:
            self._extracted_from_exec_4(config)
        self._game_cfg = f"{self.game_dir}/rev.ini"
        if os.path.exists(self._game_cfg):
            self.load_nick_clan()
        self.work = Downloader(self.game_dir)
        self.check_new_version()

    # TODO Rename this here and in `exec`
    def _extracted_from_exec_4(self, config):
        QMessageBox.warning(self, "Game not installed!",
                            "Select installation folder")
        self.game_dir = QFileDialog.getExistingDirectory(
            self) + "/Counter-Stike Source/"
        if not os.path.exists(self.game_dir):
            os.makedirs(self.game_dir)
        if not os.path.exists(self.config.dir):
            os.makedirs(self.config.dir)
        config.add_section("launcher")
        config.set("launcher", "version", str(__version__))
        config.set("launcher", "installed_dir", self.game_dir)
        with open(self.config.dir+self.config.app_cfg, "w") as config_file:
            config.write(config_file)
        self.playButton.setEnabled(False)

    def download(self):
        if not self.is_downloading:
            self.is_downloading = True
            self.playButton.setEnabled(False)
            self.work._file_status.connect(self.progressbar_file)
            self.work._downloading_status.connect(self.progressbar_all)
            self.work._file_downloaded.connect(self.progress_file)
            self.work._downloading_info.connect(self.progress_info)
            self.downloadButton.setText("Stop")
            self.work.start()
        else:
            self.is_downloading = False
            self.work.stop()

    def play(self):
        with open(self._game_cfg, "w") as config_file:
            self.game_cfg.write(config_file)
        if not self.work.play():
            QMessageBox.warning(
                self, "Warning!", "Game not installed!\nPlease download")
        else:
            self.showMinimized()

    def load_nick_clan(self):
        self.game_cfg = configparser.ConfigParser()
        self.game_cfg.read(self._game_cfg)
        self.nicknameEdit.setText(
            self.game_cfg.get("steamclient", "PlayerName"))
        self.clanEdit.setText(self.game_cfg.get("steamclient", "ClanTag"))

    def set_nick(self):
        self.game_cfg.set("steamclient", "PlayerName",
                          self.nicknameEdit.text())

    def set_clan(self):
        print(self.clanEdit.text())
        self.game_cfg.set("steamclient", "ClanTag", self.clanEdit.text())

    def check_new_version(self):
        if self.work.new_version:
            reply = QMessageBox.question(self, "A new version of the game has been released", "Do you want to update it?",
                                         QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.download()
            else:
                return

    def progressbar_file(self, msg):
        self.onefileBar.setValue(msg)

    def progressbar_all(self, msg):
        if msg > 99:
            self.allfilesBar.setDisabled(True)
            self.playButton.setEnabled(True)
            self.load_nick_clan()
            self.downloadButton.setText("Download")
        self.allfilesBar.setValue(msg)

    def progress_file(self, msg):
        self.filecheckL.setEnabled(True)
        self.filecheckL.setText(msg)

    def progress_info(self, msg):
        self.checkinfoL.setEnabled(True)
        self.checkinfoL.setText(
            "Downloaded: %i Validated: %i All: %i" % (msg[0], msg[1], msg[2]))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.work.stop()
            event.accept()
        else:
            event.ignore()

    def __is_installed(self):
        return os.path.exists(self.config.dir+self.config.app_cfg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Launcher()
    w.show()
    sys.exit(app.exec_())
