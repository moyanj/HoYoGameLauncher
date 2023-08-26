import time
import random
import uuid
import time
import random
import json
from hashlib import md5

# 2.44.1
salt = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"


def ds(type: str = "5", body: dict = {}, query: dict = {}):
    get = ""
    post = json.dumps(body)
    if post == "{}":
        post = ""
    for key, value in query.items():
        if get == "":
            get = key + "=" + value
        else:
            get = get + "&" + key + "=" + value
    get = "&".join(sorted(get.split("&")))
    t = int(time.time())
    r = random.randint(100000, 200000)
    if r == 100000:
        r = 642367
    main = f"salt={salt}&t={t}&r={r}&b={post}&q={get}"
    ds = md5(main.encode(encoding="UTF-8")).hexdigest()
    final = f"{t},{r},{ds}"
    return final


def headers(
    ck: str = "", types: str = "5", url: str = "", body: dict = {}, query: dict = {}
):
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.44.1"
    if types == "5":
        referer = "https://webstatic.mihoyo.com/"
    else:
        referer = "https://app.mihoyo.com"
    url_list = url.split("/")
    hosts = url_list[2]
    origin = f"https://{hosts}"
    headers = {
        "Cookie": ck,
        "x-rpc-app_version": "2.44.1",
        "x-rpc-device_id": str(uuid.uuid3(uuid.NAMESPACE_URL, ua))
        .replace("-", "")
        .upper(),
        "Referer": referer,
        "x-rpc-client_type": types,
        "User-Agent": ua,
        "DS": ds(types, body, query),
        "X-Requested-With": "com.mihoyo.hyperion",
        "Origin": origin,
        "Host": hosts,
        "x-rpc-sys_version": "114514",
        "x-rpc-channel": "homo",
        "x-rpc-device_name": "homo1145141919180",
        "x-rpc-device_model": "1145141919180",
    }
    return headers
