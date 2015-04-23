import os
import sys
import subprocess


def setup(root):
    _setup_environment(root)


def _setup_environment(root):
    root = root.rstrip("\\")
    repodir = os.path.dirname(root)
    libdir = os.path.join(repodir, "lib")
    suitedir = os.path.join(libdir, "pyblish-suite")
    pyqtdir = os.path.join(libdir, "python-qt5")

    for repo in ("pyblish",
                 "pyblish-maya",
                 "pyblish-endpoint",
                 "pyblish-qml"):
        path = os.path.join(suitedir, repo)
        PYTHONPATH = os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = path + (os.pathsep + PYTHONPATH)

    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = pyqtdir + (os.pathsep + PYTHONPATH)


def main(root, program, async=False, console=False):
    setup(root)

    args = [sys.executable, "-m", program]
    kwargs = dict()

    if console is False:
        CREATE_NO_WINDOW = 0x08000000
        kwargs["creationflags"] = CREATE_NO_WINDOW

    app = subprocess.Popen(args, **kwargs)

    if async is False:
        return app.communicate()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("program")
    parser.add_argument("--console", action="store_true")
    parser.add_argument("--async", action="store_true")

    kwargs = parser.parse_args()

    main(**kwargs.__dict__)
