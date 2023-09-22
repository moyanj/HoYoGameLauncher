import click
import os
import hashlib
import shutil


def md5s(filename):
    file = open(filename, "rb")
    m = hashlib.md5()
    m.update(file.read())
    return m.hexdigest()


@click.group()
def cli():
    print("cli")


@cli.command()
@click.option("--old", help="旧文件夹", default="old")
@click.option("--new", help="新文件夹", default="new")
@click.option("--out", help="输出文件夹", default="out")
def make(old, new, out):
    print("make")
    # 创建文件夹
    if not os.path.exists(out):
        os.mkdir(out)
    old_files = {}
    # 遍历文件
    for root, dirs, files in os.walk(old):
        for file in files:
            old_file = os.path.join(root, file).split(old + "\\")[1]
            old_files[old_file] = md5s(os.path.join(root, file))
    new_files = {}
    for root, dirs, files in os.walk(new):
        for file in files:
            new_file = os.path.join(root, file).split(new + "\\")[1]
            new_files[new_file] = md5s(os.path.join(root, file))
    # 逐一计算MD5
    f = open(os.path.join(out, "del.txt"), "w")
    for file, md5 in old_files.items():
        new_file_md5 = new_files.get(file, "<UNK>")
        if md5 != new_file_md5:
            print("MD5不一", file)
            print(os.path.dirname(os.path.join(out, file)))
            os.makedirs(os.path.dirname(os.path.join(out, file)), exist_ok=True)
            shutil.copy(os.path.join(old, file), os.path.join(out, file))
        elif md5 == "<UNK>":
            print("文件不存在", file)
            f.write(file + "\n")
        else:
            print("MD5一致", file)
    for file, md5 in new_files.items():
        old_file_md5 = old_files.get(file, "<UNK>")
        if old_file_md5 == "<UNK>":
            os.makedirs(os.path.dirname(os.path.join(out, file)), exist_ok=True)
            shutil.copy(os.path.join(new, file), os.path.join(out, file))

    f.close()


if __name__ == "__main__":
    cli()
