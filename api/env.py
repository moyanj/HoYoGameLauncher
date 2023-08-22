import re

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


class uid:
    """
    uid 类
    """

    def __init__(self, str_uid):
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
        self.ok = re.match("^[^34]\d{8}$", uid) != None
        self.region = result
        self.str_uid = str_uid
        self.os = result != "cn_gf01" or result != "cn_qd01"
        # self.server = 1

    def __str__(self):
        return str(self.uid)


LauncherApi = "https://api-launcher.mihoyo.com/hkrpg_cn/mdk/launcher/api"
LauncherContentApi = f"{LauncherApi}/content"
LauncherResourceApi = f"{LauncherApi}/resource"

LauncherID = {"ys": "18", "sr": "33"}
LauncherKey = {"ys": "eYd89JmJ", "sr": "6KcVuOkbcqjJomjZ"}
