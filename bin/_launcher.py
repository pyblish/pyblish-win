import os
import sys
import subprocess


def main(root, program, async=False, console=False, args=None):
    repodir = os.path.join(__file__, "..", "..")
    repodir = os.path.realpath(repodir)
    os.environ["PYTHONPATH"] = repodir + os.pathsep + os.environ.get("PYTHONPATH", "")

    args = [sys.executable, "-m", program] + args or []
    kwargs = dict()

    if not console:
        CREATE_NO_WINDOW = 0x08000000
        kwargs["creationflags"] = CREATE_NO_WINDOW

    app = subprocess.Popen(args, **kwargs)

    if not async:
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
