import os
import uuid
import json
import zipfile
import shutil
import sys
from jsmin import jsmin
from cssmin import cssmin

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
    shutil.rmtree("main")
except:
    pass


def getZipDir(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, "")

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

    zip.close()


print("Start packaging 'main'")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {} -w --version-file {}/config/info.txt --icon {}/config/icon.ico {}/main.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir
    )
)

print("Start modifying the main file name")
os.rename("./main", "./build")
os.rename("./build/main.exe", "./build/{}.exe".format(config["name"]))

print("Start packaging 'server'.")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F --version-file {}/config/info.txt --icon {}/config/icon.ico {}/server/app.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir, maindir, maindir
    )
)

print("Start modifying the 'server' file name.")
os.rename("./build/app.exe", "./build/server.exe")


print("Start packaging 'update'.")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F  --version-file {}/config/info.txt {}/update.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir
    )
)

print("Start copying resources.")
shutil.copytree("./html", "./build/html")
shutil.copytree("./server/static", "./build/static")

if len(cli) != 0:
    if "min" in cli:
        print("Start compressing JS and CSS code")
        f = open("./build/static/js/main.js", encoding="utf-8")
        jscode = f.read()
        jsmincode = jsmin(jscode)
        f.close()
        f = open("./build/static/js/main.js", "w", encoding="utf-8")
        f.write(jsmincode)
        f.close()
        f = open("./build/static/css/main.css", encoding="utf-8")
        csscode = f.read()
        cssmincode = cssmin(csscode)
        f.close()
        f = open("./build/static/css/main.css", "w", encoding="utf-8")
        f.write(cssmincode)

if len(cli) != 0:
    if "zip" in cli:
        print("Start packaging into a compressed package")
        os.mkdir("package")
        getZipDir(
            dirpath="./build", outFullName="./package/{}.zip".format(config["name"])
        )


print("All operations completed!")
