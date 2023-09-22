from env import *


def GameRecordRoleBasicInfo(uid: Player):
    return f"{ApiTakumiRecordApi}/roleBasicInfo?role_id={uid.uid}&server={uid.region}"


def GameRecordSpiralAbyss(scheduleType, uid: Player):
    return f"{ApiTakumiRecordApi}/spiralAbyss?schedule_type={scheduleType}&role_id={uid.uid}&server={uid.region}"


def AnnouncementsList():
    return f"{Hk4eApiAnnouncementApi}/getAnnList?{AnnouncementQuery}"


def AnnouncementContent():
    return f"{Hk4eApiAnnouncementApi}/getAnnContent?{AnnouncementQuery}"


def GameRecordDailyNote(uid: Player):
    return f"{ApiTakumiRecordApi}/dailyNote?server={uid.region}&role_id={uid.uid}"


def LauncherContent(game):
    if game == "ys":
        return f"{LauncherContentApi}?key={LauncherKey[game]}&launcher_id={LauncherID[game]}&language=zh-cn"
    else:
        return f"{LauncherContentApi_sr}?key={LauncherKey[game]}&launcher_id={LauncherID[game]}&language=zh-cn"


def HuTaoUpload(Rank: bool = False):
    url = f"{HuTaoRecordApi}/Upload?returningRank="
    if Rank:
        url = url + "true"
    else:
        url = url + "false"
    return url


def Ltoken() -> str:
    return f"{ApiTakumiAuthApi}/getMultiTokenByLoginTicket"
