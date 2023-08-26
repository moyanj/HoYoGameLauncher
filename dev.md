# 开发
## 打包
运行以下命令，即可在pack文件夹中找到打包好的可执行文件。

```shell
python build.py pack
```
## 从源代码运行
### 配置环境

```shell
pip install pipenv
python -m pipenv shell
```

## 运行
请先进入 pipenv 虚拟环境，再运行以下命令：
```shell
python main.py -d yes
```
main.py的具体参数说明见[#Main.py](#Main.py)
```shell
python server.py
```

该条命令如果你在运行main.py时使用了-d yes参数，则无需手动运行server.py。
## 配置项
```json
{
    "conf_init": "fasle", // 是否已经配置过
    "player": {
        "uid": "unknown",// 玩家UID（原神）
        "username": "unknown",// 玩家昵称（原神）
        "init": "false" // 是否初始化个人信息
    },
    "settings": {
        "debug": "false", // 是否使用Debug模式
        "language": "zh-cn", // 语言
        "theme": "default"// 主题（将在v99.99.99上线）
    },
    "server": {
        "port": "6553", //端口（没啥用）
        "Allowed UA": [ // 允许的UA
            "HoYoGameLauncher-WebView/1.0.0",
            "HoYoGameLauncher-Server/1.0.0"
        ],
        "Allowed IP": [ // 允许的IP
            "127.0.0.1"
        ]
    },
    "game": {
        "ys": {
            "path": "C:\\Program Files\\Genshin Impact\\Game\\YuanShen.exe"// 原神路径
        },
        "sr": {
            "path": "C:\\Program Files\\Genshin Impact\\Game\\YuanShen.exe"// 崩铁路径
        }
    }
}
```
# 代码解析
## Main.py
### main
该函数用于主程序的运行，包括初始化，主循环，以及退出程序。

#### 函数功能
- 初始化
<br>
其采用了<code>pywebview</code>库，用于创建一个浏览器窗口。然后，其去获取Flask后端([代码解析](#Server.py))渲染的HTML文件，并将其显示在浏览器窗口中。由于网页大量使用HTML5,CSS3,JavaScript ES6因此，其用户计算机上必须要安装有<code>Edge Runtime</code>才能达到最好的渲染效果。
- 主循环
  <br>
  略
- 退出程序
  <br>
  略
#### 调用方式

不建议导入其他文件内使用。
```python
from main import main
main()
```
### 其他
本文件有命令行选项：
```
-d, --debug TEXT  是否开启调试模式（yes/no）
```
如：
```
python main.py -d yes
```
即会开启调试模式，但是您也必须手动在6553端口上开发服务器。
## Server.py
这个几乎是整个项目的Core，其负责渲染HTML文件，操作本地计算机等等重要功能。
### 原理
其会创建一个Flask服务器，如果你直接运行文件的话（<code>python server.py</code>）他将会在6553端口上以Debug模式运行。
### 函数功能
#### before_request
该函数将在每次请求之前运行，其用于验证请求的来源，以防止恶意CSRF攻击。
- 原理
<br>
  其将读取Config.json里的 <code>Allowed UA</code> 字段，并将其与请求头里的<code>User-Agent</code>字段进行比较，然后也还会对IP进行验证。如果没有问题，则正常返回，如果有问题，则返回403错误。
- 调用方式
<br>
  不建议导入其他文件内使用。
```python
from server import before_request
before_request()
```

#### app.route(*)系
略

## tools/init.py
其用于初始化设置。
### 原理
其用于初始化设置，其会修改Config.json文件。
### 函数功能
#### get_Reg_key
其用于读取注册表，并返回其值。以获取原神或者崩铁官方启动器安装路径
- 原理
<br>
  其会调用<code>winreg</code>模块，并使用<code>winreg.OpenKey</code>打开注册表，然后使用<code>winreg.QueryValueEx</code>获取其值。

- 调用方式
```python
from tools.init import get_Reg_key
get_Reg_key(
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\崩坏：星穹铁道",
            "InstallPath",
        )
```

# 插件卡法

