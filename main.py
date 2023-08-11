import webview
import click
from server import app as flask
# 创建WebView窗口
@click.command()
@click.option("-d", "--debug",type=str,default="no",help="是否开启调试模式（yes/no）")
def main(debug):
    if debug == "yes":
        webview.create_window("HoYoGameLauncher", url="http://127.0.0.1:6553",text_select=True,width=1280,height=720)
        webview.start(debug=True,user_agent="HoYoGameLauncher-WebView/1.0.0")
    else:
        webview.create_window("HoYoGameLauncher", url=flask,text_select=True,width=1280,height=720)
        webview.start(user_agent="HoYoGameLauncher-WebView/1.0.0")

if __name__ == "__main__":
    main()
 
