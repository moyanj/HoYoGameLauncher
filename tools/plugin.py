
import os
import importlib


def load_plugins(dir):
    plugin_dir = dir  # 替换为你的插件目录的路径
    plugins = []
    pre_fix = plugin_dir.replace("\\", ".").replace("/", ".")
    for file_name in os.listdir(plugin_dir):
        if file_name.endswith(".py"):
            module_name = file_name[:-3]
            module = importlib.import_module(pre_fix + "." + module_name)
            module_name = module.__name__
            plugins.append(module)

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

def run_one_funcion(plugins,name, funcion, *args, **kwargs):
    try:
        for plugin in plugins:
            if plugin.info["name"] == name:
                plu = getattr(plugin, funcion)
                ret = plu(*args, **kwargs)
                break
            ret = "None"
    except Exception as e:
        print(e)
        return "None"
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