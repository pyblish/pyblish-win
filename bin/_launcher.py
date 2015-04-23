import os
import sys
import subprocess

bindir = os.path.abspath(os.path.dirname(__file__))
repodir = os.path.dirname(bindir)
libdir = os.path.join(repodir, "lib")
suitedir = os.path.join(libdir, "pyblish-suite")
pyqtdir = os.path.join(libdir, "python-qt5")


def setup():
    _setup_environment()


def _setup_environment():
    for repo in ("pyblish",
                 "pyblish-maya",
                 "pyblish-endpoint",
                 "pyblish-qml"):
        path = os.path.join(suitedir, repo)
        PYTHONPATH = os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = path + (os.pathsep + PYTHONPATH)

    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = pyqtdir + (os.pathsep + PYTHONPATH)


def main(args, async=False, console=False):
    args = list(args)
    setup()

    program = args.pop(0)

    args = [sys.executable, "-m", program] + args
    kwargs = dict()

    if console is False:
        CREATE_NO_WINDOW = 0x08000000
        kwargs["creationflags"] = CREATE_NO_WINDOW

    app = subprocess.Popen(args, **kwargs)

    if async is False:
        return app.communicate()


if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = dict()

    for flag in ("--console", "--async"):
        try:
            index = args.index(flag)
            kwargs[args.pop(index).strip("-")] = True
        except:
            pass

    main(args, **kwargs)
