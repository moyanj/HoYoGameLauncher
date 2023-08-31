# 开发

# 打包
运行以下命令，即可在pack文件夹中找到打包好的可执行文件。

```shell
python build.py pack
```
# 从源代码运行

## 配置环境

```shell
pip install pipenv
python -m pipenv shell
```

# 运行

请先进入 pipenv 虚拟环境，再运行以下命令：
```shell
python main.py
```
main.py的具体参数说明见[#Main.py](#Main.py)
```shell
python server.py
```

# 参数

- `-d`或`--debug` : 启动开发模式（不启动服务端），默认不加。
- `--width <width>` : 窗口宽度，默认1280。
- `--height <height>` : 窗口高度，默认720。
- `--minimized` : 启动时最小化，默认不加。
- `--engine` : 启动时使用的HTML渲染引擎。支持：`edgechromium`（Microsoft Edge WebView2）、`gtk`、`mshtml`(不建议)，默认`edgechromium`。
- `--server` : 启动服务端在6553端口上，默认不加。


# 插件开发

## 可以调用的库
此为在import后的名字

- sys
- builtins
- marshal
- nt
- winreg
- time
- zipimport
- codecs
- encodings
- abc
- io
- stat
- genericpath
- ntpath
- os
- site
- math
- operator
- datetime
- types
- enum
- itertools
- keyword
- reprlib
- collections
- functools
- copyreg
- re
- token
- tokenize
- linecache
- traceback
- warnings
- weakref
- string
- threading
- atexit
- logging
- posixpath
- fnmatch
- errno
- zlib
- bz2
- lzma
- shutil
- bisect
- random
- tempfile
- contextlib
- typing
- uuid
- json
- select
- selectors
- socket
- struct
- binascii
- base64
- ssl
- socketserver
- wsgiref
- http
- copy
- email
- urllib
- locale
- calendar
- quopri
- html
- uu
- mimetypes
- signal
- msvcrt
- subprocess
- platform
- cgi
- hashlib
- hmac
- unicodedata
- pickle
- configparser
- ast
- opcode
- dis
- importlib
- inspect
- bottle
- webview
- gettext
- ctypes
- click
- contextvars
- markupsafe
- nturl2path
- colorama
- dataclasses
- pkgutil
- secrets
- werkzeug
- numbers
- decimal
- heapq
- difflib
- pprint
- concurrent
- asyncio
- blinker
- pathlib
- jinja2
- itsdangerous
- flask
- Crypto
- cffi
- pycparser
- lib
- queue
- ipaddress
- urllib3
- idna
- zipfile
- certifi
- stringprep
- requests
- api
- multiprocessing
- sysconfig
- glob
- loguru
- plugins
- env
- views
- server
- main

## 不可使用的函数名
- route_files

## 文件结构

```
plugins/<插件名>/─┐
                  ├── __init__.py
                  ├─┐static
                  │ ├── css
                  │ ├── images
                  │ └── js
                  └─┬ templates
                    └── index.html
```

### `__init__.py`

主文件，必须包含有，其需要继承`lib.plugin.Plugin`这个类。
<br>
其只能调用[该表](#可以调用的库)内的函数，当然，您也可以将库放在`plugins/<插件名>`内，您就可以调用了。（需在import 时加点，如：有一个名为`c`的库,你可以这样导入：`import .c`）
route函数命名规则：
1. 必须以route开头
2. 其以`_`代替url里的`/`
3. 不得使用[此表](#可以调用的库)内的函数名
如route_test_1,就可以在`<插件名>/test/1/`处访问到其返回值


```python
from lib.plugin import Plugin
class Plugin(Plugin):
    __name__ = "插件名"
    __version__ = "插件版本"
    __description__ = "插件描述"
    __author__ = "插件作者"
    def __init__(self):
        super().__init__()
    def route_<路径>(self, request):
        return "<返回值>"
    def before_reques(self, request):
        # 用于验证请求，True为通过，False为不通过。
        return True
```

### `static`

静态文件夹，其下的文件可以在`/<插件名>/files/<文件路径>`访问得到。（文件路径相对于`plugins/<插件名>/static`）

### `templates`

模板文件夹，其下的文件会被加载进主页面中，其命名规则[见此](#模板命名规则)

## 模板命名规则

- header.html
    <br>
    其会被加载进header中（`head`）。
- sidebar.html
    <br>
    其会被加载进主页面的sidebar中（`.nav`）。
- content.html
    <br>
    其会被加载进主页面的内容区域中（`.container-fluid`）。
- modal.html
    <br>
    其会被加载进模态框中。
- settings.html
    <br>
    其会被加载进设置页面的内容区域中（`.container`）。








