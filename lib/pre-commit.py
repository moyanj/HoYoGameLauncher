import os
import click
import time

# 获取当前版本号
with open("./data/version.txt", "r") as version_file:
    current_version = version_file.read()


# 更新版本号
def dev():
    big_ver = current_version.split("-")[0]
    small = "-Dev-" + str(int(time.time()))
    new_version = big_ver + small
    return new_version


def sta():
    big_ver = current_version.split("-")[0]
    ver_couter = big_ver.split(".")
    ver_couter_int = []
    for i in ver_couter:
        ver_couter_int.append(int(i))
    ver_couter_int[2] = ver_couter_int[2] + 1
    if ver_couter_int[2] > 8:
        ver_couter_int[2] = 0
        ver_couter_int[1] = ver_couter_int[1] + 1
    if ver_couter_int[1] > 10:
        ver_couter_int[1] = 0
        ver_couter_int[0] = ver_couter_int[0] + 1
    new_version = ".".join(str(i) for i in ver_couter_int)
    return new_version


@click.command()
@click.option("-t", default="dev", help="当前版本号")
def main(t):
    global current_version
    if t == "dev":
        new_version = dev()
    elif t == "sta":
        new_version = sta()
    elif t == "pre":
        try:
            ver = current_version.split("-Pre")
            new_version = ver[0] + "-Pre" + str(int(ver[1]) + 1)
        except:
            if "Dev" in current_version:
                ver = current_version.split("-")
                big_ver = ver[0]
                new_version = big_ver + "-Pre1"
            else:
                current_version = sta()
                new_version = current_version + "-Pre1"

    else:
        exit()

    with open("./data/version.txt", "w") as version_file:
        version_file.write(new_version)


if __name__ == "__main__":
    main()
