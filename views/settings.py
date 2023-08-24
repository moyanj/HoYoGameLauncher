from flask import Blueprint, render_template, request
from env import *

app = Blueprint("settings", __name__, url_prefix="/setting")

@app.route("/html")
def setting_html():
    lang = conf.get_language()
    try:
        data = json.load(open("data\language\{}.json".format(lang), encoding="utf-8"))
    except:
        data = json.load(open("data\language\zh-cn.json", encoding="utf-8"))
    return render_template("setting.html", lang=data)


@app.route("/", methods=["POST"])
def setting():
    pass