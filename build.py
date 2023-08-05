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
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {} -w --icon {}/config/icon.ico {}/main.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir
    )
)

print("Start modifying the main file name")
os.rename("./main", "./build")
os.rename("./build/main.exe", "./build/{}.exe".format(config["name"]))

print("Start packaging 'server'.")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F --icon {}/config/icon_server.ico {}/server/app.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir, maindir, maindir
    )
)

print("Start modifying the 'server' file name.")
os.rename("./build/app.exe", "./build/server.exe")


print("Start packaging 'update'.")
os.system(
    "C: && pyinstaller --workpath {}\\work --specpath {}\\spec --distpath {}/build -F --icon {}/config/icon_update.ico {}/update.py > ./log.txt".format(
        work, work, maindir, maindir, maindir, maindir, maindir
    )
)

print("Start copying resources.")
shutil.copytree("./html", "./build/html")
shutil.copytree("./server/static", "./build/static")

if len(cli) != 0:
    if "min" in cli:
        print("Start compressing JS and CSS code")
        try:
            path = "./build/static/js/"
            for root,dirs,files in os.walk(path):
                for file in files:
                    thispath = os.path.join(root,file)
                    print(thispath)
                    f = open(thispath, encoding="utf-8")
                    jscode = f.read()
                    jsmincode = jsmin(jscode)
                    f.close()
                    f = open(thispath, "w", encoding="utf-8")
                    f.write(jsmincode)
                    f.close()
            path = "./build/static/css/"
            for root,dirs,files in os.walk(path):
                for file in files:
                    print(thispath)
                    thispath = os.path.join(root,file)
                    f = open(thispath, encoding="utf-8")
                    csscode = f.read()
                    cssmincode = cssmin(csscode)
                    f.close()
                    f = open(thispath, "w", encoding="utf-8")
                    f.write(cssmincode)
        except:
            pass

if len(cli) != 0:
    if "zip" in cli:
        print("Start packaging into a compressed package")
        os.mkdir("package")
        getZipDir(
            dirpath="./build", outFullName="./package/{}.zip".format(config["name"])
        )


print("All operations completed!")
