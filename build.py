import os
import uuid
import json
import zipfile
import shutil
import sys

# 有zip约68s
config = json.load(open("config/config.json"))
cli = sys.argv[1:]
tmpdir = os.getenv("TMP")
dirname = config["name"] + "-" + str(uuid.uuid4())
work = os.path.join(tmpdir, dirname)
maindir = os.getcwd()

try:
    shutil.rmtree("build")
    shutil.rmtree("package")
except:
    pass


def getZipDir(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, "")

        for filename in filenames:
            zip.write(os.path.join(path, filename),
                      os.path.join(fpath, filename))

    zip.close()


print("开始打包main")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {} -w --version-file {}/config/info.txt {}/main.py".format(
        work, work, maindir, maindir, maindir
    )
)
os.rename("./main", "./build")
os.rename("./build/main.exe", "./build/{}.exe".format(config["name"]))
os.system(
    "signcode -spc ./config/root.spc -v ./config/root.pvk -t http://timestamp.digicert.com ./build/{}.exe".format(
        config["name"]
    )
)

print("开始打包server")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F --add-data {}/server/file;file/ --version-file {}/config/info.txt {}/server/app.py".format(
        work, work, maindir, maindir, maindir, maindir, maindir
    )
)
os.rename("./build/app.exe", "./build/server.exe")
os.system(
    "signcode -spc ./config/root.spc -v ./config/root.pvk -t http://timestamp.digicert.com ./build/server.exe"
)


print("开始打包update")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F  --version-file {}/config/info.txt {}/update.py".format(
        work, work, maindir, maindir, maindir, maindir
    )
)
os.system(
    "signcode -spc ./config/root.spc -v ./config/root.pvk -t http://timestamp.digicert.com ./build/server.exe"
)

shutil.copytree("./html", "./build/html")
shutil.copytree("./server/file", "./build/file")

if len(cli) != 0:
    if "zip" in cli:
        print("开始打包zip")
        os.mkdir("package")
        getZipDir(
            dirpath="./build", outFullName="./package/{}.zip".format(config["name"])
        )
