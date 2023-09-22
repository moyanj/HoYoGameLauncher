from loguru import logger as log
import os
import json
import sys
import lib.plugin as plu
import lib.config as conf
import base64 as b64
import logging
from lib import debug as dbg
import re
import pickle as p
from lib import i18ns as i18n
from lib.retur import Rest

with open("data/version.txt",encoding="utf-8") as f:
    HOYOGAMELAUNCHER_VERSION = f.read()
print(HOYOGAMELAUNCHER_VERSION)
# 关闭Flask原生日志
logs = logging.getLogger("werkzeug")
logs.disabled = True

# 删除loguru默认日志记录器
log.remove(0)
# 添加文件记录器
log.add(
    "log/flask.log",
    level="DEBUG",
    format=format("{time:YYYY-MM-DD HH:mm:ss}[ {level} ]- {message}"),
    enqueue=True,
)
# 添加调试记录器
log.add(
    sys.stdout,
    level="DEBUG",
    format=format(
        "<green>{time:YYYY-MM-DD HH:mm:ss} </green>[ {level} ]- <level>{message}</level>"
    ),
    colorize=True,
    enqueue=True,
    diagnose=True,
)
# 角色头像表
avatarID = json.load(open("data/avatar.json", "r", encoding="utf-8"))
# 程序文件路径
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))
# 插件列表
plugin = plu.load_plugins("plugins")

print = log.debug

# Copyright (c) DGP Studio. All rights reserved.
ApiGeetest = "https://api.geetest.com"
ApiV6Geetest = "https://apiv6.geetest.com"
ApiTakumi = "https://api-takumi.mihoyo.com"
ApiTakumiAuthApi = f"{ApiTakumi}/auth/api"
ApiTaKumiBindingApi = f"{ApiTakumi}/binding/api"
ApiTakumiRecord = "https://api-takumi-record.mihoyo.com"
ApiTakumiCardApi = f"{ApiTakumiRecord}/game_record/app/card/api"
ApiTakumiCardWApi = f"{ApiTakumiRecord}/game_record/app/card/wapi"
ApiTakumiEvent = f"{ApiTakumi}/event"
ApiTakumiEventCalculate = f"{ApiTakumiEvent}/e20200928calculate"
ApiTakumiRecordApi = f"{ApiTakumiRecord}/game_record/app/genshin/api"
ApiTakumiRecordAapi = f"{ApiTakumiRecord}/game_record/app/genshin/aapi"
AppMihoyoReferer = "https://app.mihoyo.com"
AppAuthApi = f"{AppMihoyoReferer}/account/auth/api"
BbsApi = "https://bbs-api.mihoyo.com"
BbsApiUserApi = f"{BbsApi}/user/wapi"
Hk4eApi = "https://hk4e-api.mihoyo.com"
Hk4eApiAnnouncementApi = f"{Hk4eApi}/common/hk4e_cn/announcement/api"
Hk4eApiGachaInfoApi = f"{Hk4eApi}/event/gacha_info/api"
PassportApi = "https://passport-api.mihoyo.com"
PassportApiAuthApi = f"{PassportApi}/account/auth/api"
PassportApiV4 = "https://passport-api-v4.mihoyo.com"
SdkStatic = "https://sdk-static.mihoyo.com"
SdkStaticLauncherApi = f"{SdkStatic}/hk4e_cn/mdk/launcher/api"
WebStaticMihoyoReferer = "https://webstatic.mihoyo.com"
AnnouncementQuery = "game=hk4e&game_biz=hk4e_cn&lang=zh-cn&bundle_id=hk4e_cn&platform=pc&region=cn_gf01&level=55&uid=100000000"


class Player:
    """
    Player 类
    """

    def __init__(
        self,
        str_uid,
        ck: str = "",
        stoken: str = "",
        id: str = "",
        name: str = "",
        ltoken: str = "",
    ):
        uid = int(str_uid)
        prefix = int(str_uid[0])
        if 1 <= prefix and prefix <= 4:
            result = "cn_gf01"  # 国服
        elif 5 == prefix:
            result = "cn_qd01"  # 渠道
        elif 6 == prefix:
            result = "os_usa"  # 各服
        elif 7 == prefix:
            result = "os_euro"  # 各服
        elif 8 == prefix:
            result = "os_asia"  # 各服
        elif 9 == prefix:
            result = "os_cht"  # 各服
        else:
            result = "unknown"  # 未知
        self.uid = uid
        self.ok = re.match(r"^[^34]\d{8}$", str_uid) != None
        self.region = result
        self.str_uid = str_uid
        self.os = result != "cn_gf01" or result != "cn_qd01"
        self.cookie = ck
        self.stoken = stoken
        self.ltoken = ltoken
        self.id = id
        self.name = name
        # self.server = 1

    def __str__(self):
        return str(self.uid)

    def dump(self, name):
        data = {
            "uid": self.uid,
            "region": self.region,
            "ok": self.ok,
            "os": self.os,
            "ck": b64.b64encode(self.cookie.encode("utf-16le")),
            "stoken": b64.b64encode(self.stoken.encode("utf-16le")),
            "ltoken": b64.b64encode(self.ltoken.encode("utf-16le")),
            "id": self.id,
            "name": self.name,
        }
        bit_data = p.dumps(data)
        file = open(f"{name}.uid", "wb")
        file.write(bit_data)

    def load(self, name):
        file = open(f"{name}", "rb")
        bit_data = file.read()
        data = p.loads(bit_data)
        self.uid = data["uid"]
        self.region = data["region"]
        self.ok = data["ok"]
        self.os = data["os"]
        self.str_uid = str(data["uid"])
        self.stoken = b64.b64decode(data["stoken"]).decode("utf-16le")
        self.id = data["id"]
        self.cookie = b64.b64decode(data["ck"]).decode("utf-16le")
        self.name = data["name"]
        self.ltoken = b64.b64decode(data["ltoken"]).decode("utf-16le")
        return self


HuTaoApi = "https://homa.snapgenshin.com"
HuTaoRecordApi = f"{HuTaoApi}/Record"
HuTaoStatisticsApi = f"{HuTaoApi}/Statistics"
HuTaoStatisticsWeaponApi = f"{HuTaoStatisticsApi}/Weapon"
HuTaoStatisticsTeamApi = f"{HuTaoStatisticsApi}/Team"
HuTaoStatisticsAvatarApi = f"{HuTaoStatisticsApi}/Avatar"


LauncherApi = "https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api"
LauncherContentApi = f"{LauncherApi}/content"
LauncherResourceApi = f"{LauncherApi}/resource"

LauncherApi_sr = "https://api-launcher.mihoyo.com/hkrpg_cn/mdk/launcher/api"
LauncherContentApi_sr = f"{LauncherApi_sr}/content"
LauncherResourceApi_sr = f"{LauncherApi_sr}/resource"

LauncherID = {"ys": "18", "sr": "33"}
LauncherKey = {"ys": "eYd89JmJ", "sr": "6KcVuOkbcqjJomjZ"}
