from flask import Flask, request, send_file  # flask
import sqlite3 as sql  # 数据库
import os  # 系统操作
from flask_cors import CORS  # 跨域
import init  # 函数
import requests as r
import json

version = int("0")

# 初始化Flask
app = Flask(__name__)
# 初始化CORS
CORS(app, supports_credentials=True)
# 创建数据库
init.main()
# 连接数据库
conn = sql.connect("data.db", check_same_thread=False)
cur = conn.cursor()


def updatetype(types):
    if types == "STATIC":
        return "界面更新"
    elif types == "SERVER":
        return "服务端更新"
    elif types == "MAIN":
        return "主程序更新"
    elif types == "APP":
        return "大型更新"
    else:
        return "unknown"

# 验证请求


@app.before_request
def before_request():
    # UA = request.headers.get("verifykey")
    ip = request.remote_addr
    if ip != "127.0.0.1":
        return "This is not a request from HoYoGameLauncher", 403


# 运行游戏


@app.route("/run/<game>")
def game(game):
    # 查询游戏路径
    data = cur.execute("SELECT * FROM game WHERE name = '{}';".format(game))
    data = data.fetchall()
    gamepath = data[0][1]
    # 提取信息
    file = os.path.basename(gamepath)
    path = os.path.dirname(gamepath)
    panfu = gamepath.split(":")[0] + ":"
    # 运行
    # os.system("{} && cd {} && dir && {}".format(panfu, path, file))
    return "RUN OK", 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/post/gamepath")
def postgamepath():
    """
    修改游戏路径
    """
    gamepath = request.args.get("gamepath")
    game = request.args.get("game")
    cur.execute(
        "UPDATE game SET path = '{}' WHERE name = '{}';".format(gamepath, game))
    conn.commit()
    return "OK", 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/get/gamepath/<game>")
def getonegamepath(game):
    """
    获取一个游戏的路径
    """
    data = cur.execute("SELECT * FROM game WHERE name = '{}';".format(game))
    data = data.fetchall()
    i = data[0][1]
    return i, 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/get/gamepath")
def getgamepath():
    """
    获取所有游戏的路径
    """
    data = cur.execute("SELECT * FROM game;")
    data = data.fetchall()
    data = {
        "ys": data[0][1],
        "sr": data[1][1],
    }
    return data, 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/files/<path:filename>")
def getfile(filename):
    """
    静态文件
    """
    return send_file("file\\" + filename), 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/testupdate")
def update():
    url = "https://ghproxy.com/https://raw.githubusercontent.com/moyanj/HoYoGameLauncher/update/update.json"
    req = r.get(url)
    data = json.loads(str(req.text))
    text = {
        "version": data["version"],
        "description": data["description"],
        "type":  updatetype(data["type"])
    }
    if data["ver"] > version:
        return text, 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return "no", 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/update")
def update2():
    tmpdir = os.getenv("TMP")
    url = "https://ghproxy.com/https://raw.githubusercontent.com/moyanj/HoYoGameLauncher/update/update.json"
    req = r.get(url)
    data = req.text()
    data = json.loads(data)
    fileurl = data["url"]
    req = r.get(fileurl)
    with open(tmpdir+"\\update.zip", "wb") as f:
        f.write(req.content)
    os.system("update.exe")
    return "ok", 200, {"Access-Control-Allow-Origin": "*"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6553, debug=True)
