import webview
import subprocess
from threading import Thread

# 运行服务器


def server():
    cmd = "server.exe > log.txt"
    subprocess.run(cmd, shell=True)


# 启动服务器线程
t1 = Thread(target=server)
t1.start()
# 读取HTML
with open("html/index.html", "r", encoding="utf-8") as f:
    html = f.read()
try:
    # 创建WebView窗口
    webview.create_window("HoYoGameLauncher", html=html)
    webview.start()
except:
    # 杀死服务器进程
    subprocess.run("taskkill /f /im 'server.exe'", shell=True)
