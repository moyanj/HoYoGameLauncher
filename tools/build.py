import click
import os
import shutil
import zipfile


def getZipDir(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, "")

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

    zip.close()


@click.group(
    help="""
    This command line is applicable to the packaging of HoYoGameLauncher
    """
)
def cli():
    pass


@cli.command(help="Package a separate server")
def pack_server():
    os.system(
        "pyinstaller --workpath ./build/work --specpath ./build/ --distpath ./pack --icon ../config/icon_server.ico -F server.py"
    )


@cli.command(help="pack app")
def pack():
    try:
        shutil.rmtree("./build")
        shutil.rmtree("./pack")
        shutil.rmtree("./main")
        shutil.rmtree("package")
    except:
        pass
    os.system(
        "pyinstaller --workpath ./build/work --specpath ./build/ --distpath ./ -w --icon ../config/icon.ico main.py"
    )

    os.rename("./main", "./pack")
    os.rename("./pack/main.exe", "./pack/HoYoGameLauncher.exe")
    shutil.copytree("html", "pack/html")
    shutil.copytree("static", "pack/static")
    shutil.copytree("language", "pack/language")
    shutil.copy("config.example.json", "pack/config.json")
    try:
        os.mkdir("./pack/log")
    except:
        pass


@cli.command(help="zip app")
def zip():
    os.mkdir("package")
    getZipDir(dirpath="./pack", outFullName="./package/HoYoGameLauncher.zip")


if __name__ == "__main__":
    cli()
