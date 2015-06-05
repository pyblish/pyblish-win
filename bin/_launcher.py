import os
import sys
import subprocess


def setup(root):
    pythonpath = os.path.realpath(os.path.join(root, "..", "pythonpath"))
    pyqtdir = os.path.realpath(os.path.join(root, "..", "lib", "python-qt5"))

    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = pythonpath + os.pathsep + pyqtdir + os.pathsep + PYTHONPATH


def main(root, program, async=False, console=False, args=None):
    """Command-line entry point

    Arguments:
        root (str): Directory from which executable is launched
        program (str): Name of program, e.g. pyblish-qml
        async (bool, optional): Run asynchronously, default is False
        console (bool, optional): Run with console, default is False
        args (list, optional): Additional arguments passed to program

    """

    setup(root)

    args = [sys.executable, "-m", program] + args or []
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

    kwargs, args = parser.parse_known_args()

    main(args=args, **kwargs.__dict__)
