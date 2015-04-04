import os

bindir = os.path.dirname(__file__)
repodir = os.path.dirname(bindir)


def setup_environment():
    suitedir = os.path.join(repodir, "pyblish-suite")
    base = os.path.abspath(suitedir)

    for repo in ("pyblish",
                 "pyblish-maya",
                 "pyblish-endpoint",
                 "pyblish-qml"):
        path = os.path.join(base, repo)
        PYTHONPATH = os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = path + (os.pathsep + PYTHONPATH)

    pyqtdir = os.path.join(repodir, "python-qt5")
    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = pyqtdir + (os.pathsep + PYTHONPATH)
