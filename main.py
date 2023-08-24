import webview
import click
from server import app as flask
import ctypes, sys

def is_admin():
    try:
            
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        print("not admin")
        return False

# 创建WebView窗口
@click.command()
@click.option("-d", "--debug", type=str, default="no", help="是否开启调试模式（yes/no）")
def main(debug):
    if is_admin():
        # 将要运行的代码加到这里
        if debug == "yes":
            webview.create_window(
                "HoYoGameLauncher",
                url="http://127.0.0.1:6553",
                text_select=True,
                width=1280,
                height=720,
            )
            webview.start(debug=True, user_agent="HoYoGameLauncher-WebView/1.0.0")
        else:
            webview.create_window(
                "HoYoGameLauncher", url=flask, text_select=True, width=1280, height=720
            )
            webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0")
    else:
        print("get admining...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        
    


if __name__ == "__main__":
    main()
