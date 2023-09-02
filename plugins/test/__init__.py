from lib.plugin import Plugin
from flask import abort


class Plugins(Plugin):
    __name__ = "test"
    def __init__(self):
        super().__init__()

    def route_main(self, req):
        return "ok"

    def route_type(self, req):
        return 1
    def route_name(self, req):
        raise NameError

    def route_404(self, req):
        return abort(404)

    def route_500(self, req):
        return abort(500)

    def route_403(self, req):
        return abort(403)

    def route_400(self, req):
        return abort(400)

    def route_401(self, req):
        return abort(401)

    def route_405(self, req):
        return abort(405)

    def route_408(self, req):
        return abort(408)
