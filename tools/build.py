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
        "pyinstaller --workpath ./build/work --specpath ./build/ --distpath ./pack --icon ../images/icon.ico -F server.py"
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
        "pyinstaller --workpath ./build/work --specpath ./build/ --distpath ./ -w --icon ../images/icon.ico main.py"
    )

    os.rename("./main", "./HoYoGameLauncher")
    os.rename("./HoYoGameLauncher/main.exe", "./HoYoGameLauncher/HoYoGameLauncher.exe")
    shutil.copytree("html", "HoYoGameLauncher/html")
    shutil.copytree("static", "HoYoGameLauncher/static")
    shutil.copytree("language", "HoYoGameLauncher/language")
    shutil.copy("config.example.json", "HoYoGameLauncher/config.json")
    try:
        os.mkdir("./HoYoGameLauncher/log")
        os.mkdir("./HoYoGameLauncher/plugins")
    except:
        pass


@cli.command(help="zip app")
def zip():
    os.mkdir("package")
    getZipDir(dirpath="./pack", outFullName="./package/HoYoGameLauncher.zip")


if __name__ == "__main__":
    cli()
