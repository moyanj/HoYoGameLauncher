import webview
import click
from server import app as flask

engine_dict = {
    "Edge":"edgechromium",
    "IE":"mshtml",
    "GTK":"gtk"
}
# 创建WebView窗口
@click.command()
@click.option("--debug", is_flag=True,help="是否开启调试模式")
@click.option("--width", default=1280, help="宽度")
@click.option("--height", default=720, help="高度")
@click.option("--minimized", is_flag=True, help="最小化")
@click.option("--engine", default="Edge", help="webview引擎")
@click.option("--server", is_flag=False, help="是否单独启动服务端")
@click.option("--port", default=6553, help="服务端端口")
@click.option("--fullscreen", is_flag=False, help="是否全屏")
def main(debug, width,height,minimized,engine,server,port,fullscreen):
    if engine not in ["Edge", "IE", "GTK"]:
        print("请输入正确的引擎")
        exit()
    # 将要运行的代码加到这里
    if server:
        flask.run(host="0.0.0.0", port=port, debug=True)
    if debug:
        webview.create_window(
            "HoYoGameLauncher",
            url="http://127.0.0.1:6553",
            text_select=True,
            width=width,
            height=height,
            minimized = minimized,
            fullscreen = fullscreen
        )
        webview.start(debug=True, user_agent="HoYoGameLauncher-WebView/1.0.0",gui=engine_dict[engine])
    else:
        print("默认模式")
        webview.create_window(
            "HoYoGameLauncher",
            url=flask,
            text_select=True,
            width=width,
            height=height,
            minimized = minimized,
            fullscreen = fullscreen
        )
        webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0",gui=engine_dict[engine])


if __name__ == "__main__":
    main()
