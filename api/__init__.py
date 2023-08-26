import requests as r
from flask import redirect
import json
from lib.config import Config
from api import endpoint as ep
import json
import lib

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
        with open("html/static/images/ys_bg.png", "wb") as f:
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
        with open("html/static/images/sr_bg.png", "wb") as f:
            bg_content = r.get(bg).content
            f.write(bg_content)
            f.close()
            conf.set_game_version(int(adv["version"]), "sr")
        return redirect("/files/images/sr_bg.png")
    else:
        return redirect("/files/images/sr_bg.png")


def upload_hutao():
    url = ep.HuTaoUpload(False)

    payload = "<body data here>"
    headers = {
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json",
    }

    response = r.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_ltoken(cookie: str):
    login = lib.load_cookie(cookie)
    login_ticket = login["login_ticket"]
    login_uid = login["login_uid"]
    ltmid_v2 = login["ltmid_v2"]
    req = r.get(
        ep.Ltoken, {"token_types": "2", "login_ticket": login_ticket, "uid": login_uid}
    )
    ltoken = json.loads(req.text)["data"]["list"][0]["token"]
    ck = f"ltoken={ltoken}; ltuid={ltmid_v2};"
    return ck
