import requests as r
from flask import redirect
import json
from lib.config import Config
from api import endpoint as ep

conf = Config("config.json")


def get_ysbg():
    print(ep.LauncherContent("ys"))
    req = r.get(ep.LauncherContent("ys"))
    datas = json.loads(req.text)
    all_data = datas["data"]
    adv = all_data["adv"]
    bg = adv["background"]
    bd_ver = conf.get_game_version("ys")
    if bd_ver < int(adv["version"]):
        with open("static/images/ys_bg.png", "wb") as f:
            bg_content = r.get(bg).content
            f.write(bg_content)
            f.close()
            conf.set_game_version(int(adv["version"]), "ys")
        return redirect("/files/images/ys_bg.png")
    else:
        return redirect("/files/images/ys_bg.png")


def get_srbg():
    req = r.get(ep.LauncherContent("sr"))
    print(ep.LauncherContent("sr"))
    datas = json.loads(req.text)
    all_data = datas["data"]
    adv = all_data["adv"]
    bg = adv["background"]
    bd_ver = conf.get_game_version("sr")
    if bd_ver < int(adv["version"]):
        with open("static/images/sr_bg.png", "wb") as f:
            bg_content = r.get(bg).content
            f.write(bg_content)
            f.close()
            conf.set_game_version(int(adv["version"]), "sr")
        return redirect("/files/images/sr_bg.png")
    else:
        return redirect("/files/images/sr_bg.png")
