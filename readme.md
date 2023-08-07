<h1 align="center">
  <img src="images\icon.png" width="64px" height="64px">
  <br>
  <a href="https://github.com/moyanj/HoYoGameLauncher">
    HoYoGameLauncher
  </a>
</h1>
<p align="center">
    <a target="_blank" href="https://github.com/moyanj"><img src="https://img.shields.io/badge/github-moyanj-brightgreen.svg"/></a>&nbsp;
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/Code%20Style-black-000000.svg"/></a>
    <a target="_blank" ><img src="https://img.shields.io/badge/License-BSD-brightgreen.svg" /></a>&nbsp;
    <a target="_blank" ><img src="https://img.shields.io/github/languages/top/moyanj/HoYoGameLauncher.svg" /></a>&nbsp;
    <a target="_blank" ><img src="https://img.shields.io/github/commit-activity/t/moyanj/HoYoGameLauncher" /></a>&nbsp;
</p>
<p align="center">
  此存储库包含<strong>HoYoGameLauncher</strong>的源代码。<strong>HoYoGameLauncher</strong>是一个<a href="https://www.mihoyo.com">米哈游</a>游戏启动器，旨在简化玩家启动游戏的步骤。它功能强大，维护积极，易于使用。
</p>

<p align="center">
<a href="#介绍">介绍</a> &nbsp;&bull;&nbsp;
<a href="#安装">安装</a> &nbsp;<!--&bull;&nbsp;
 <a href="https://github.com/moyanj/HoYoGameLauncher/dev.md">开发文档</a> -->
</p>

# 介绍
HoYoGameLauncher提供了一个米哈游聚合启动器，可以快捷的启动：
- 崩坏：星穹铁道
- 原神
- 原神国际服（暂未实现）
- 崩坏：星穹铁道国际服（暂未实现）
- 崩坏3（暂未实现）


# 安装
下载[最新releases版本](https://github.com/moyanj/HoYoGameLauncher/releases/latest)<br/>
下载[最新开发版本](https://github.com/moyanj/HoYoGameLauncher/actions/workflows/package.yml)(可能无法正常运行)<br/>

- 如果你下载了exe安装包, 请直接运行，然后根据提示安装。<br/>
- 如果你下载了zip程序压缩包, 请解压后双击打开`HoYoGameLauncher.exe`即可运行。<br/>
- 如果你下载了源代码, 请使用以下方法打包：<br/>
## 打包
### 打包环境
- Python3.10+
- Windows 10 21H1 +（不支持Linux）
- Flask == 2.3.2
- Flask-Cors == 4.0.0
- pyinstaller == 5.13.0
- pywebview == 4.2.2
（可通过`requirements.txt`安装）
### 打包步骤
运行以下命令，即可在build文件夹中找到打包好的可执行文件。

```shell
python build.py
```
## 从源代码运行
### 配置环境

```shell
pip install -r requirements.txt
```

### 运行服务端

```shell
cd server
python app.py
```

### 运行客户端

```
python main.py
```

之后就会弹出启动器窗口
## 使用的开源项目
- [Flask](https://github.com/pallets/flask)（为服务器提供框架）
- [Flask-Cors](https://github.com/corydolphin/flask-cors)（实现跨域请求）
- [pywebview](https://github.com/r0x0r/pywebview)（显示页面）
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)（打包EXE）
- [jsmin](https://github.com/tikitu/jsmin)（压缩JS）
- [cssmin](https://github.com/mir-rs/cssmin)（压缩CSS）
- [requests](https://github.com/psf/requests)（请求API）
- [bootstrap](https://github.com/twbs/bootstrap)（前端CSS）
- [Vue.js](https://github.com/vuejs/vue)（前端框架(正在写)）



## 致谢
- 由 [Microsoft](https://www.microsoft.com/) 的 [NewBing](https://www.bing.com/new) 为我们提供了图标。
- 由 [Microsoft](https://code.visualstudio.com/) 提供 IDE 支持。
- 由 [清华大学](https://github.com/THUDM) 提供CodeGeeX代码辅助编写。
- 由 [EnkaAPI](https://enka.network/) 提供原神数据查询支持。
