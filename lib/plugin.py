import os
import importlib
import inspect
from flask import abort


class Plugin:
    def __init__(self):
        self.info = {}

    def route_main(self, req):
        return "Plugin Index"

    def before_request(self, req):
        return True


def load_plugins(dir):
    plugin_dir = dir
    plugins = []
    pre_fix = plugin_dir.replace("\\", ".").replace("/", ".")
    for file_name in os.listdir(plugin_dir):
        if not os.path.isdir(dir +"/" + file_name):

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
    ret = None
    for plugin in plugins:
        if plugin.info["name"] == name:
            plu = getattr(plugin, funcion)
            ret = plu(*args, **kwargs)
            break
        else:
            ret = "None"
    else:
        if ret == "None":
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
