import platform as pf
import sys
import time
import psutil
import os
import moyanlib as mlib
import json
import shutil
import lib

AppDataPath = os.path.join(os.environ["APPDATA"], "HoYoGameLauncher")
save_path = os.path.dirname(os.path.realpath(sys.argv[0]))

def get_current_memory_mb():
    # 获取当前进程内存占用。
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    return str(info.uss / 1024 / 1024)


def crash(error):
    DumpPath = os.path.join(AppDataPath, "ErrorDump")
    if os.path.exists(DumpPath):
        shutil.rmtree(DumpPath)
    os.makedirs(DumpPath, exist_ok=True)
    system_name = pf.node()
    computer_bit = pf.architecture()[0]
    cpu_count = psutil.cpu_count()
    disks = psutil.disk_partitions()
    disks_list = []
    networks = psutil.net_io_counters()
    p = psutil.Process(os.getpid())
    mem = psutil.virtual_memory()

    mem_total = format(float(mem.total) / 1024 / 1024 / 1024, ".3f")
    mem_free = format(float(mem.free) / 1024 / 1024 / 1024, ".3f")
    mem_used = format(float(mem.used) / 1024 / 1024 / 1024, ".3f")

    open_files = []
    for i in disks:
        disk_name = i.device
        disk_type = i.fstype
        diskss = psutil.disk_usage(disk_name)
        disk_total = format(diskss.total / 1024 / 1024 / 1024, ".3f")
        disk_used = format(diskss.used / 1024 / 1024 / 1024, ".3f")
        disk_free = format(diskss.free / 1024 / 1024 / 1024, ".3f")
        disk_info = {
            "Type": disk_type,
            "Name": disk_name,
            "Total": disk_total,
            "Used": disk_used,
            "Free": disk_free,
        }
        disks_list.append(disk_info)

    for i in p.open_files():
        open_files.append(i.path)
    f = open(os.path.join(DumpPath, "System.json"), "w", encoding="utf-8")
    System = {
        "DeviceID":mlib.getDeviceID(),
        "SystemName": system_name,
        "ComputerBit": computer_bit,
        "CPUCount": cpu_count,
        "Disks": disks_list,
        "Networks": {
            "Bytes Sent":networks.bytes_sent,
            "Bytes Recv":networks.bytes_recv,
            "Packages Sent":networks.packets_sent,
            "Packages Recv":networks.packets_recv,
        }
    }
    json.dump(System, f, ensure_ascii=False, indent=4)
    f.close()
    f = open(os.path.join(DumpPath, "Mem.json"), "w", encoding="utf-8")
    Mem = {
        "Total": mem_total,
        "Used": mem_used,
        "Free": mem_free,
        "App":get_current_memory_mb()
    }
    json.dump(Mem, f, ensure_ascii=False, indent=4)
    f.close()
    f = open(os.path.join(DumpPath, "Info.json"), "w", encoding="utf-8")
    Infos = {
        "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "Time Stamp": int(time.time()),
        "Python Version": sys.version.split(" ")[0],
        "Boot Time": psutil.boot_time(),
        "Application":{
            "PID":os.getpid(),
            "Threads Count":p.num_threads(),
            "Open Files":open_files,

        }
    }
    json.dump(Infos, f, ensure_ascii=False, indent=4)
    f.close()
    f = open(os.path.join(DumpPath, "StackTrace"), "w", encoding="utf-8")
    f.write(str(error))
    f.close()
    shutil.copytree(os.path.join(save_path, "log"), os.path.join(DumpPath, "Log"))
    shutil.copytree(os.path.join(save_path, "plugins"), os.path.join(DumpPath, "Plugins"))
    shutil.copy(os.path.join(save_path, "config.json"), os.path.join(DumpPath, "Config.json"))
    # 以树形列出所有文件
    out = os.popen(f"tree {save_path} /F")
    out = out.read()
    f = open(os.path.join(DumpPath, "Files.txt"), "w", encoding="utf-8")
    f.write(out)
    f.close()
    lib.zipDir(DumpPath, os.path.join(save_path, "Dump.hgld"))