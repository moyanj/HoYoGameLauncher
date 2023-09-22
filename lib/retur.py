import json
from flask import make_response


def Rest(msg: str = "OK", status_code: int = 200, data: dict = None):
    """Rest

    Keyword Arguments:
        msg -- 消息 (default: {"OK"})
        status_code -- 状态码 (default: {200})
        data -- 数据 (default: {None})

    Returns:
        处理后的返回字符串
    """
    ret_dict = {"Msg": msg, "Code": status_code, "Data": data}
    retStr = json.dumps(ret_dict, indent=4, ensure_ascii=False)
    req = make_response(retStr)
    req.status_code = status_code
    req.headers["Content-Type"] = "application/json; charset=utf-8"

    return req
