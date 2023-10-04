from flask import Blueprint, redirect, jsonify
from env import *
import requests as r  # 网络请求

app = Blueprint("data", __name__, url_prefix="/get")


@app.route("/gamepath")
def getgamepath():
    """
    获取所有游戏的路径
    """
    data = {
        "ys": conf.get_game_path("ys"),
        "sr": conf.get_game_path("sr"),
    }
    return data


@app.route("/lang")
def langs():
    filenamelist = os.listdir("data/language")
    outlist = []
    for file in filenamelist:
        d = file.split(".")
        outlist.append(d[0])
    return outlist


@app.route("/language")
def get_language():
    return conf.get_language()


@app.route("/username")
def username():
    """
    获取用户名
    """
    user = conf.get_player_username()
    if user == "unknown":
        uid = conf.get_player_uid()
        if uid == "unknown":
            return "旅行者"
        else:
            data = r.get("https://profile.microgg.cn/api/uid/{}".format(uid))
            data = json.loads(data.text)
            # print(data)
            name = data["playerInfo"]["nickname"]
            conf.set_player_username(name)
            return name
    else:
        return user


@app.route("/avatar")
def getavatar():
    """
    获取头像
    """
    if os.path.exists("html/static/images/avatar.png"):
        return redirect("/files/images/avatar.png")
    else:
        global avatarID
        uid = conf.get_player_uid()
        if uid == "unknown":
            return redirect("https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png")
        else:
            data = r.get("https://profile.microgg.cn/api/uid/{}/?info".format(uid))
            data = json.loads(data.text)
            # print(data)
            avatar = data["playerInfo"]["profilePicture"]["avatarId"]
            url = avatarID[str(avatar)]
            data = r.get(url)
            with open("html/static/images/avatar.png", "wb") as f:
                f.write(data.content)
            return redirect("/files/images/avatar.png")

@app.route("/ver")
def getVer():
    return Rest(data=HOYOGAMELAUNCHER_VERSION)