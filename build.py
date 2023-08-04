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
print("Start cleaning up useless files")
shutil.rmtree("./build/clr_loader/ffi/dlls/x86")
shutil.rmtree("./build/webview/lib/runtimes/win-x86")
shutil.rmtree("./build/webview/lib/runtimes/win-arm64")
os.remove("./build/webview/lib/WebBrowserInterop.x86.dll")
if len(cli) != 0:
    if "zip" in cli:
        print("Start packaging into a compressed package")
        os.mkdir("package")
        getZipDir(
            dirpath="./build", outFullName="./package/{}.zip".format(config["name"])
        )
print("All operations completed!")
