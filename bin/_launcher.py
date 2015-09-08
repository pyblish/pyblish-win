"""Bootstrap a given Pyblish application prior to launching"""

import os
import sys
import subprocess


def setup(root):
    pythonpath = os.path.realpath(os.path.join(root, "..", "pythonpath"))
    pyqtdir = os.path.realpath(os.path.join(root, "..", "lib", "python-qt5"))

    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = os.pathsep.join(
        [pythonpath, pyqtdir, PYTHONPATH])


def main(root, program, args=None):
    """Command-line entry point

    Arguments:
        root (str): Directory from which executable is launched
        program (str): Name of program, e.g. pyblish-qml
        async (bool, optional): Run asynchronously, default is False
        console (bool, optional): Run with console, default is False
        args (list, optional): Additional arguments passed to program

    """

    setup(root)

    args = [sys.executable,
            "-u",  # Unbuffered, for outputting to stdout below
            "-m", program] + args or []

    CREATE_NO_WINDOW = 0x08000000
    popen = subprocess.Popen(args,
                             creationflags=CREATE_NO_WINDOW,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

    for line in iter(popen.stdout.readline, b""):
        sys.stdout.write(line)

    popen.communicate()  # Block until done


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Absolute path to /bin directory")
    parser.add_argument("program", help="Name of program, e.g. pyblish_qml")
    parser.add_argument("--console", action="store_true", help="Deprecated")
    parser.add_argument("--async", action="store_true", help="Deprecated")

    kwargs, args = parser.parse_known_args()

    if kwargs.__dict__.pop("console"):
        print("--console has been deprecated")
    if kwargs.__dict__.pop("async"):
        print("--async has been deprecated")

    main(args=args, **kwargs.__dict__)
