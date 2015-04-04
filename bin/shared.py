import os
import sys

bindir = os.path.dirname(__file__)
repodir = os.path.dirname(bindir)
libdir = os.path.join(repodir, "lib")
suitedir = os.path.join(libdir, "pyblish-suite")
pyqtdir = os.path.join(libdir, "python-qt5")


def setup():
    setup_environment()
    setup_pyqt()


def setup_environment():
    base = os.path.abspath(suitedir)

    for repo in ("pyblish",
                 "pyblish-maya",
                 "pyblish-endpoint",
                 "pyblish-qml"):
        path = os.path.join(base, repo)
        PYTHONPATH = os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = path + (os.pathsep + PYTHONPATH)

    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = pyqtdir + (os.pathsep + PYTHONPATH)


def setup_pyqt():
    sys.path.insert(0, pyqtdir)
    import util
    util.createqtconf()
    sys.path.remove(pyqtdir)
