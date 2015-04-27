import os
import sys


package_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.dirname(package_dir)
repository_dir = os.path.dirname(python_dir)


def wrap_module(module):
    """Wrap `module` into corresponding module from Suite

    Arguments:
        module (str): Name of module, e.g. "pyblish"

    """

    library_dir = os.path.join(
        repository_dir,
        "lib",
        "pyblish-suite",
        module)

    if library_dir not in sys.path:
        sys.path.insert(0, library_dir)

    module = module.replace("-", "_")
    mod = __import__(module)
    sys.modules[module] = mod
    reload(mod)


def augment_dependencies():
    """Add PyQt5 to PYTHONPATH"""
    pyqt_path = os.path.join(repository_dir, "lib", "python-qt5")
    assert os.path.isdir(pyqt_path)

    if pyqt_path not in os.environ.get("PYTHONPATH", ""):
        var = pyqt_path + os.pathsep + os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = var

    if pyqt_path not in sys.path:
        sys.path.insert(0, pyqt_path)


def augment_path():
    """Add Python 2.7 to PATH"""
    python_path = os.path.join(repository_dir, "lib", "Python27")
    assert os.path.isdir(python_path)
    if not python_path in os.environ.get("PATH", ""):
        var = python_path + os.pathsep + os.environ.get("PATH", "")
        os.environ["PATH"] = var


def augment_pythonpath():
    """Add Pyblish packages to PYTHONPATH"""
    if python_dir not in os.environ["PYTHONPATH"]:
        print "Adding %s to PYTHONPATH"
        var = python_dir + os.pathsep + os.environ.get("PYTHONPATH", "")
        os.environ["PYTHONPATH"] = var
