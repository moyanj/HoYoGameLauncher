import webview
import subprocess
from threading import Thread


def server():
    cmd = "server.exe > log.txt"
    subprocess.run(cmd, shell=True)


t1 = Thread(target=server)
t1.start()

with open("html/index.html", "r", encoding="utf-8") as f:
    html = f.read()
try:
    webview.create_window("HoYoGameLauncher", html=html)
    webview.start()
except:
    subprocess.run("taskkill /f /im 'server.exe'", shell=True)
