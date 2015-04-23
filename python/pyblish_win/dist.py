import os
import re
import json
import shutil
import subprocess

import version


def collect(base):
    """Collect files for distribution

    Arguments:
        base (str): Path to source

    """

    col = list()
    for root, dirs, files in os.walk(base):

        # Exclude Directories
        relpath = os.path.relpath(root, base)
        if any(relpath.startswith(d) for d in (
                ".git",
                "dist",
                "build",
                "lib\\python-qt5\\src",
                "lib\\Python27\\tcl",
                "lib\\Python27\\Doc",
                "lib\\Python27\\include"
                "lib\\Python27\\Tools",
                "lib\\python-qt5\\PyQt5\examples",
                "lib\\python-qt5\\PyQt5\include",
                "lib\\python-qt5\\PyQt5\mkspecs",
                "lib\\python-qt5\\PyQt5\qsci",
                "lib\\python-qt5\\PyQt5\sip",
                "lib\\python-qt5\\PyQt5\translations",
                "lib\\python-qt5\\PyQt5\uic",
                )):
            continue

        for fname in files:

            # Exclude files
            if any(f in fname for f in (
                    ".pyc",
                    "Qt5Web",
                    "QtWeb",
                    "Qt5Multimedia",
                    "QtMultimedia",
                    "icudt53",
                    "opengl32sw",
                    "qtdesigner.dll",
                    "d3dcompiler_47.dll",
                    "QtXmlPatterns.dll",
                    "Qt5Declarative.dll"
                    )):
                continue

            path = os.path.join(root, fname)
            relpath = os.path.relpath(path, base)

            if any(re.match(p, relpath) for p in (
                    "^.*(PyQt5).*(.exe)$",
                    "^(build.bat)$",
                    "^(install.bat)$",
                    "^(reset.bat)$",
                    "^(test.bat)$",
                    "^(update.bat)$",
                    "^(setup.iss)$",
                    "^[.]",
                    )):
                continue

            col.append(relpath)

    return col


def bundle(src, dst):
    """Bundle files from `src` into `dst`

    Arguments:
        src (str): Source directory of files to bundle, e.g. /.
        dst (str): Output directory in which to copy files /build

    """

    print("Collecting files..")

    # Increment build
    package_path = os.path.join(src, "package.json")
    with open(package_path, "r+") as f:
        package = json.load(f)
        package["build"] += 1
        f.seek(0)
        json.dump(package, f, indent=4)

    col = collect(src)

    print("Copying files into /build")
    for fname in col:
        out = os.path.join(dst, fname)

        try:
            os.makedirs(os.path.dirname(out))
        except WindowsError:
            pass

        shutil.copyfile(src=fname, dst=out)

    # Replace with a light-weight version
    shutil.copy(src=os.path.join(src, "icudt53.dll"),
                dst=os.path.join(dst, "lib", "python-qt5", "PyQt5"))

    print("Build finished successfully.")

    return dst


def exe(src, dst):
    """Create installer using Inno Setup

    Arguments:
        src (str): Path to bundle, e.g. /build
        dst (str): Output directory in which to compile installer, e.g. /dist

    """

    print("Creating installer..")

    package_path = os.path.join(src, "package.json")
    with open(package_path) as f:
        build = json.load(f)["build"]

    subprocess.call(["iscc",
                     "/dMyVersion=%s" % version.version,
                     "/dMyBuild=%03d" % build,
                     "/dMyOutputDir=%s" % dst,
                     "setup.iss"])

    print("Successfully created installer")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("--clean", action="store_true")

    kwargs = parser.parse_args()

    base = kwargs.target
    build = os.path.join(base, "build")

    if kwargs.clean and os.path.exists(build):
        print("Cleaning build directory..")

        try:
            shutil.rmtree(build)
        except:
            raise Exception("Could not remove up build directory")

    bundle(src=base, dst=build)
    exe(src=build, dst="dist")
