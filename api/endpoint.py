from api.env import *


def GameRecordRoleBasicInfo(uid: uid):
    return f"{ApiTakumiRecordApi}/roleBasicInfo?role_id={uid.uid}&server={uid.region}"


def GameRecordSpiralAbyss(scheduleType, uid: uid):
    return f"{ApiTakumiRecordApi}/spiralAbyss?schedule_type={scheduleType}&role_id={uid.uid}&server={uid.region}"


def AnnouncementsList():
    return f"{Hk4eApiAnnouncementApi}/getAnnList?{AnnouncementQuery}"


def AnnouncementContent():
    return f"{Hk4eApiAnnouncementApi}/getAnnContent?{AnnouncementQuery}"


def GameRecordDailyNote(uid: uid):
    return f"{ApiTakumiRecordApi}/dailyNote?server={uid.region}&role_id={uid.uid}"


def LauncherContent(game):
    if game == "ys":
        print("ys")
        return f"{LauncherContentApi}?key={LauncherKey[game]}&launcher_id={LauncherID[game]}&language=zh-cn"
    else:
        print("other")
        return f"{LauncherContentApi_sr}?key={LauncherKey[game]}&launcher_id={LauncherID[game]}&language=zh-cn"
