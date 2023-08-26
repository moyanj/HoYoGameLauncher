import webview
import click
from server import app as flask


# 创建WebView窗口
@click.command()
@click.option("-d","--debug", is_flag=True)
@click.option("--width", default=1280, help="宽度")
@click.option("--height", default=720, help="宽度")
@click.option("--minimized", is_flag=True, help="最小化")
@click.option("--engine", default="edgechromium", help="webview引擎")
@click.option("--server", is_flag=False, help="端口")
def main(debug, width,height,minimized,engine,server):
    if engine not in ["edgechromium", "mshtml", "gtk"]:
        print("请输入正确的引擎")
        exit()
    # 将要运行的代码加到这里
    if server:
        flask.run(host="0.0.0.0", port=6553, debug=True)
    if debug:
        webview.create_window(
            "HoYoGameLauncher",
            url="http://127.0.0.1:6553",
            text_select=True,
            width=width,
            height=height,
            minimized = minimized
        )
        webview.start(debug=True, user_agent="HoYoGameLauncher-WebView/1.0.0",gui=engine)
    else:
        print("默认模式")
        webview.create_window(
            "HoYoGameLauncher",
            url="http://127.0.0.1:6553",
            text_select=True,
            width=width,
            height=height,
            minimized = minimized
        )
        webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0",gui=engine)


if __name__ == "__main__":
    main()
