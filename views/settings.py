from flask import Blueprint, render_template, request
from env import *

app = Blueprint("settings", __name__, url_prefix="/setting")


@app.route("/html")
def setting_html():
    return render_template("setting.html", lang={})


@app.route("/", methods=["POST"])
def setting():
    pass
