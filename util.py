# Minhas classes
import json
import os
import platform


class AutoDict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


class ConfigBase:
    def __init__(self, filename: str = ''):
        if filename:
            self._load_config(filename)

    def _load_config(self, filename: str):
        with open(filename, 'r') as f:
            config_data = json.load(f)

        for key in config_data:
            setattr(self, key, config_data[key])


# Utilitários e funções gerais
def check_system() -> dict:
    if platform.system() == 'Windows':
        sl = '\\'
        sys = 'windows'
        ffmpeg = 'ffmpeg.exe'
        mp4box = 'C:\\"Program Files"\\GPAC\\MP4Box.exe'
        mp4client = 'C:\\"Program Files"\\GPAC\\MP4Client.exe'
        kvazaar = 'bin\\kvazaar.exe'
        siti = 'bin\\SITI.exe'
    else:
        sl = '/'
        sys = 'unix'
        ffmpeg = 'ffmpeg'
        mp4box = 'MP4Box'
        kvazaar = 'kvazaar'
        siti = 'bin/siti'
        mp4client = 'MP4Client'

    programs = dict(sl=sl,
                    sys=sys,
                    ffmpeg=ffmpeg,
                    mp4box=mp4box,
                    kvazaar=kvazaar,
                    siti=siti,
                    mp4client=mp4client)
    return programs


def save_json(obj: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=2)


def load_json(filename: str = 'times.json') -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def show_json(obj: dict, show=True, ret=True):
    output = json.dumps(obj, indent=2)
    if show:
        print(output)
    if ret:
        return output


def makedir(dirname: str):
    os.makedirs(dirname, exist_ok=True)
