import platform as pf
import sys
import time
import os


def crash(error, app):
    system_name = pf.platform()
    computer_name = pf.node()
    computer_system = pf.system()
    computer_bit = pf.architecture()[0]
    file_system = sys.getfilesystemencoding()
    recurdion = sys.getrecursionlimit()
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_stamp = int(time.time())
    try:
        os.mkdir("debug")
    except:
        pass
    f = open("debug.txt", "w", encoding="utf-8")
    f.write("Info: \n")
    f.write("System Name:" + system_name + "\n")
    f.write("Computer Name:" + computer_name + "\n")
    f.write("Computer System:" + computer_system + "\n")
    f.write("Computer Bit:" + str(computer_bit) + "\n")
    f.write("File System:" + file_system + "\n")
    f.write("Recursion Limit:" + str(recurdion) + "\n")
    f.write("Time:" + date + "\n")
    f.write("Time Stamp:" + str(time_stamp) + "\n")
    f.write("\nStack Trace: \n")
    f.write(str(error))
    f.write("\nFlask Log: \n")
    with open("log/flask.log", "r") as file:
        lines = file.readlines()[-20:]
    f.writelines(lines)
    f.write("\nApplication Variables: \n")
    config_list = [
        "template_folder",
        "root_path",
        "config",
        "_static_folder",
        "import_name",
        "name",
    ]
    for key, value in app.__dict__.items():
        if key in config_list:
            if key == "config":
                for key1, value1 in value.items():
                    f.write(key1 + "=" + str(value1) + "\n")
            else:
                f.write(key + "=" + str(value) + "\n")
