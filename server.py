from flask import (
    Flask,
    request,
    send_from_directory,
    redirect,
    render_template,
    jsonify,
)  # flask
import os  # 系统操作
import tools.init as init  # 函数
import requests as r  # 网络请求
import json  # json解析
import sys  # 我也不知道
from tools.config import Config  # 配置
import tools.api as api
from loguru import logger as log
from tools import plugin as plu



# 初始化一些文件夹
try:
    os.mkdir("log")  # 日志文件夹
    os.mkdir("plugins")  # 日志文件夹
except:
    pass

log.add(
    "log/flask.log",
    rotation="1 days",
    retention="7 days",
    level="DEBUG",
    compression="zip",
)


# 初始化一些全局变量
avatarID = json.load(open("static/avatar.json", "r", encoding="utf-8"))  # 角色头像表
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # 程序文件路径
print = log.debug


# 初始化Flask
app = Flask(__name__, template_folder=save_path + "/html/")

# 配置文件初始化
init.main()
plugin = plu.load_plugins("plugins")
# 创建配置对象
conf = Config("config.json")

@app.before_request
def before_request():
    """
    验证请求
    """
    plu.run_funcion(plugin, "hello")
    UA = request.headers.get("User-Agent")
    ip = request.remote_addr
    allowed_ua = conf.get_allowed_ua()
    allowed_ip = conf.get_allowed_ip()
    if ip not in allowed_ip or UA not in allowed_ua:
        log.warning("接收到一个不正常的请求：")
        return "This is not a request from HoYoGameLauncher", 403
    log.info(f"method:{request.method}  path:{request.path}  IP:{request.remote_addr}")


@app.route("/")
def index():
    lang = conf.get_language()
    try:
        data = json.load(open("language\{}.json".format(lang), encoding="utf-8"))
    except:
        data = json.load(open("language\zh-cn.json", encoding="utf-8"))
    return render_template("index.html", lang=data)


@app.route("/init", methods=["GET"])
def info_init():
    """
    初始化信息
    """
    uid = request.args.get("uid", "unknown")
    conf.set_player_uid(uid)
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


@app.route("/run/<game>")
def game(game):
    """
    运行游戏
    """
    # 查询游戏路径
    gamepath = conf.get_game_path(game)
    # 提取信息
    file = os.path.basename(gamepath)
    path = os.path.dirname(gamepath)
    panfu = gamepath.split(":")[0] + ":"
    # 运行
    os.system("{} && cd {} && dir && {}".format(panfu, path, file))
    return "RUN OK"


@app.route("/post/gamepath")
def postgamepath():
    """
    修改游戏路径
    """
    gamepath = request.args.get("gamepath")
    game = request.args.get("game")
    conf.set_game_path(gamepath, game)
    return "OK"


@app.route("/get/gamepath/<game>")
def getonegamepath(game):
    """
    获取一个游戏的路径
    """
    i = conf.get_game_path(game)
    return i


@app.route("/get/gamepath")
def getgamepath():
    """
    获取所有游戏的路径
    """
    data = {
        "ys": conf.get_game_path("ys"),
        "sr": conf.get_game_path("sr"),
    }
    return data


@app.route("/files/<path:filename>")
def getfile(filename):
    """
    静态文件
    """
    return (send_from_directory(save_path + "/static/", filename), 200)


@app.route("/avatar")
def getavatar():
    """
    获取头像
    """
    if os.path.exists("static/images/avatar.png"):
        return redirect("/files/images/avatar.png")
    else:
        global avatarID
        uid = conf.get_player_uid()
        if uid == "unknown":
            return redirect("https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png")
        else:
            data = r.get("https://enka.network/api/uid/{}/?info".format(uid))
            data = json.loads(data.text)
            # print(data)
            avatar = data["playerInfo"]["profilePicture"]["avatarId"]
            url = avatarID[str(avatar)]
            data = r.get(url)
            with open("static/images/avatar.png", "wb") as f:
                f.write(data.content)
            return redirect("static/images/avatar.png")


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
            data = r.get("https://enka.network/api/uid/{}/?info".format(uid))
            data = json.loads(data.text)
            # print(data)
            name = data["playerInfo"]["nickname"]
            conf.set_player_username(name)
            return name
    else:
        return user


@app.route("/get/lang")
def langs():
    filenamelist = os.listdir("language")
    outlist = []
    for file in filenamelist:
        d = file.split(".")
        outlist.append(d[0])
    return jsonify(outlist)


@app.route("/settings/<key>/<val>")
def settings(key, val):
    if key == "language":
        conf.set_language(val)
    return "success"


@app.route("/get/language")
def get_language():
    return conf.get_language()


@app.route("/bg/ys")
def bg_ys():
    return api.get_ysbg()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
