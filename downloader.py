from typing import Dict
import requests
import configparser
import io
import lzma
import os
import subprocess
from zlib import crc32
import shutil
import pathlib
from PySide2.QtCore import QThread, Slot, Signal
from config import Config

class Downloader(QThread):
    _file_status = Signal(int)
    _file_downloaded = Signal(str)
    _downloading_status = Signal(int)
    _downloading_info = Signal(list)

    def __init__(self, dir):
        QThread.__init__(self)
        self.config_name = Config.game_cfg
        self.config_url = Config.url
        self.dir = dir
        self.config_dir = f"{self.dir}/{self.config_name}"
        # self.__exec_app_config()
        # "filename: [weight, hash CRC-32]"
        self.updated_config, self.file_list_url, self.download_url = self.__update_config()
        self.cur_config = self.__load_cur_config()
        self.file_list = self.__load_file_list()
        self.temp = self.__create_temp()
        self.new_version = self.__check_game_version()
        self.done = 0
        self.isRunning = True

    def __del__(self):
        self.wait()

    def run(self):
        self.download_files()

    def stop(self):
        self.isRunning = False

    def create_dirs(self):
        for dir, [weight, ___] in self.file_list.items():
            dir = f"{self.dir}/{dir}"
            if not weight and not os.path.exists(dir):
                os.makedirs(dir)

    @Slot()
    def play(self):
        exe_ = f"{self.dir}/{self.cur_config['naz1']['run']}"
        if not os.path.exists(exe_):
            return False
        subprocess.Popen(exe_)
        return True

    def download_files(self):
        self.create_dirs()
        weight_all = self.__weight_all()
        dl = 0
        #Downloaded , checked, all
        cl = [0, 0, len(self.file_list)]
        for file, [weight, hash] in self.file_list.items():
            if weight and self.__file_check(f"{self.dir}{file}", hash) and self.isRunning:
                self.__download_file(file)
                cl[0] += 1
            else:
                cl[1] += 1
            dl += weight
            st = (100 * dl / weight_all)
            self._file_downloaded.emit(file)
            self._downloading_status.emit(st)
            self._downloading_info.emit(cl)
        with open(f"{self.dir}/{self.config_name}", "w") as f:
            self.updated_config.write(f)
            if not os.path.exists(self.config_dir):
                os.makedirs(self.config_dir)
            
    def __weight_all(self):
        return sum(w for ____, [w, ____] in self.file_list.items())

    def __update_config(self):
        config = configparser.ConfigParser()
        r = requests.get(self.config_url).text
        buf = io.StringIO(r)
        config.read_file(buf)
        file_list_url = f"{config['naz1']['adrskach1']}/{config['naz1']['nazcek1']}.dim.lzma"
        return config, file_list_url, config['naz1']['adrskach1']

    def __load_cur_config(self):
        if os.path.exists(self.dir) and os.path.exists(self.config_dir):
            config = configparser.ConfigParser()
            config.read(self.config_dir)
            return config
        else:
            with open(self.config_dir, "w") as f:
                self.updated_config.write(f)
                f.close()
            return self.updated_config

    def __check_game_version(self):
        cur_config = configparser.ConfigParser()
        cur_config.read(f"{self.dir}/{self.config_name}")
        cur_version, cur_build, cur_update, cur_data = cur_config["naz1"]["ver1"].split(
            " ")
        upd_version, upd_build, upd_update, upd_data = self.updated_config["naz1"]["ver1"].split(
            " ")
        if upd_version > cur_version or upd_update > cur_update or upd_build > cur_build or upd_data > cur_data:
            return True
        return False

    def __load_file_list(self):
        r = requests.get(self.file_list_url)
        dim = lzma.decompress(r.content).decode("utf-8").split("\n")
        return {dim[i].replace("\r", "").replace("\\", "/"): [int(dim[i - 1]), int(dim[i + 1])] for i in range(1, len(dim), 3)}

    def __create_temp(self):
        temp = os.getenv("TEMP") + "/"
        temp_ = "./temp/.cache"
        if not temp and not os.path.exists(temp_):
            os.makedirs(temp_)
            return temp_
        return temp

    def __file_check(self, file, hash):
        if not os.path.exists(file) or self.__calculate_hash(file, hash):
            return True

    def __calculate_hash(self, fileName, hash):
        prev = 0
        for eachLine in open(fileName, "rb"):
            prev = crc32(eachLine, prev)
        return (prev != hash)

    def __download_file(self, file_name):
        temp_file = self.temp + pathlib.Path(f"{file_name}.lzma").name
        with open(temp_file, "wb") as f:
            file_lenght = requests.head(
                f"{self.download_url}/{file_name}.lzma").headers["content-length"]
            response = requests.get(
                f"{self.download_url}/{file_name}.lzma", stream=True)
            dl = 0
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(100 * dl / int(file_lenght))
                self._file_status.emit(done)
                #sys.stdout.write("\r[%s%s]" % ('=' * self.done, ' ' * (50-self.done)))
                # sys.stdout.flush()

        with lzma.open(temp_file) as compressed:
            output_path = pathlib.Path(f"{self.dir}{file_name}")
            with open(output_path, 'wb') as destination:
                shutil.copyfileobj(compressed, destination)
        os.remove(temp_file)
