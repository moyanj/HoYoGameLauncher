import requests as r
from flask import redirect
import json
from api import endpoint as ep
import json
import lib
from env import *


def get_ysbg():
    req = r.get(ep.LauncherContent("ys"))
    datas = json.loads(req.text)
    all_data = datas["data"]
    adv = all_data["adv"]
    bg = adv["background"]
    bd_ver = conf.getBGVersion("ys")
    if bd_ver < int(adv["version"]):
        with open("html/static/images/ys_bg.png", "wb") as f:
            bg_content = r.get(bg).content
            f.write(bg_content)
            f.close()
            conf.setBGVersion("ys", int(adv["version"]))
        return redirect("/files/images/ys_bg.png")
    else:
        return redirect("/files/images/ys_bg.png")


def get_srbg():
    req = r.get(ep.LauncherContent("sr"))
    datas = json.loads(req.text)
    all_data = datas["data"]
    adv = all_data["adv"]
    bg = adv["background"]
    bd_ver = conf.getBGVersion("sr")
    if bd_ver < int(adv["version"]):
        with open("html/static/images/sr_bg.png", "wb") as f:
            bg_content = r.get(bg).content
            f.write(bg_content)
            f.close()
            conf.setBGVersion("sr", int(adv["version"]))
        return redirect("/files/images/sr_bg.png")
    else:
        return redirect("/files/images/sr_bg.png")


def get_ltoken(cookie: str):
    login = lib.load_cookie(cookie)
    login_ticket = login["login_ticket"]
    login_uid = login["login_uid"]
    ltmid_v2 = login["ltmid_v2"]
    url = ep.Ltoken()
    req = r.get(
        url, {"token_types": "2", "login_ticket": login_ticket, "uid": login_uid}
    )
    ltoken = json.loads(req.text)["data"]["list"][0]["token"]
    ck = f"ltoken={ltoken}; ltuid={ltmid_v2};"
    return ck
