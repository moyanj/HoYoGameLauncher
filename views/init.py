from flask import Blueprint, redirect, jsonify, request
from env import *
import requests as r  # 网络请求

app = Blueprint("init", __name__)


@app.route("/init", methods=["GET"])
def info_init():
    """
    初始化信息
    """
    str_uid = request.args.get("uid", "unknown")
    conf.set_player_uid(str_uid)
    player = Player(str_uid)
    player.dump(f"data\player\{str_uid}")
    conf.set_player_initialized(True)
    try:
        os.remove("static/images/avatar.png")
    except:
        pass
    return "ok"


@app.route("/ifinit")
def ifinit():
    """
    判断是否初始化
    """
    if conf.is_player_initialized():
        return "ok"
    else:
        return "not ok"
