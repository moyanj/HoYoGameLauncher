import requests as r
from flask import redirect
import json
import hashlib
def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    return md5_hash.hexdigest()
def get_ysbg():
    req = r.get("https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api/content?filter_adv=true&key=eYd89JmJ&language=zh-cn&launcher_id=18")
    datas = json.loads(req.text)
    all_data = datas["data"]
    adv = all_data["adv"]
    bg = adv["background"]
    req = r.get(bg)
    bg_content = req.content
    bg_md5 = calculate_md5(bg_content)
    print(bg_md5)
    if bg_md5 != adv["bg_checksum"]:
        with open("static/images/ys_bg.png", "wb") as f:
            f.write(bg_content)
            f.close()
        return redirect("/files/images/ys_bg.png")
    else:
        return redirect("/files/images/ys_bg.png")
