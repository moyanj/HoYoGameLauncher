<h1 align="center">
  <img src="https://cdn.jsdelivr.net/gh/moyanj/HoYoGameLauncher@1.0.1/images/icon.png" width="64px" height="64px">
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
  此存储库包含了<strong>HoYoGameLauncher</strong>的源代码。<strong>HoYoGameLauncher</strong>是一个<a href="https://www.mihoyo.com">米哈游</a>游戏启动器，旨在简化玩家启动游戏的步骤。它功能强大，维护积极，易于使用。
</p>

<p align="center">
<a href="#介绍">介绍</a> &nbsp;&bull;&nbsp;
<a href="#安装">安装</a> &nbsp;&bull;&nbsp;
 <a href="/dev">开发文档</a>
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
下载[最新开发版本](https://github.com/moyanj/HoYoGameLauncher/actions/workflows/release.yml)(可能无法正常运行)<br/>

- 如果你下载了exe安装包, 请直接运行，然后根据提示安装。<br/>
- 如果你下载了zip程序压缩包, 请解压后双击打开`HoYoGameLauncher.exe`即可运行。（注意：您可能需要安Microsoft Edge WebView2）<br/>
- 如果你下载了源代码, 请前往[开发文档](/dev)查看如何运行。<br/>
# 特别感谢
* [OpenAI](https://openai.com/)
* [Microsoft](https://www.microsoft.com/)
* [GitHub](https://github.com/)
* [清华大学](https://github.com/THUDM)
* [UIGF organization](https://uigf.org)
* [EnkaAPI](https://enka.network/)

# 特定的原神项目 
- [Snap.Hutao](https://hut.ao)
- [Genshin.Launcher.Plus](https://github.com/DawnFz/Genshin.Launcher.Plus)
- [Starward](https://github.com/Scighost/Starward)
# 使用的技术栈
## 后端
- [Flask](https://github.com/pallets/flask)（服务器框架）
- [pywebview](https://github.com/r0x0r/pywebview)（显示页面）
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)（打包EXE）
- [requests](https://github.com/psf/requests)（请求API）
## 前端
- [bootstrap](https://github.com/twbs/bootstrap)（前端CSS框架）
- [jQuery](https://github.com/jquery/jquery)（前端JS框架）
- [Vue](https://vuejs.org/)（前端JS框架）
- [Elment Plus](https://element-plus.org/)（前端UI框架）