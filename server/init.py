import sqlite3 as sql
import os
from configparser import ConfigParser
import winreg


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
    if os.path.exists("data.db"):
        pass
    else:
        ysgamepath, srgamepath = get_game_path()
        conn = sql.connect("data.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS game (name text, path text, includes text)"
        )
        cur.execute("CREATE TABLE IF NOT EXISTS config (key text, value text)")
        cur.execute("INSERT INTO game VALUES ('ys', '{}', 'null')".format(ysgamepath))
        cur.execute("INSERT INTO game VALUES ('sr', '{}', 'null')".format(srgamepath))
        conn.commit()
        cur.close()
        conn.close()
