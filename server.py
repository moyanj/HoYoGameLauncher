from flask import (
    Flask,
    request,
    send_from_directory,
    render_template,
    redirect,
)  # Flask
import os  # 系统操作
import requests
import lib.init as inits  # 函数
import json  # json解析
import api  # 所有API
from env import *  # 所有全局变量
from views import data, settings, init  # 视图函数
import traceback  # 错误追踪
from lib import debug as dbg  # DBG

# 初始化Flask
app = Flask(__name__, template_folder=save_path + "/html/")


# 404错误
@app.errorhandler(404)
def error_404(e):
    return Rest("页面不存在", 404)


# 顶级错误处理器
@app.errorhandler(Exception)
def error_500(e):
    stack_trace = traceback.format_exc()
    dbg.crash(stack_trace)
    return Rest(f"未知错误，错误日志位于{save_path}\\debug.txt", 500)


# 注册蓝图
app.register_blueprint(data.app)
app.register_blueprint(settings.app)
app.register_blueprint(init.app)


# 初始化程序
inits.main()
# 加载玩家列表
PlayerList = []
for filename in os.listdir("data/player"):
    play = Player("111111")
    name = "data/player/" + filename
    PlayerList.append(play.load(name=name))


# 输出日志
@app.after_request
def after_request(response):
    # 获取状态码
    status_code = response.status_code
    # log
    log.info(f"{request.method} {request.path} {status_code}")
    return response


@app.route("/")
def index():
    # 返回主页
    return render_template("index.html")


@app.route("/run/<game>")
def game(game):
    """
    运行游戏
    """
    # 查询游戏路径
    gamepath = conf.getGamePath(game)
    # 提取信息
    file = os.path.basename(gamepath)
    path = os.path.dirname(gamepath)
    panfu = gamepath.split(":")[0] + ":"
    # 运行
    os.system("{} && cd {} && {}".format(panfu, path, file))
    return Rest("成功")


@app.route("/post/gamepath")
def postgamepath():
    """
    修改游戏路径
    """
    gamepath = request.args.get("gamepath")
    game = request.args.get("game")
    conf.setGamePath(gamepath, game)
    return Rest("成功")


@app.route("/files/<path:filename>")
def getfile(filename):
    """
    静态文件
    """
    return send_from_directory(save_path + "/html/static/", filename), 200


@app.route("/settings/<key>/<val>")
def settin(key, val):
    if key == "language":
        conf.setLang(val)
    return Rest("成功")


@app.route("/bg/ys")
def bg_ys():
    return api.get_ysbg()


@app.route("/bg/sr")
def bg_srr():
    return api.get_srbg()


@app.route("/web/wiki/ys")
def wiki_ys():
    req = requests.get(
        "https://bbs.mihoyo.com/ys/obc/?&bbs_presentation_style=no_header&mihoyo_app=true5"
    )
    return redirect(
        "https://bbs.mihoyo.com/ys/obc/?&bbs_presentation_style=no_header&mihoyo_app=true5"
    )


@app.route("/i18n/get")
def i18n_get():
    return Rest(data=i18n.t(request.args.get("key")))
    # return i18n.t(request.args.get("key"))


@app.route("/<path:url>")
def pluurl(url):
    url = str(url)
    plu_name = url.split("/")
    plu_len = len(plu_name)
    if plu_len == 1:
        data = plu.run_one_funcion(plugin, str(plu_name[0]), "route_main", request)
        return data
    elif plu_name[1] == "files":
        data = plu.run_one_funcion(plugin, str(plu_name[0]), "route_files", request)
        return data
    else:
        plu_path = plu_name[1:]
        function_name = "route"
        for i in plu_path:
            function_name = function_name + "_" + i
        data = plu.run_one_funcion(plugin, str(plu_name[0]), function_name, request)
        return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
