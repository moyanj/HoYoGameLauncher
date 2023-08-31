from flask import Flask, request, send_from_directory, render_template  # flask
import os  # 系统操作
import lib.init as inits  # 函数
import json  # json解析
import api
from api.env import *
from env import *
from views import data, settings, init
import traceback
from lib import debug as dbg

# 初始化Flask
app = Flask(__name__, template_folder=save_path + "/html/")
# 初始化程序
inits.main()
# 注册蓝图
app.register_blueprint(data.app)
app.register_blueprint(settings.app)
app.register_blueprint(init.app)


# 一大堆错误处理
@app.errorhandler(404)
def error_404(e):
    return f"该页面不存在", 404


@app.errorhandler(Exception)
def error_500(e):
    print(e)
    stack_trace = traceback.format_exc()
    dbg.crash(stack_trace, app)
    return f"未知错误，错误日志位于{save_path}\debug.txt", 500


# 加载玩家列表
PlayerList = []
for filename in os.listdir("data/player"):
    print("data/player/" + filename)
    play = Player("111111")
    name = "data/player/" + filename
    PlayerList.append(play.load(name=name))



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
    '''
    for i in plugin_return:
        if not i or ip not in allowed_ip or UA not in allowed_ua:
            log.warning("接收到一个不正常的请求：")
            return "This is not a request from HoYoGameLauncher", 403
    '''
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


@app.route("/<path:url>")
def pluurl(url):
    url = str(url)
    plu_name = url.split("/")
    plu_len = len(plu_name)
    if plu_len == 1:
        print(0)
        print(plu_name[0])
        data = plu.run_one_funcion(plugin, str(plu_name[0]), "route_main", request)
        print(data)
        return data
    elif plu_name[1] == "files":
        print(2)
        data = plu.run_one_funcion(plugin, str(plu_name[0]), "route_files", request)
        return data
    else:
        print(1)
        plu_path = plu_name[1:]
        function_name = "route"
        for i in plu_path:
            print(i)
            function_name = function_name + "_" + i
            print(function_name)
        data = plu.run_one_funcion(plugin, str(plu_name[0]), function_name, request)
        return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
