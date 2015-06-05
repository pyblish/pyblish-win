import os
import sys


def wrap_module(module):
    """Wrap `module` into corresponding module from Suite

    Arguments:
        module (str): Name of module, e.g. "pyblish"

    """

    library_dir = os.path.join(__file__, "..", "..", "lib", "pyblish-x", "modules", module)
    library_dir = os.path.realpath(library_dir)

    assert os.path.isdir(library_dir), library_dir

    if library_dir not in sys.path:
        sys.path.insert(0, library_dir)

    module = module.replace("-", "_")
    mod = __import__(module)
    sys.modules[module] = mod
    reload(mod)


pythonpath = os.path.dirname(os.path.abspath(__file__))
repository_dir = os.path.dirname(pythonpath)


def install_dependencies():
    """Add PyQt5 to PYTHONPATH"""
    pyqt_path = os.path.join(repository_dir, "lib", "python-qt5")
    assert os.path.isdir(pyqt_path)

    if pyqt_path not in os.environ.get("PYTHONPATH", ""):
        var = pyqt_path + os.pathsep + os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = var

    if pyqt_path not in sys.path:
        sys.path.insert(0, pyqt_path)


def install_path():
    """Add Python 2.7 to PATH"""
    python_path = os.path.join(repository_dir, "lib", "Python27")
    assert os.path.isdir(python_path)
    if python_path not in os.environ.get("PATH", ""):
        var = python_path + os.pathsep + os.environ.get("PATH", "")
        os.environ["PATH"] = var


def install_pythonpath():
    """Add Pyblish packages to PYTHONPATH"""
    if pythonpath not in os.environ["PYTHONPATH"]:
        var = pythonpath + os.pathsep + os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = var
