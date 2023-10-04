import webview
import click
from server import app as flask
from env import *
import platform
from tkinter import messagebox
import winreg
import requests


def get_Reg_key(path, key_):
    reg_root = winreg.HKEY_CURRENT_USER
    reg_path = path
    reg_flags = winreg.KEY_READ
    key = winreg.OpenKey(reg_root, reg_path, 0, reg_flags)

    value, key_type = winreg.QueryValueEx(key, key_)
    winreg.CloseKey(key)
    return value


try:
    EdgeVersion = get_Reg_key("Software\\Microsoft\\EdgeWebView\\BLBeacon", "version")
except:
    EdgeVersion = "0"
    messagebox.showwarning("警告", "未安装Microsoft Edge WebView2")
    # 是否安装Microsoft Edge WebView2
    if messagebox.askyesno("提示", "是否安装Microsoft Edge WebView2?"):
        req = requests.get(DownloadURL["WebView"])
        WebViewDownloadPath = os.path.join(
            AppDataPath, "DownloadFiles", "MicrosoftEdgeWebView2.exe"
        )
        with open(WebViewDownloadPath, "wb") as f:
            f.write(req.content)
        os.system(WebViewDownloadPath)

        restart()


# 渲染引擎字典
engine_dict = {"Edge": "edgechromium", "IE": "mshtml", "GTK": "gtk"}


def run_server(port, debug):
    """启动服务器

    Arguments:
        port -- 端口
        debug --  是否为调试
    """
    flask.run(host="0.0.0.0", port=port, debug=debug, processes=True)


# 创建WebView窗口
@click.command()
@click.option("--debug", is_flag=True, help="是否开启调试模式")
@click.option("--width", default=1280, help="宽度")
@click.option("--height", default=720, help="高度")
@click.option("--minimized", is_flag=True, help="最小化")
@click.option("--engine", default="Edge", help="webview引擎")
@click.option("--server", is_flag=True, help="是否单独启动服务端")
@click.option("--port", default=6553, help="服务端端口")
@click.option("--fullscreen", is_flag=True, help="是否全屏")
@click.option("--private", is_flag=True, help="是否为隐私模式。")
def main(debug, width, height, minimized, engine, server, port, fullscreen, private):
    """主函数

    Arguments:
        略
    """
    # 判断是否为正确的渲染引擎
    if engine not in engine_dict.keys():
        messagebox.showerror("错误", "请输入正确的引擎！")
        exit()
    # 防止拿 Wine 跑原神
    if platform.system() != "Windows":
        messagebox.showerror("错误", "请使用Windows系统运行HoYoGameLauncher")
        exit()
    # 判断是否启动服务器
    if server:
        run_server(port, debug)
    # 以Debug模式启动
    if debug:
        webview.create_window(
            "HoYoGameLauncher",
            url="http://127.0.0.1:6553",
            text_select=True,
            width=width,
            height=height,
            minimized=minimized,
            fullscreen=fullscreen,
        )
        webview.start(
            debug=True,
            user_agent="HoYoGameLauncher-WebView/1.0.0",
            gui=engine_dict[engine],
            private_mode=private,
            storage_path=os.path.join(AppDataPath, "Web"),
        )
    # 以普通模式启动
    else:
        print("默认模式")
        # 创建窗口
        webview.create_window(
            "HoYoGameLauncher",
            url=flask,
            text_select=True,
            width=width,
            height=height,
            minimized=minimized,
            fullscreen=fullscreen,
        )
        # 显示窗口
        webview.start(
            user_agent="HoYoGameLauncher-WebView/1.0.0",
            gui=engine_dict[engine],
            private_mode=private,
            storage_path=os.path.join(AppDataPath, "Web"),
        )



if __name__ == "__main__":
    main()
