import os
import importlib
import inspect
from flask import abort
from env import *


class Plugin:
    __name__ = ""
    __version__ = ""
    __description__ = ""
    __author__ = ""

    def __init__(self):
        self.root = (
            os.path.dirname(os.path.realpath(sys.argv[0]))
            + "\\plugins\\"
            + self.__name__
        )

    def route_main(self, req):
        return "Plugin Index"

    def before_request(self, req):
        return True

    def route_files(self, req):
        static_path = os.path.join(self.root, "static")
        path_list = req.path.split("/")
        file_path = ""
        for path in path_list[3:]:
            if path_list[3:].index(path) == 0:
                file_path = path
            else:
                file_path = file_path + "/" + path
        if file_path == "":
            return "Files"
        else:
            try:
                f = open(static_path + "\\" + file_path, "rb")
                data = f.read()
            except Exception as e:
                log.error("File Not Found")
                return "File Not Found"
            else:
                return data


def load_plugins(dir):
    plugin_dir = dir
    plugins = []
    pre_fix = plugin_dir.replace("\\", ".").replace("/", ".")
    for file_name in os.listdir(plugin_dir):
        if not os.path.isdir(dir + "/" + file_name):
            module_name = file_name.split(".")[0]
            module = importlib.import_module(pre_fix + "." + module_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
                    plugins.append(obj())
        else:
            module = importlib.import_module(pre_fix + "." + file_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
                    plugins.append(obj())
    return plugins


def run_funcion(plugins, funcion, *args, **kwargs):
    ret_data = []
    for plugin in plugins:
        try:
            plu = getattr(plugin, funcion)
            ret = plu(*args, **kwargs)
            ret_data.append(ret)
        except Exception as e:
            pass
    return ret_data


def run_one_funcion(plugins, name, funcion, *args, **kwargs):
    ret = "Nones"
    for plugin in plugins:
        if plugin.__name__ == name:
            try:
                plu = getattr(plugin, funcion)
                ret = plu(*args, **kwargs)
            except AttributeError as e:
                # log.error(e)
                ret = "Nones"
            break
        else:
            ret = "Nones"

    if ret == "Nones":
        return abort(404)
    else:
        return ret


def get_plugin_info(plugins):
    ret_data = []
    for plugin in plugins:
        try:
            ret_data.append(plugin.info)
        except Exception as e:
            pass
    return ret_data
