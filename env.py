from loguru import logger as log
import os
import json
import sys
import lib.plugin as plu
from lib.config import Config  # 配置
from api.env import *

log.add(
    "log/flask.log",
    level="DEBUG",
)
avatarID = json.load(open("data/avatar.json", "r", encoding="utf-8"))  # 角色头像表
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # 程序文件路径
plugin = plu.load_plugins("plugins")
# 创建配置对象
conf = Config("config.json")
