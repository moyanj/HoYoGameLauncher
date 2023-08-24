import webview
import click
from server import app as flask
from loguru import logger as log
import faulthandler as f

f.dump_traceback(open("./1.txt", "w"), True)
log.add(
    "log/main.log",
    rotation="1 days",
    retention="7 days",
    level="DEBUG",
    compression="zip",
)


# 创建WebView窗口
@click.command()
@click.option("-d", "--debug", type=str, default="no", help="是否开启调试模式（yes/no）")
def main(debug):
    if debug == "yes":
        log.debug("开启调试模式")
        webview.create_window(
            "HoYoGameLauncher",
            url="http://127.0.0.1:6553",
            text_select=True,
            width=1280,
            height=720,
        )
        webview.start(debug=True, user_agent="HoYoGameLauncher-WebView/1.0.0")
    else:
        log.debug("未使用调试模式")
        webview.create_window(
            "HoYoGameLauncher", url=flask, text_select=True, width=1280, height=720
        )
        webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0")


if __name__ == "__main__":
    main()
