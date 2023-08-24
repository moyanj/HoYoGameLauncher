from flask import Flask, request, send_from_directory, render_template  # flask
import os  # 系统操作
import lib.init as inits  # 函数
import json  # json解析
import api
import traceback
from lib import debug as dbg
from api.env import *
from env import *
from views import data,settings,init

# 初始化一些文件夹
try:
    os.mkdir("log")  # 日志文件夹
    os.mkdir("plugins")  # 日志文件夹
except:
    pass

log.add(
    "log/flask.log",
    level="DEBUG",
)


# 初始化一些全局变量
avatarID = json.load(open("data/avatar.json", "r", encoding="utf-8"))  # 角色头像表
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # 程序文件路径
# print = log.debug


# 初始化Flask
app = Flask(__name__, template_folder=save_path + "/html/")
inits.main()
plugin = plu.load_plugins("plugins")
# 创建配置对象
conf = Config("config.json")
app.register_blueprint(data.app)
app.register_blueprint(settings.app)
app.register_blueprint(init.app)

@app.errorhandler(404)
def error_404(e):
    return f"该页面不存在", 404

@app.errorhandler(Exception)
def error_500(e):
    print(e)
    stack_trace = traceback.format_exc()
    dbg.crash(stack_trace, app)
    return f"未知错误，错误日志位于{save_path}\debug.txt", 500


@app.before_request
def before_request():
    """
    验证请求
    """

    plugin_return = plu.run_funcion(plugin, "before_request", request)
    UA = request.headers.get("User-Agent")
    ip = request.remote_addr
    allowed_ua = conf.get_allowed_ua()
    allowed_ip = conf.get_allowed_ip()
    for i in plugin_return:
        if not i or ip not in allowed_ip or UA not in allowed_ua:
            log.warning("接收到一个不正常的请求：")
            return "This is not a request from HoYoGameLauncher", 403
    log.info(f"method:{request.method}  path:{request.path}  IP:{request.remote_addr}")


@app.route("/")
def index():
    lang = conf.get_language()
    try:
        data = json.load(open("data\language\{}.json".format(lang), encoding="utf-8"))
    except:
        data = json.load(open("data\language\zh-cn.json", encoding="utf-8"))
    plugins_info = plu.get_plugin_info(plugin)
    return render_template("index.html", lang=data, plugins=plugins_info)


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


@app.route("/files/<path:filename>")
def getfile(filename):
    """
    静态文件
    """
    return (send_from_directory(save_path + "/html/static/", filename), 200)


@app.route("/settings/<key>/<val>")
def settings(key, val):
    if key == "language":
        conf.set_language(val)
    return "success"


@app.route("/bg/ys")
def bg_ys():
    return api.get_ysbg()


@app.route("/bg/sr")
def bg_srr():
    return api.get_srbg()

# 此函数会引发TypeError
@app.route("/test/hsr")
def bg_srrs():
    return api


@app.route("/plu/<path:url>")
def pluurl(url):
    url = str(url)
    plu_name = url.split("/")[0]
    data = plu.run_one_funcion(plugin, plu_name, "main_route", request)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=False)
