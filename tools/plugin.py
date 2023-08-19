import os
import importlib


def load_plugins(dir):
    plugin_dir = dir  # 替换为你的插件目录的路径
    plugins = []
    pre_fix = plugin_dir.replace("\\", ".").replace("/", ".")
    print(pre_fix)
    for file_name in os.listdir(plugin_dir):
        if file_name.endswith(".pyc"):
            module_name = file_name[:-4]
            print(module_name)
            module = importlib.import_module(pre_fix + "." + module_name)
            module_name = module.__name__
            plugins.append(module)

    return plugins


def run_funcion(plugins, funcion, *args, **kwargs):
    for plugin in plugins:
        try:
            plu = getattr(plugin, funcion)
            plu(*args, **kwargs)
        except Exception as e:
            pass
