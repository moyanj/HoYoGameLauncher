import webview
import subprocess
from threading import Thread
import jinja2 as j
import sys
from server.app import app as flask
Static_URL = "http://127.0.0.1:6553/files"
class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def exit(self):
        subprocess.run("taskkill /f /im 'server.exe'", shell=True)
        self._window.destroy()


if sys.argv[1] != "debug":
    # 运行服务器
    def server():
        subprocess.run("server.exe'", shell=True)


    # 启动服务器线程
    t1 = Thread(target=server)
    t1.start()

# 渲染HTML
env = j.Environment(loader=j.FileSystemLoader("html"))
template = env.get_template("index.html")
html = template.render(static_url = Static_URL) 
api = Api()

# 创建WebView窗口
window = webview.create_window("HoYoGameLauncher", url=flask,text_select=True,width=1280,height=720)
api.set_window(window)
if sys.argv[1] == "debug":
    webview.start(debug=True,user_agent="HoYoGameLauncher-WebView/1.0.0")
else:
    webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0")
 
