import json
import pickle
from env import *

_config = json.load(open("config.json", "r"))

def save():
    global _config
    json.dump(_config, open("config.json", "w"))
    _config = json.load(open("config.json", "r"))


# Modes
def getMode():
    return _config["mode"]

def setMode(mode):
    if mode not in ["PYINSTALLER","MSIX","DEBUG"]:
        raise Exception("Invalid mode")
    else:
        _config["mode"] = mode
        save()

def getInit(obj):
    if obj not in ["conf","player"]:
        raise Exception("Invalid object")
    else:
        if obj == "conf":
            return _config["conf_init"] == "False"
        elif obj == "player":
            return _config["player_init"] == "False"

def setInit(obj, value):
    if obj not in ["conf","player"]:
        raise Exception("Invalid object")
    else:
        if obj == "conf":
            _config["conf_init"] = value
        elif obj == "player":
            _config["player_init"] = value
        save()  

def getLang():
    return _config["settings"]["language"]

def setLang(lang):
    if lang not in "-":
        raise Exception("Invalid language")
    else:
        _config["settings"]["language"] = lang
        save()

def addAllowedUA(ua):
    _config["server"]["Allowed UA"].append(ua)
    save()

def delAllowedUA(ua):
    _config["server"]["Allowed UA"].remove(ua)
    save()

def getAllowedUA():
    return _config["server"]["Allowed UA"]

def addAllowedIP(ip):
    _config["server"]["Allowed IP"].append(ip)
    save()

def delAllowedIP(ip):
    _config["server"]["Allowed IP"].remove(ip)
    save()

def getAllowedIP():
    return _config["server"]["Allowed IP"]

def getGamePath(game):
    return _config["games"][game]["path"]

def setGamePath(game, path):
    _config["games"][game]["path"] = path
    save()

def getBGVersion(game:str) -> int:
    return _config["games"][game]["bg_version"]

def setBGVersion(game:str, version:int):
    _config["games"][game]["bg_version"] = version
    save()

def getLangData(lang) -> dict:
    lang = json.loads(f"data\\language\\{lang}.json")
    return lang

def getPlayerData(player:str):
    player_info = pickle.load(open(f"data\\players\\{player}.uid", "rb"))
    return player_info