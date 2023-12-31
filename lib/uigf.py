from jinja2 import Template
import time
from api.env import uid

"""
lists = [
    {
      "uigf_gacha_type": "200",
      "gacha_type": "200",
      "item_id": "11301",
      "count": "1",
      "time": "2023-04-07 11:56:46",
      "name": "冷刃",
      "item_type": "武器",
      "rank_type": "3",
      "id": "1680836760001104137"
    }
]
"""


def out_uigf(uid: uid, lists: list, out_path: str):
    f = open("data/template/uigf.txt", encoding="utf-8")
    template = Template(f.read())
    text = template.render(
        uid=uid.uid,
        timestamp=int(time.time()),
        time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        lists=lists,
    )
    cf = open(out_path, "w", encoding="utf-8")
    cf.write(text)
