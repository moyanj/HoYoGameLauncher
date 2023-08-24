from configparser import ConfigParser
import winreg
from lib.config import Config
from lib import tool
import requests as r

conf = Config("config.json")


def get_Reg_key(path, key_):
    reg_root = winreg.HKEY_LOCAL_MACHINE
    reg_path = path
    reg_flags = winreg.KEY_READ
    key = winreg.OpenKey(reg_root, reg_path, 0, reg_flags)
    value, key_type = winreg.QueryValueEx(key, key_)
    winreg.CloseKey(key)
    return value


def raedini(path):
    conf = ConfigParser()
    conf.read(path)
    return conf


def get_game_path():
    try:
        yslunpath = get_Reg_key(
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\原神", "InstallPath"
        )
    except:
        ys = False
        ysgamepath = "C:\\Program Files\\Genshin Impact\\Game\\YuanShen.exe"
    else:
        ys = True

    try:
        srlunpath = get_Reg_key(
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\崩坏：星穹铁道",
            "InstallPath",
        )
    except:
        sr = False
        ysgamepath = "C:\\Program Files\\Genshin Impact\\Game\\YuanShen.exe"
    else:
        sr = True

    if ys:
        # 读取配置文件
        f = raedini(yslunpath + "\\config.ini")
        ysgamepath = (
            f["launcher"]["game_install_path"] + "/" + f["launcher"]["game_start_name"]
        )
    if sr:
        f = raedini(srlunpath + "\\config.ini")
        srgamepath = (
            f["launcher"]["game_install_path"] + "/" + f["launcher"]["game_start_name"]
        )

    return ysgamepath, srgamepath


def main():
    """
    hasc
    """
    if not conf.is_conf_initialized():
        ysgamepath, srgamepath = get_game_path()
        conf.set_game_path(ysgamepath, "ys")
        conf.set_game_path(srgamepath, "sr")
        key = tool.generate_random_key(32)
        conf.set_auth_key(key)
        conf.set_conf_initialized(True)
