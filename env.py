from loguru import logger as log
import os
import json
import sys
import lib.plugin as plu
from lib.config import Config  # 配置
from api.env import *
import logging

# 关闭Flask原生日志
logs = logging.getLogger ('werkzeug') 
logs.disabled = True

# 删除loguru默认日志记录器
log.remove(0)
# 添加文件记录器
log.add(
    "log/flask.log",
    level="DEBUG",
    format=format("{time:YYYY-MM-DD HH:mm:ss}[ {level} ]- {message}"),
    enqueue=True
)
# 添加调试记录器
log.add(
    sys.stdout,
    level="DEBUG",
    format=format("<green>{time:YYYY-MM-DD HH:mm:ss} </green>[ {level} ]- <level>{message}</level>"),
    colorize=True,
    enqueue=True,
    diagnose=True
)
# 角色头像表
avatarID = json.load(open("data/avatar.json", "r", encoding="utf-8"))  
# 程序文件路径
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))  
# 插件列表
plugin = plu.load_plugins("plugins") 

print = log.debug
# 创建配置对象
conf = Config("config.json")
