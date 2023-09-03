import platform as pf
import sys
import time
import psutil
import os
def get_current_memory_mb():
    # 获取当前进程内存占用。
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    return str(info.uss / 1024 / 1024)

def crash(error, app, flask_e):
    p = psutil.Process(os.getpid())
    mem = psutil.virtual_memory()

    mem_total = format(float(mem.total) / 1024 / 1024 /1024, '.3f')
    mem_free = format(float(mem.free) / 1024 / 1024 /1024, '.3f')
    mem_used = format(float(mem.used) / 1024 / 1024 /1024, '.3f')

    if "TypeError" in error:
        err_type = "1A7JW358NS78000"
    elif "NameError" in error:
        err_type = "1762VB58NS78000"
    elif "IndexError" in error:
        err_type = "95Q68SBR8NT00000"
    else:
        err_type = "NBEDDQ6YXVG"

    system_name = pf.platform()
    computer_name = pf.node()
    computer_system = pf.system()
    computer_bit = pf.architecture()[0]
    file_system = sys.getfilesystemencoding()
    recurdion = sys.getrecursionlimit()
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_stamp = int(time.time())
    cpu_count = psutil.cpu_count()
    disks = psutil.disk_partitions()
    networks = psutil.net_io_counters()
    boot_time = psutil.boot_time()
    python = sys.version.split(" ")[0]

    

    f = open("debug.txt", "w", encoding="utf-8")

    f.write("Info: \n")

    f.write("   Error Code:" + err_type + "\n")
    f.write("   Time:" + date + "\n")
    f.write("   Time Stamp:" + str(time_stamp) + "\n")
    f.write(f"   Python Version: {python}\n")
    f.write("   Total Memory: "+mem_total+" GB\n")
    f.write("   Free Memory: "+mem_free+" GB\n")
    f.write("   Total memory usage: "+mem_used+" GB\n")
    f.write("   Boot Time: " + str(boot_time) + "\n")
    f.write("   Application:\n")
    f.write("       Application occupies memory: "+get_current_memory_mb()+" MB\n")
    f.write("       Application Threads Count: "+str(p.num_threads())+"\n")
    f.write("       Application Process ID: "+str(p.pid)+"\n")
    f.write("       Application Open Files: \n")
    for i in p.open_files():
        f.write("           "+i.path+"\n")
    f.write("   System:\n")
    f.write("       System Name:" + system_name + "\n")
    f.write("       Computer Name:" + computer_name + "\n")
    f.write("       Computer System:" + computer_system + "\n")
    f.write("       Computer Bit:" + str(computer_bit) + "\n")
    f.write("       File System:" + file_system + "\n")
    f.write("       Recursion Limit:" + str(recurdion) + "\n")
    f.write("       CPU Count:" + str(cpu_count) + "\n")
    f.write("   Disks:\n")
    for i in disks:
        disk_name = i.device
        disk_type = i.fstype
        disk = psutil.disk_usage(disk_name)
        disk_total = format(disk.total/1024/1024/1024,'.3f')
        disk_used = format(disk.used/1024/1024/1024,'.3f')
        disk_free = format(disk.free/1024/1024/1024,'.3f')
        f.write(f"      {disk_name}:\n")
        f.write(f"         Type: {disk_type}\n")
        f.write(f"         Total: {disk_total} GB\n")
        f.write(f"         Used: {disk_used} GB\n")
        f.write(f"         Free: {disk_free} GB\n")
        f.write(f"         Percentage: {disk.percent}%\n")
    f.write("   Networks:\n")
    f.write("      Sent: "+str(networks.bytes_sent)+" Bytes\n")
    f.write("      Received: "+str(networks.bytes_recv)+" Bytes\n")
    f.write("      Packets Sent: "+str(networks.packets_sent)+"\n")
    f.write("      Packets Received: "+str(networks.packets_recv)+"\n")

    f.write("\nStack Trace: \n")
    f.write("   "+str(error))

    f.write("\nFlask Log: \n")
    with open("log/flask.log", "r", encoding="utf-8") as file:
        logs = []
        lines = file.readlines()[-20:]
        for line in lines:
            logs.append("   "+line)
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
                    f.write("   "+key1 + "=" + str(value1) + "\n")
            else:
                f.write("   "+key + "=" + str(value) + "\n")

#def upload():
    
